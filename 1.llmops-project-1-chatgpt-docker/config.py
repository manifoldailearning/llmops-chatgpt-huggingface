import os

# Export OPENAI_API before starting the app. Do not commit a real key.
api_key = os.environ.get("OPENAI_API", "")
# Vector store id printed by the notebook after client.vector_stores.create.
vector_store_id = os.environ.get("OPENAI_VECTOR_STORE_ID", "")
