import pyautogui
import speech_recognition as sr
from time import sleep

#pip install pynput
#pip install pipwin
#pip install SpeechRecognition
#pip install pyaudio
#pipwin install pyaudio
#pipwin install SpeechRecognition

#from pynput.keyboard import Key, Controller
#keyboard = Controller()

microfone = sr.Recognizer()
source    = sr.Microphone()
jarvis    = True
tempo = 0.3
print('==========================================\nSe a frase Dita for: "Jarvis mudar tela"\no programa será ativado.\nEm execução:\n==========================================\n')
print("Comandos:\n1-jarvis mudar tela\n2-fechar jarvis\n3-jarvis aumente o tempo\n\n")

def compartilhar_tela():
    print("Por favor selecione a janela\n")
    #pyautogui.press("f")
    pyautogui.press("f")
    sleep(tempo)
    pyautogui.press("h")
    sleep(tempo)
    pyautogui.press("f")
    sleep(tempo)
    pyautogui.press("s")
    pyautogui.press("s")

while jarvis:
    frase = ""
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        audio = microfone.listen(source)
        
    try:
        frase = microfone.recognize_google(audio,language='pt-BR')
        print("Você disse: " + frase)

        if frase.lower() == "jarvis mudar tela":
            compartilhar_tela()
        elif frase.lower() == "fechar jarvis":
            jarvis = False
        elif frase.lower() == "jarvis aumente o tempo":
            tempo += 0.3
            
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except Exception as e:
        print("Não entendi")
        print(e)




