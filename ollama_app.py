import ollama

prompt = "Who is the cheif minister of Karnataka?"

response = ollama.chat(model="phi3:medium", messages=[{"role": "user", "content": prompt}])

print(response.message.content)