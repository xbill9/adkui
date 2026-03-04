# Gemini Code Assistant Context

This document provides context for the Gemini Code Assistant to understand the ADK (Agent Development Kit) project for building an agentic comic book pipeline.

## Project Overview

This project implements a multi-agent system using the **Google ADK** to automate the creation of comic books. It follows a sequential pipeline where different specialized agents handle scripting, panelization, image synthesis, and final assembly.

It is based on the solution to the codelab: [Create a low-code agent with ADK visual builder](https://codelabs.developers.google.com/codelabs/create-low-code-agent-with-ADK-visual-builder)

## Key Technologies

*   **Framework:** Google ADK (Agent Development Kit) [Docs](https://google.github.io/adk-docs/)
*   **Language:** Python 3
*   **Generative AI:** Vertex AI (GenAI SDK)
*   **Models:**
    *   **LLM Tasks:** `gemini-2.5-flash` (Used for scripting, panelization, and assembly coordination)
*   **Environment:** `.env` for Google Cloud project configuration (project ID, location, etc.)

## Project Structure

*   `Agent1/`, `Agent2/`, `Agent3/`: Iterative stages of agent configurations.
*   `Agent3/`: The primary comic pipeline implementation.
    *   `comic_pipeline_agent.yaml`: Orchestrates the full process (SequentialAgent).
    *   `scripting_agent.yaml`: Generates the comic script and character manifest.
    *   `panelization_agent.yaml`: Breaks the script into 8 distinct panels.
    *   `image_synthesis_agent.yaml`: Generates images for each panel.
    *   `assembly_agent.yaml`: Compiles panels into an HTML format.
    *   `tools/`: Python implementations for ADK tools.
        *   `image_generation.py`: Interfaces with Vertex AI for image tasks (Gemini-based).
        *   `file_writer.py`: Handles HTML generation and asset management.
*   `images/`: Local storage for generated panel images.
*   `output/`: Contains the final `comic.html` and associated assets.

## Known Bugs & Workarounds

*   **Environment Variables:** After creating the `.env` file, you must `source .env` to expose variables in the current shell.
*   **YAML Nesting:** Agent creation may incorrectly nest the YAML file in a subdirectory. The workaround is to manually move it to the root of the agent's directory.
*   **Issue Tracker:** See [adk-python Issue #4134](https://github.com/google/adk-python/issues/4134).

## Workflow

The `comic_pipeline_agent` (found in `Agent3`) runs a `SequentialAgent` workflow:
1.  **Scripting**: A seed idea is expanded into a script and character manifest.
2.  **Panelization**: The script is divided into exactly 8 panels with detailed descriptions.
3.  **Image Synthesis**: Each panel description is used to generate a 16:9 image.
4.  **Assembly**: The images and script are wrapped into a responsive HTML layout saved in `output/comic.html`.

## Setup & Configuration

1.  **GCP Project**: Ensure `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION` are set in `.env`.
2.  **Dependencies**: Requires `google-adk`, `google-genai`, `vertexai`, and `python-dotenv`.
3.  **Authentication**: Use `gcloud auth application-default login` for local development.
