from transformers import pipeline

pipe = pipeline("text-generation", model="Qwen/Qwen3-0.6B")
messages = [
    {"role": "user", "content": "Jesus is LORD"},
]
print(pipe(messages))
