def talking_to_assistant(paper_question: str):
    # create thread
    thread = client.beta.threads.create(
        messages=[
            {
                "role": "user",
                "content": paper_question,
            }
        ],
        tool_resources={
            "file_search": {
                "vector_store_ids": [vector_store_id]
            }
        }
    )

    # when yoyu create a run, the tool file-search in the assistant will query
    # on the vector_db that the assitant is tied to.
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id, assistant_id=assitant_id
    )

    messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))

    message_content = messages[0].content[0].text
    annotations = message_content.annotations
    citations = []
    for index, annotation in enumerate(annotations):
        message_content.value = message_content.value.replace(annotation.text, f"[{index}]")
        if file_citation := getattr(annotation, "file_citation", None):
            cited_file = client.files.retrieve(file_citation.file_id)
            citations.append(f"[{index}] {cited_file.filename}")

    return message_content.value
