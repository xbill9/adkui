# Gemini Code Assistant Context

This document provides context for the Gemini Code Assistant to understand the ADK (Agent Development Kit) project for building an agentic comic book pipeline.

## Project Overview

This project implements a multi-agent system using the **Google ADK** to automate the creation of comic books. It follows a sequential pipeline where different specialized agents handle scripting, panelization, image synthesis, and final assembly.

## Key Technologies

*   **Framework:** Google ADK (Agent Development Kit)
https://google.github.io/adk-docs/
*   **Language:** Python 3
*   **Generative AI:** Vertex AI (GenAI SDK)
*   **Models:** ``imagen-3.0-generate-002 (for image generation and editing)
*   **Models:** ``gemini-2.5-flash 
*   **Environment:** `.env` for Google Cloud project configuration

## Project Structure

*   `Agent1/`, `Agent2/`, `Agent3/`: Different stages/versions of agent configurations.
*   `Agent3/`: The primary comic pipeline implementation.
    *   `comic_pipeline_agent.yaml`: Orchestrates the full process.
    *   `scripting_agent.yaml`: Generates the comic script.
    *   `panelization_agent.yaml`: Breaks the script into distinct panels.
    *   `image_synthesis_agent.yaml`: Generates images for each panel.
    *   `assembly_agent.yaml`: Compiles panels into an HTML format.
    *   `tools/`: Python implementations for ADK tools.
        *   `image_generation.py`: Interfaces with Vertex AI for image tasks.
        *   `file_writer.py`: Handles HTML generation and asset management.
*   `images/`: Local storage for generated panel images.
*   `output/`: Contains the final `comic.html` and associated assets.

## Workflow

The `comic_pipeline_agent` (found in `Agent3`) runs a `SequentialAgent` workflow:
1.  **Scripting**: A prompt leads to a comic script.
2.  **Panelization**: The script is divided into panels with descriptions.
3.  **Image Synthesis**: Each panel description is used to generate a 16:9 image via Gemini.
4.  **Assembly**: The images and script are wrapped into a responsive HTML layout.

## Setup & Configuration

1.  **GCP Project**: Ensure `GOOGLE_CLOUD_PROJECT` is set in `.env`.
2.  **Dependencies**: Requires `google-adk`, `google-genai`, `vertexai`, and `python-dotenv`.
3.  **Authentication**: Use `gcloud auth application-default login` for local development.
