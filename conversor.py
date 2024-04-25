# CONVERSOR
import colorama
from colorama import Fore
colorama.init(autoreset=True)
while True:
    print(f'{Fore.GREEN} Bem vindo ào Farenheit conversor \n')
    objetivo = str(input("deseja Inserir Celsius ou Farenheit C/F \n"))
    if objetivo == "C" or objetivo == "c":
        inputcelcius = float(input(f'Insira o valor em Celsius para ser convertido para farenheit \n'))
        f = (inputcelcius * 9)/5 + 32
        print(f'O FerenHeit é {f} \n')
    elif objetivo == "F" or 'f':
        x = float(input(f'Insira o valor em farenheit para ser convertido par a celcius \n'))
        c = ((x - 32)/9)*5
        print(f'O Celcius é {c} \n')
    else:
        print("digite um valor valido \n")
        continue