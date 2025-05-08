from ai_model import model


def app():
    with open('system_prompt.txt', 'r', encoding='utf-8') as f:
        system_prompt = f.read()

    with open('dataset.json', 'r', encoding='utf-8') as f:
        dataset = f.read()

    model_name = 'gemma3'
    prompt = f"data: {dataset}\n\n {system_prompt}"

    print(model(model_name=model_name, prompt=prompt))    
    

if __name__ == '__main__':
    app()
