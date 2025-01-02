from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

client = InferenceClient(api_key=os.getenv('API_KEY'))

def generate_planning_ia(term, generate: bool):

	messages = [
		{
			"role": "user",
			"content": f'{term} não se baseie em tópicos, insira tudo em apenas um parágrafo e seja bem resumido, é apenas uma ideia inicial.'
		}
	]

	completion = client.chat.completions.create(
		model="microsoft/Phi-3.5-mini-instruct", 
		messages=messages, 
		max_tokens=1000,
		temperature=0.2
	)

	print(completion)
	print(completion.choices[0].message.content)

# generate_planning_ia('crie um planejamento escolar para alunos com sindome de down para a matéria de matemática (numeros de 1 a 9)', True)