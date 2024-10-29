import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

dotenv_path = os.path.join(os.path.expanduser('~'), '.env')
_ = load_dotenv(dotenv_path) # read local .env file

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

llm_model = "gpt-4o"

model = ChatOpenAI(temperature=0, model=llm_model, openai_api_key=OPENAI_API_KEY)
prompt  = "hello"
templated_prompt  = ChatPromptTemplate.from_template(prompt)
expanded_prompt = templated_prompt.format_messages()

res = model(expanded_prompt)
print(res.content)
