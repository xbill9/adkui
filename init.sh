gcloud services enable aiplatform.googleapis.com
gcloud services enable cloudresourcemanager.googleapis.com

curl -s https://raw.githubusercontent.com/haren-bh/gcpbillingactivate/main/activate.py | python3

cat <<EOF> .env
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=$(gcloud config get-value project)
GOOGLE_CLOUD_LOCATION=us-central1
IMAGEN_MODEL="imagen-3.0-generate-002"
GENAI_MODEL="gemini-2.5-flash"
EOF

gcloud auth application-default login
