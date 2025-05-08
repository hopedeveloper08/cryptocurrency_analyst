import ollama

def model(model_name, prompt):
    response = ollama.chat(model=model_name, messages=[
        {'role': 'system', 'content': prompt}])
    return response['message']['content']
