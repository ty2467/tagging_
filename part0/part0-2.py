import os
from dotenv import load_dotenv

file_path = os.path.join(os.path.expanduser('~'), 'Desktop/tagging_and_store/data/finance_1.csv')
with open(file_path, 'r') as f:
    for line in f:
        print(line+"\n")