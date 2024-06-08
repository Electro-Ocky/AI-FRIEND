import subprocess

def chat_with_gpt3(user_input):
    # Substitua este comando com a chamada à API GPT-3 ou outra lógica de geração de texto
    return "Você disse: " + user_input

def text_to_speech(text):
    # Usar o comando espeak para a síntese de fala
    subprocess.call(['espeak', '-ven+f3', '-s150', text])

def main():
    print("Bem-vindo ao Chat de Voz com GPT!")
    print("Você pode começar a conversar digitando suas mensagens.")
    print("Digite 'sair' para encerrar o chat.")

    while True:
        user_input = input("Você: ")
        
        if user_input.lower() == 'sair':
            print("Até logo!")
            break

        # Obter a resposta do modelo GPT-3 (ou simulado)
        response = chat_with_gpt3(user_input)

        # Reproduzir a resposta em áudio
        text_to_speech(response)

if __name__ == "__main__":
    main()
