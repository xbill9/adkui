import time
import os
import io
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
from dotenv import load_dotenv
import uuid
from typing import Union
from datetime import datetime
from google import genai
from google.genai import types
from google.adk.tools import ToolContext

import logging
import asyncio

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# It's better to initialize the client once and reuse it.
# IMPORTANT: Your Google Cloud Project ID must be set as an environment variable
# for the client to authenticate correctly.


def edit_image(client, prompt: str, previous_image: str, model_id: str) -> Union[bytes, None]:
   """
   Calls the model to edit an image based on a prompt.

   Args:
       prompt: The text prompt for image editing.
       previous_image: The path to the image to be edited.
       model_id: The model to use for the edit.

   Returns:
       The raw image data as bytes, or None if an error occurred.
   """

   try:
       with open(previous_image, "rb") as f:
           image_bytes = f.read()

       response = client.models.generate_content(
           model=model_id,
           contents=[
               types.Part.from_bytes(
                   data=image_bytes,
                   mime_type="image/png",  # Assuming PNG, adjust if necessary
               ),
               prompt,
           ],
           config=types.GenerateContentConfig(
               response_modalities=['IMAGE'],
           )
       )

       # Extract image data
       for part in response.candidates[0].content.parts:
           if part.inline_data:
               return part.inline_data.data

       logger.warning("Warning: No image data was generated for the edit.")
       return None

   except FileNotFoundError:
       logger.error(f"Error: The file {previous_image} was not found.")
       return None
   except Exception as e:
       logger.error(f"An error occurred during image editing: {e}")
       return None

async def generate_image(tool_context: ToolContext, prompt: str, image_name: str, previous_image: str = None) -> dict:
   """
   Generates or edits an image and saves it to the 'images/' directory.

   If 'previous_image' is provided, it edits that image. Otherwise, it generates a new one.

   Args:
       prompt: The text prompt for the operation.
       image_name: The desired name for the output image file (without extension).
       previous_image: Optional path to an image to be edited.

   Returns:
       A confirmation message with the path to the saved image or an error message.
   """
   load_dotenv()
   project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
   if not project_id:
       return "Error: GOOGLE_CLOUD_PROJECT environment variable is not set."
  
   try:
       client = genai.Client(vertexai=True, project=project_id, location="global")
   except Exception as e:
       return f"Error: Failed to initialize genai.Client: {e}"

   image_data = None
   model_id = "gemini-3-pro-image-preview"

   try:
       if previous_image:
           logger.info(f"Editing image: {previous_image}")
           image_data = edit_image(
               client=client,
               prompt=prompt,
               previous_image=previous_image,
               model_id=model_id
           )
       else:
           logger.info("Generating new image")
           # Generate the image
           response = client.models.generate_content(
               model=model_id,
               contents=prompt,
               config=types.GenerateContentConfig(
                   response_modalities=['IMAGE'],
                   image_config=types.ImageConfig(aspect_ratio="16:9"),
               ),
           )

           # Check for errors
           if response.candidates[0].finish_reason != types.FinishReason.STOP:
               return f"Error: Image generation failed. Reason: {response.candidates[0].finish_reason}"

           # Extract image data
           for part in response.candidates[0].content.parts:
               if part.inline_data:
                   image_data = part.inline_data.data
                   break

       if not image_data:
           return {"status": "error", "message": "No image data was generated.", "artifact_name": None}

       # Create the images directory if it doesn't exist
       output_dir = "images"
       os.makedirs(output_dir, exist_ok=True)

       # Save the image to file system
       file_path = os.path.join(output_dir, f"{image_name}.png")
       with open(file_path, "wb") as f:
           f.write(image_data)

       # Save as ADK artifact
       counter = str(tool_context.state.get("loop_iteration", 0))
       artifact_name = f"{image_name}_" + counter + ".png"
       report_artifact = types.Part.from_bytes(data=image_data, mime_type="image/png")
       await tool_context.save_artifact(artifact_name, report_artifact)
       logger.info(f"Image also saved as ADK artifact: {artifact_name}")

       return {
           "status": "success",
           "message": f"Image generated and saved to {file_path}. ADK artifact: {artifact_name}.",
           "artifact_name": artifact_name,
       }

   except Exception as e:
       return f"An error occurred: {e}"
