from google import genai

client = genai.Client(
    api_key="coloque_sua_API_key_aqui"
)

def ask(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents= prompt + "Responda em até 250 caracteres.",
    )

    return response.text
    
print("Bem vindo(a) ao Python AI!")
print("===========================")

while(True):
    print("Escolha uma das opções:")
    print("1 - Perguntar para a AI")
    print("0 - Sair")
    print("============================")

    op = int(input("Opção: "))

    if op == 1:
        prompt = input("Faça uma pergunta: ")
        response = ask(prompt)
        print(f"Resposta: {response}")
    elif op == 0:
        print("Até mais!")
        break
    else:
        print("Opção inválida!")
    
    print("===========================")
