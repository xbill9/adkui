import os
import shutil

def write_comic_html(html_content: str, image_directory: str = "images") -> str:
   """
   Writes the final HTML content to a file and copies the image assets.

   Args:
       html_content: A string containing the full HTML of the comic.
       image_directory: The source directory where generated images are stored.

   Returns:
       A confirmation message indicating success or failure.
   """
   output_dir = "output"
   images_output_dir = os.path.join(output_dir, image_directory)

   try:
       # Create the main output directory
       if not os.path.exists(output_dir):
           os.makedirs(output_dir)

       # Copy the entire image directory to the output folder
       if os.path.exists(image_directory):
           if os.path.exists(images_output_dir):
               shutil.rmtree(images_output_dir)  # Remove old images
           shutil.copytree(image_directory, images_output_dir)
       else:
           return f"Error: Image directory '{image_directory}' not found."

       # Write the HTML file
       html_file_path = os.path.join(output_dir, "comic.html")
       with open(html_file_path, "w") as f:
           f.write(html_content)

       return f"Successfully created comic at '{html_file_path}'"

   except Exception as e:
       return f"An error occurred: {e}"
