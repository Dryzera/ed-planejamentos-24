from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "microsoft/Phi-3.5-mini-instruct"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def generate_planning_ia(term):

    messages = [
        {"role": "user", "content": term},
        {"role": "assistant", "content": ""}
    ]

    inputs = tokenizer(messages, return_tensors="pt", truncation=True, padding=True, max_length=1024)

    with torch.no_grad():
        outputs = model.generate(
            inputs['input_ids'], 
            max_length=1500, 
            num_return_sequences=1, 
            temperature=0.2, 
            do_sample=False
        )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

if __name__ == '__main__':
	generate_planning_ia('crie um planejamento escolar para alunos com sindome de down para a matéria de matemática (numeros de 1 a 9)')

def not_used():
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