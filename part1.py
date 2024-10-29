import os
from dotenv import load_dotenv

from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from enum import Enum

dotenv_path = os.path.join(os.path.expanduser('~'), '.env')
_ = load_dotenv(dotenv_path) # read local .env file
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

llm_model = "gpt-4o"
model = ChatOpenAI(temperature=0, model=llm_model, openai_api_key=OPENAI_API_KEY)

class Purpose(Enum):
    CAREER_PATHWAY = 1
    SKILLS_ADVICE = 2
    INTERVIEW_OR_RESUME = 3

class Seriousness(Enum):
    PRACTICAL_OR_IMPLEMENTATIONAL = 1
    GENERAL_OR_CONCEPTUAL = 2
    PERSONAL_OR_CULTURAL = 3

class Formality(Enum):
    FORMAL = 1
    SEMI_FORMAL = 2
    CASUAL = 3

enum_classes = [Purpose, Seriousness, Formality]

def read_in():
    temp_list = []
    file_path = os.path.join(os.path.expanduser('~'), 'Desktop/tagging_and_store/data/finance_1.csv')
    with open(file_path, 'r') as f:
        for line in f:
            # item_in_list = [line, ""]
            item_in_list = {'ITEM': line, 'TAG': ""}
            temp_list.append(item_in_list)
    return temp_list



def tagging(document_item):
    tags = ""

    # for item in temp_list:
    for category in enum_classes:
        prompt = """
        the input in triple backticks is a prompt on a professional q&a forum.
        in triple subtraction lines is members of a enum class, each representing a category within a dimension of categorization
        
        look through the enum along with the input, and decide which tag of the enum best describes the input.
        
        what to return:
        treating this just as a C language enum, return just the int of that enum member, base 1 indexing.
        return only the int and nothing more.
        
        
        ```input: {input}``` 
        ---num:{num}---
        """

        categories = ""
        for element in category:
            # if element.
            categories += element.name + ", "

        templated_prompt = ChatPromptTemplate.from_template(prompt)
        expanded_prompt = templated_prompt.format_messages(input = document_item, num = categories)

        tag_res = model(expanded_prompt)
        tags += tag_res.content


    return tags


def main():
    # tag_try = tagging("what are the unique skills needed for software engineering in art productions")
    # tag_try2 = tagging("hey bro anyone throw sick ass parties on the finance ind in weekends")
    # print(tag_try2)
    read_in_list = read_in()
    i = 0
    for a in read_in_list:
        if i == 30:
            break
        data = a['ITEM']
        a['TAG'] = tagging(data)
        i+=1

    # print(read_in_list)
    items_222 = []
    for d in read_in_list:
        if d['TAG'] == '222':
            items_222.append(d)

    print(items_222)

    file_path = os.path.join(os.path.expanduser('~'), 'Desktop/tagging_and_store/tagged_files/item_222.md')
    with open(file_path, 'w') as f:
        for e in items_222:
            e['ITEM'] = e['ITEM'].replace('\n', ', ')
            f.write(e['ITEM'])
            f.write(e['TAG'])
            f.write('\n')


if __name__ == '__main__':
    main()
#
# file_path_write_to = directory_write_to + "/"
# with open(directory_write_to, 'w') as f:
# #create file
# #write file
# return file_path
