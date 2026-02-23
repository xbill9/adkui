if [ -f "$HOME/project_id.txt" ]; then
    PROJECT_ID=$(cat "$HOME/project_id.txt")
else
    read -p "Enter Project ID: " PROJECT_ID
    echo "$PROJECT_ID" > "$HOME/project_id.txt"
fi

gcloud config set project "$PROJECT_ID"

gcloud services enable aiplatform.googleapis.com
gcloud services enable cloudresourcemanager.googleapis.com
gcloud services enable artifactregistry.googleapis.com
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com

gcloud services enable cloudaicompanion.googleapis.com


curl -s https://raw.githubusercontent.com/haren-bh/gcpbillingactivate/main/activate.py | python3

cat <<EOF> .env
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=$PROJECT_ID
GOOGLE_CLOUD_LOCATION=us-central1
IMAGEN_MODEL="imagen-3.0-generate-002"
GENAI_MODEL="gemini-2.5-flash"
EOF

source .env

gcloud auth application-default login
