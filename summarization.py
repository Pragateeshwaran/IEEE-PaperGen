import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()
def content_generator(logit):
  client = AzureOpenAI(
    azure_endpoint = "https://openai-demetrius.openai.azure.com/", 
    api_key=os.getenv("AZURE_OPENAI_KEY"),  
    api_version="2024-02-15-preview"
  )

  logits = logit
  message_text = [{"role": "user", "content": logits}, {"role":"system","content":"You are an AI assistant that makes the detailed content for IEEE paper in IEEE format for the Text i give you and Use the words and format exactly same as IEEE paper just give me a content except the content dont give any thing else"}]

  completion = client.chat.completions.create(
    model="gpt4-demetrius", 
    messages = message_text,
    temperature=0.5,
    max_tokens=1000,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
  )
  print(completion)
  with open("Content.txt", "w") as f:
    f.write(completion.choices[0].message.content)
  return completion

