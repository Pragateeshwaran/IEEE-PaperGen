import os
from dotenv import load_dotenv
from langchain.llms import openai
from langchain.embeddings.openai import OpenAIEmbeddings
from PyPDF2 import PdfReader
from langchain.vectorstores import FAISS 
import pickle 
load_dotenv()
def text_extractor(IEEE_List):
    text = ""
    data_folder = os.path.join(os.path.dirname(__file__), 'data') 

    for IEEE in IEEE_List:
        print(f'Extracting {IEEE}')
        file_path = os.path.join(data_folder, IEEE)
        Paper_reader = PdfReader(file_path)

        for Paper_pages in Paper_reader.pages:
            text += Paper_pages.extract_text()

    with open(os.path.join(os.path.dirname(__file__), 'MyFiles.txt'), 'w', encoding='utf-8') as f:
        f.write(text)
    embeddings = OpenAIEmbeddings()
    VectorStore = FAISS.from_texts(text, embedding=embeddings)
    with open("vector.pkl", "wb") as f:
        pickle.dump(VectorStore, f)

data_folder = os.path.join(os.path.dirname(__file__), 'data')
IEEE_List = os.listdir(data_folder)

text_extractor(IEEE_List)