from time import sleep
import requests
import pandas as pd
import os

try:
    # chamando a api
    response = requests.get("https://api.exchangerate-api.com/v4/latest/BRL")
    data = response.json()

    # criando o dicionário filtrado
    main = set(['USD', 'EUR', 'JPY', 'GBP', 'CNY', 'AUD', 'CHF', 'CAD', 'HKD', 'NZD'])
    mainList = {curr: value for curr, value in data['rates'].items() if curr in main}

    # Top 10 moedas
    dfMain = pd.DataFrame(list(mainList.items()), columns=['Currency', 'Exchange(BRL)'])

    # Todas as moedas
    dfGeneral = pd.DataFrame(list(data['rates'].items()), columns=['Currency', 'Exchange(BRL)'])

except requests.exceptions.RequestException:
    print(f"It was not possible to obtain the exchanges")
    exit()

while True:
    print("Welcome, please choose which table you would like to view.")
    print("1: Top 10 currencies in the world")
    print("2: All currencies")
    print("3: Exit")

    try:
        choice = int(input("\nChoice: "))
    except ValueError:
        print("Please insert a valid value")
        continue
    
    match(choice):
        case 1:
            print("\n"+ dfMain.to_string(index=False), end='\n\n')
            input("Press Enter to exit. ")
        case 2:
            print("\n"+ dfGeneral.to_string(index=False), end='\n\n')
            input("Press Enter to exit. ")
        case 3:
            print("Thank you for using the program")
            sleep(1)
            break
        case _:
            print("Please insert a valid value", end='\n\n')
            sleep(1)
            continue

    os.system("cls" if os.name == "nt" else "clear")