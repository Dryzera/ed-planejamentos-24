from transformers import pipeline

gerador = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

prompt = """
Crie um planejamento de aula de Matemática para alunos do ensino fundamental, com foco nos números de 1 a 9.
Inclua atividades interativas como:
1. Exercícios para identificar e escrever os números de 1 a 9.
2. Jogos de contagem e associação de números com objetos.
3. Desafios práticos de soma e subtração utilizando os números de 1 a 9.
"""
resposta = gerador(prompt, max_length=1500, temperature=0.2, do_sample=False)

print(resposta[0]['generated_text'])