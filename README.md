# ADK Comic Pipeline

This repository contains an agentic pipeline for generating comic books, built using the **Google Agent Development Kit (ADK)** and **Vertex AI**.

It is based on the solution to the codelab: [Create a low-code agent with ADK visual builder](https://codelabs.developers.google.com/codelabs/create-low-code-agent-with-ADK-visual-builder)

## Features

- **Automated Scripting**: Generates creative comic scripts and character manifests from high-level prompts.
- **Intelligent Panelization**: Breaks down scripts into exactly 8 storyboarded panels.
- **HTML Assembly**: Compiles the final artwork and script into a responsive HTML comic book.

## Project Structure

- `Agent3/`: The main agent configurations for the comic pipeline.
- `Agent3/tools/`: Custom Python tools for image generation and file handling.
- `images/`: Directory where intermediate panel images are stored.
- `output/`: The final output directory containing `comic.html`.

## How it Works

The system uses a `SequentialAgent` (the `comic_pipeline_agent`) that coordinates four specialized agents:
1. **Scripting Agent**: Narrative and Character Architect.
2. **Panelization Agent**: Cinematographer and Storyboarder.
3. **Image Synthesis Agent**: Technical Artist and Asset Generator.
4. **Assembly Agent**: Frontend Developer for final packaging.

## Known Bugs & Workarounds

*   **Step 6**: After creating the `.env` file, run `source .env` to expose variables in the current shell.
*   **Step 7**: Agent creation may nest the YAML file in a subdirectory. Move the YAML file to the root of the agent's folder as a workaround.
*   **Issue Tracking**: See [google/adk-python Issue #4134](https://github.com/google/adk-python/issues/4134).

## Getting Started

1.  **Configure Environment**: Set `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION` in the `.env` file (or run `./set_env.sh`).
2.  **Authenticate**: Run `gcloud auth application-default login`.
3.  **Install Dependencies**: `pip install -r requirements.txt`.
4.  **Run Pipeline**: Execute the `comic_pipeline_agent` (found in `Agent3/`) using the ADK CLI.
