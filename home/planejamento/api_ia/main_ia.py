from transformers import pipeline

gerador = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

prompt = "Desenvolva um planejamento de aula de Matemática para alunos do ensino fundamental, ensinando os números de 1 a 9 com atividades interativas."
resposta = gerador(prompt, max_length=300, num_return_sequences=1, temperature=0.7)

print(resposta[0]['generated_text'])