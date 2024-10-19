import ollama

# CONTEXT_SIZE = 8000


def ollama_llm(prompt: list):
    context_size = len(prompt) * 1.50
    # Inicializar Llama3 y darle el prompt-inicial
    response = ollama.chat(
        model="llama3",
        messages=prompt,
        options={
            "temperature": 0.0,
            "num_ctx": context_size,
        },
    )
    # return response
    return response["message"]["content"]


def merge_instructions(goal: str, backstory: str, messages: list):
    formatted_messages = "\n".join(messages)
    backstory = backstory.replace("{messages}", formatted_messages)
    print(backstory)
    return f"{goal}\n{backstory}\n{messages}"
