from huggingface_hub import InferenceClient
from dotenv import load_dotenv
from home.models import PromptIa
from together import Together 
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

def generate_response_ia(messages):
	client = Together(api_key=os.getenv('API_KEY_TOGETHER'))

	response = client.chat.completions.create(
		model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
		messages=messages,
		max_tokens=500,
		temperature=0.8,
		top_p=0.9,
	)
	return response.choices[0].message.content

def question_ia(term, user):
	prompt_ia = PromptIa.objects.get(user=user)
	messages = prompt_ia.context

	messages.append({
		'role': 'user',
		'content': term
	})

	response = generate_response_ia(messages)

	messages.append({
		'role': 'assistant',
		'content': response
	})

	prompt_ia.context = messages
	prompt_ia.save()

	return response

if __name__ == '__main__':
	generate_planning_ia('crie um planejamento escolar para alunos com sindome de down para a matéria de matemática (numeros de 1 a 9)')