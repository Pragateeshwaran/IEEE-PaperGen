import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from main import returner

load_dotenv()

client = AzureOpenAI(
  azure_endpoint = "https://openai-demetrius.openai.azure.com/", 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2024-02-15-preview"
)

logits = returner()
message_text = [{"role": "user", "content": logits}, {"role":"system","content":"You are an AI assistant that makes the content for IEEE paper with use of text and time stamp."}]

completion = client.chat.completions.create(
  model="gpt4-demetrius", # model = "deployment_name"
  messages = message_text,
  temperature=0.5,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)
print(completion.choices[0].message.content)

