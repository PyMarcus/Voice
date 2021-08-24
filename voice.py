import pyttsx3
import sys

# mini diálogo
voz = pyttsx3.init()
print("Choose the options:")
print("1- Hi, what's your name?")
print("2- What's your age?")
print("3- How's life treating you?")
print("4- What do you crave?")
try:
    escolha: int = int(input(">>> "))
except ValueError:
    print("Informe um valor válido")
    sys.exit(1)
except TypeError:
    print("Informe um valor válido")
    sys.exit(1)
else:
    if escolha == 1:
        voz.say("Hi, my name is ROBOT, bro!")
    elif escolha == 2:
        voz.say("I'm 23 years old.")
    elif escolha == 3:
        voz.say("Good, and u?")
    elif escolha == 4:
        voz.say("Learn more")
    else:
        voz.say("Are u crazy? invalid option, bro.")
    voz.runAndWait()

