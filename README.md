# ADK Comic Pipeline

This repository contains an agentic pipeline for generating comic books, built using the Google Agent Development Kit (ADK) and Vertex AI.

It is based on the solution to the codelab:
[Create a low-code agent with ADK visual builder](https://codelabs.developers.google.com/codelabs/create-low-code-agent-with-ADK-visual-builder)

## Known Bugs
Step 6 - add a source .env after creating the file to expose the variables in the current shell

Step 7- agent creation may nest the yaml file in a subdirectory
workaround is to move the yaml file to the root of the directory

open issue in GitHub:
https://github.com/google/adk-python/issues/4134

## Features

- **Automated Scripting**: Generates creative comic scripts from high-level prompts.
- **Intelligent Panelization**: Breaks down scripts into visualizable panels.
- **AI Image Generation**: Uses `gemini-3-pro-image-preview` to generate and edit panel artwork.
- **HTML Assembly**: Compiles the final product into a shareable HTML comic book.

## Project Structure

- `Agent3/`: The main agent configurations for the comic pipeline.
- `Agent3/tools/`: Custom Python tools for image generation and file handling.
- `images/`: Directory where intermediate panel images are stored.
- `output/`: The final output directory containing `comic.html`.

## How it Works

The system uses a `SequentialAgent` (the `comic_pipeline_agent`) that coordinates four specialized agents:
1. **Scripting Agent**
2. **Panelization Agent**
3. **Image Synthesis Agent**
4. **Assembly Agent**

## Getting Started

1.  **Configure Environment**: Set your `GOOGLE_CLOUD_PROJECT` in the `.env` file.
2.  **Install ADK**: Ensure the Google ADK and required Python packages are installed.
3.  **Run Pipeline**: Execute the `comic_pipeline_agent` using the ADK CLI or runtime.
