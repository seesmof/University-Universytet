from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')

prompt = 'Once upon a time'

output = generator(prompt, max_length=100)

print(output)
