from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

client = InferenceClient(api_key=os.getenv('API_KEY'))

messages = [
	{
		"role": "user",
		"content": "Gere um planejamento extramemente resumido para uma aula de português para alunos com autismo, visando a condição dos alunos. Não se esqueça, os alunos possuem problemas neurológicos."
	}
]

completion = client.chat.completions.create(
    model="microsoft/Phi-3.5-mini-instruct", 
	messages=messages, 
	max_tokens=500,
    temperature=0.2
)

print(completion)
print(completion.choices[0].message.content)