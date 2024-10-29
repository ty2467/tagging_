import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.expanduser('~'), '.env')
_ = load_dotenv(dotenv_path)

import openai
openai.api_key = os.getenv('OPENAI_API_KEY')

client = openai.OpenAI()


def set_up_vec (vector_store_name, file_paths: list):
    assistant = client.beta.assistants.create(
        name='vector_db_assistant',
        model="gpt-4o",
        tools=[{"type": "file_search"}]
    )

    vector_store = client.beta.vector_stores.create(name=vector_store_name)

    file_streams = [open(path, "rb") for path in file_paths]

    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store.id,
        files=file_streams
    )

    assistant = client.beta.assistants.update(
        assistant_id=assistant.id,
        tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
    )

    return assistant.id, vector_store.id

def main():
    files = []
