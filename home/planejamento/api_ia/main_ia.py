from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

client = InferenceClient(api_key=os.getenv('API_KEY'))
# client = InferenceClient(api_key=os.getenv('API_KEY2'))

def generate_planning_ia(term):

	messages = [
		{
			"role": "user",
			"content": f'{term}'
		}
	]

	completion = client.chat.completions.create(
		model="microsoft/Phi-3.5-mini-instruct", 
		messages=messages, 
		max_tokens=1500,
		temperature=0.2
	)

	response = completion.choices[0].message.content
	return response

if __name__ == '__main__':
	generate_planning_ia('crie um planejamento escolar para alunos com sindome de down para a matéria de matemática (numeros de 1 a 9)')