import threading
import openai
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname('~'), ".env")
_ = load_dotenv(dotenv_path)
openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI()

def assistant_talker(assistant_id, vector_store_id, user_prompt:str):
    thread = client.beta.threads.create(
        messages = [
            {
            "role": "user",
            "content": user_prompt
            }
        ],
        tool_resources = {
            "file_search": { "vector_store_ids": [vector_store_id] }
        }
    )

    run = client.beta.threads.runs.create_and_poll(
        thread_id = thread.id, assistant_id = assistant_id
    )

    assistant_responses = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))

    content = assistant_responses[0].content[0].text
    annotations = content.annotations
    citations = []
    for index, annotation in enumerate(annotations):
        content.value = content.value.replace(annotation.text, f"[{index}]")
        if file_citation := getattr(annotation, "file_citation", None):
            cited_file = client.files.retrieve(file_citation.file_id)
            citations.append(f"[{index}] {cited_file.filename}")

    return content.value

threads = []

for i in range(5):
    thread_temp = threading.Thread(target  = foo)
    threads.append(thread_temp)

for t in threads:#manual starting
    t.start()

for t in threads:
    t.join()
