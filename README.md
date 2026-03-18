# ADK Comic Pipeline

This repository contains an agentic pipeline for generating comic books, built using the **Google Agent Development Kit (ADK)** and **Vertex AI**.

It is based on the solution to the codelab: [Create a low-code agent with ADK visual builder](https://codelabs.developers.google.com/codelabs/create-low-level-agent-with-ADK-visual-builder)

## Features

- **Automated Scripting**: Generates creative comic scripts and character manifests from high-level prompts.
- **Intelligent Panelization**: Breaks down scripts into exactly 8 storyboarded panels.
- **AI Image Synthesis**: Generates 16:9 images for each panel using Vertex AI.
- **HTML Assembly**: Compiles the final artwork and script into a responsive HTML comic book.
- **Cloud Deployment**: Scripts included for deploying agents to Google Cloud Run.

## Project Structure

- `Agent1/`: A basic agent featuring a Google Search tool.
- `Agent2/`: An agent focused on image generation using sub-agents.
- `Agent3/`: The primary comic pipeline implementation.
  - `Agent3/tools/`: Custom Python tools for image generation and file handling.
- `images/`: Directory where intermediate panel images are stored.
- `output/`: The final output directory containing `comic.html` and assets.
- `Makefile`: Shortcuts for common development tasks.

## Scripts & Utilities

- `comic.sh`: Starts a local web server (port 8080) to view the generated comic.
- `deploycloudrun.py`: Automates deployment to Google Cloud Run, including IAM and Service Account setup.
- `fix_comic.py`: Manual utility to regenerate the `comic.html` with a default story (Momotaro).
- `set_env.sh`: Helper script to set required environment variables.
- `init.sh` / `set_adc.sh`: Initial setup and authentication helpers.

## How it Works (Agent3)

The system uses a `SequentialAgent` (the `comic_pipeline_agent`) that coordinates four specialized agents:
1. **Scripting Agent**: Narrative and Character Architect.
2. **Panelization Agent**: Cinematographer and Storyboarder.
3. **Image Synthesis Agent**: Technical Artist and Asset Generator.
4. **Assembly Agent**: Frontend Developer for final packaging.

## Known Bugs & Workarounds

*   **Environment Variables**: After creating the `.env` file, run `source .env` or `./set_env.sh` to expose variables.
*   **YAML Nesting**: Agent creation may nest the YAML file in a subdirectory. Move the YAML file to the root of the agent's folder as a workaround.
*   **Issue Tracking**: See [google/adk-python Issue #4134](https://github.com/google/adk-python/issues/4134).

## Getting Started

1.  **Configure Environment**: Set `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION` in the `.env` file or use `./set_env.sh`.
2.  **Authenticate**: Run `gcloud auth application-default login`.
3.  **Install Dependencies**: `pip install -r requirements.txt`.
4.  **Run Pipeline**: Execute the `comic_pipeline_agent` (found in `Agent3/`) using the ADK CLI:
    ```bash
    adk run Agent3 --input "Your comic idea here"
    ```
5.  **View Results**: Run `./comic.sh` and open `http://localhost:8080` in your browser.

## Deployment

To deploy an agent to Google Cloud Run:
```bash
python deploycloudrun.py
```
*Note: Default deployment is configured for Agent1. Edit `deploycloudrun.py` or set environment variables to deploy other agents.*
