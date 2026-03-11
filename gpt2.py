from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

while True:
    prompt = input("You: ")

    result = generator(prompt, max_length=50)

    print("AI:", result[0]["generated_text"])
