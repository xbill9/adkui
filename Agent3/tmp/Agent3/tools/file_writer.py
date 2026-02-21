import os
import shutil

def write_comic_html(comic_title: str, panel_data: list) -> str:
    """
    Generates a responsive HTML5 file for the comic book and organizes assets.

    Args:
        comic_title: The title of the comic.
        panel_data: A list of dictionaries, where each dict contains 'panel_number',
                    'description', and 'image_url'.

    Returns:
        The path to the final HTML file.
    """
    output_dir = "output"
    images_dir = os.path.join(output_dir, "images")
    
    # Ensure the main output and images directories exist
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    # Sanitize title for use as a filename
    safe_title = "".join(c for c in comic_title if c.isalnum() or c in (' ', '_')).rstrip()
    file_name = f"{safe_title.replace(' ', '_')}.html"
    file_path = os.path.join(output_dir, file_name)

    # In a real scenario, panel_data would contain remote URLs that need to be
    # downloaded. Here, we assume the 'image_url' from the previous step
    # is already a relative path to a file in 'output/images'. The
    # 'generate_image' tool is designed to place them there directly.
    
    # Start HTML content
    html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{comic_title}</title>
    <style>
        body {{ font-family: sans-serif; background-color: #1a1a1a; color: #f0f0f0; margin: 0; }}
        .container {{ max-width: 800px; margin: 20px auto; padding: 0 15px; }}
        h1 {{ text-align: center; color: #ffc107; }}
        .panel {{ margin-bottom: 30px; border: 2px solid #333; border-radius: 8px; overflow: hidden; background-color: #2b2b2b; }}
        .panel img {{ display: block; width: 100%; height: auto; }}
        .panel .description {{ padding: 15px; font-size: 1.1em; line-height: 1.5; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{comic_title}</h1>
'''

    # Sort panels by number just in case they are out of order
    # Assuming description contains panel number, e.g., "Panel 1: ..."
    def get_panel_num(item):
        try:
            # Extract the first number found in the description
            return int(''.join(filter(str.isdigit, item['description'].split(':')[0])))
        except:
            return 999 # Put items that fail parsing at the end
            
    sorted_panels = sorted(panel_data, key=get_panel_num)

    # Add each panel to the HTML
    for panel in sorted_panels:
        description = panel.get('description', 'No description available.')
        image_url = panel.get('image_url', 'images/placeholder.png')
        html_content += f'''
        <div class="panel">
            <img src="{image_url}" alt="{description}">
            <div class="description">{description}</div>
        </div>
'''

    # Close HTML tags
    html_content += '''
    </div>
</body>
</html>
'''

    # Write the HTML file
    with open(file_path, 'w') as f:
        f.write(html_content)

    print(f"Comic HTML file created at: {file_path}")
    print(f"All image assets are located in: {images_dir}")
    
    return f"Successfully generated the comic. You can find it at: {file_path}"
