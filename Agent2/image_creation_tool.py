import os
import logging
from typing import Union, Dict
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.adk.tools import ToolContext

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def create_image(prompt: str, tool_context: ToolContext) -> Union[Dict, str]:
    """
    Generates an image based on a text prompt using the Google GenAI SDK (Vertex AI).

    Args:
        prompt: The text prompt to generate the image from.
        tool_context: The ADK tool context for saving artifacts.

    Returns:
        A dictionary with status, message, and artifact_name on success, or an error message string on failure.
    """
    logger.info(f"Attempting to generate image for prompt: '{prompt}'")

    try:
        # Load environment variables from .env file two levels up
        dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
        load_dotenv(dotenv_path=dotenv_path)
        
        project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
        location = os.getenv("GOOGLE_CLOUD_LOCATION")
        model_name = os.getenv("IMAGEN_MODEL", "imagen-3.0-generate-002")

        if not all([project_id, location]):
            return "Error: Missing GOOGLE_CLOUD_PROJECT or GOOGLE_CLOUD_LOCATION in .env file."

        client = genai.Client(
            vertexai=True,
            project=project_id,
            location=location,
        )

        response = client.models.generate_images(
            model=model_name,
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="16:9",  # Consistent with the comic book project's standard
                safety_filter_level="block_low_and_above",
                person_generation="allow_adult",
            ),
        )

        if not response.generated_images:
            return "Error: No image was generated."

        # Process the first generated image
        generated_image = response.generated_images[0]
        image_bytes = generated_image.image.image_bytes
        
        # Use a unique name for the artifact
        counter = str(tool_context.state.get("loop_iteration", 0))
        artifact_name = f"generated_image_{counter}.png"
        
        # Save as ADK artifact
        report_artifact = types.Part.from_bytes(
            data=image_bytes, 
            mime_type="image/png"
        )
        await tool_context.save_artifact(artifact_name, report_artifact)
        
        logger.info(f"Image generated and saved as ADK artifact: {artifact_name}")
        
        return {
            "status": "success",
            "message": f"Image generated successfully. ADK artifact: {artifact_name}.",
            "artifact_name": artifact_name,
        }

    except Exception as e:
        error_message = f"An error occurred during image generation: {e}"
        logger.error(error_message)
        return error_message
