import os

# Export OPENAI_API before starting the app. Do not commit a real key.
api_key = os.environ.get("OPENAI_API", "")
# Printed by the notebook when the assistant is created. Override with OPENAI_ASSISTANT_ID.
assistant_id = os.environ.get("OPENAI_ASSISTANT_ID", "asst_VaRmvfp30jPvLuVJgYzxGmXf")
