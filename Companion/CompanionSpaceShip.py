import pyttsx3
import random

# Inicializa o mecanismo de síntese de fala
engine = pyttsx3.init()

# Define a propriedade da voz para uma voz mais aguda
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Seleciona a segunda voz, que geralmente é mais aguda

# Ajusta a velocidade da fala (quanto maior, mais rápido)
engine.setProperty('rate', 150) 

# Ajusta a frequência da voz (quanto maior, mais aguda)
engine.setProperty('pitch', 200) 

# Lista de interesses da criança
interesses = ["elétrica", "programação", "robótica", "computadores"]

# Lista de frases de saudação
saudacoes = ["Oi! Como vai você?", "Olá! Estou animado para conversar com você!", "Oi! O que você está fazendo?"]

# Dicionário de respostas do chatbot
respostas_chatbot = {
    "sobre": "Eu sou um chatbot super legal! Adoro falar sobre eletricidade, programação e muitas outras coisas.",
    "eletricidade": "Elétrica é fascinante! Podemos falar sobre circuitos, eletrônica e muito mais!",
    "programação": "Eu adoro programação! Vamos conversar sobre linguagens de programação e projetos legais!",
    "jogo": "Legal! Vamos jogar um jogo! Qual é a sua pergunta?",
    "obrigado": "De nada! Estou aqui para ajudar sempre que precisar."
}

# Função para interagir com o usuário
def interact():
    print("Bem-vindo ao ChatBot! Estou aqui para conversar com você.")
    print("Você pode enviar mensagens a qualquer momento. Digite 'sair' para encerrar o chat.")

    while True:
        user_input = input("Você: ")

        if user_input.lower() == 'sair':
            print("Até logo!")
            break

        # Verifica se o usuário está iniciando um jogo
        if user_input.lower() == 'jogo':
            print("ChatBot: Vamos jogar um jogo! Pense em um número de 1 a 10 e eu vou tentar adivinhar!")
            jogo_adivinhacao()
            continue

        # Processa a entrada do usuário e obtém uma resposta
        response = processar_entrada(user_input)
        print("ChatBot:", response)
        speak(response)

def processar_entrada(user_input):
    # Verifica se a entrada do usuário corresponde a alguma resposta predefinida
    for chave, resposta in respostas_chatbot.items():
        if chave in user_input.lower():
            return resposta
    
    # Se não houver correspondência, retorna uma resposta padrão
    return "Hmm, não tenho certeza do que você quis dizer. Podemos conversar sobre outra coisa?"

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 3

    while tentativas > 0:
        try:
            palpite = int(input("Você: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue
        
        if palpite == numero_secreto:
            print("ChatBot: Parabéns! Você acertou!")
            speak("Parabéns! Você acertou!")
            break
        elif palpite < numero_secreto:
            print("ChatBot: Muito baixo! Tente um número maior.")
            speak("Muito baixo! Tente um número maior.")
        else:
            print("ChatBot: Muito alto! Tente um número menor.")
            speak("Muito alto! Tente um número menor.")
        
        tentativas -= 1

    if tentativas == 0:
        print("ChatBot: Suas tentativas acabaram! O número secreto era:", numero_secreto)
        speak("Suas tentativas acabaram! O número secreto era " + str(numero_secreto))

def speak(text):
    # Reproduz o texto em áudio
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    interact()
