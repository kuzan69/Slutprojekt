import PySimpleGUI as sg
import pandas as pd
from matplotlib import pyplot as plt

def table():

    sg.set_options(auto_size_buttons=True)
    filename = sg.popup_get_file(
        'fil att öppna', no_window=True, file_types=(("CSV Files", "*.csv"),))
    # --- populate table with file contents --- #
    if filename == '':
        return

    data = []
    header_list = []

    #Popup för att programmet ska veta vad den ska göra, visa dina kolumn namn eller skapa egna
    button = sg.popup_yes_no('Har denna fil redan namn på columnen?')

    if filename is not None:
        try:
            # Header = None betyder att du direkt sätter kolumnnamnen i dataframen
            df = pd.read_csv(filename, sep=',', engine='python', header=None)

            # Läs allt i flera rader
            data = df.values.tolist()

            # Välj ja eller nej om din csv fil har namn på columnerna eller inte
            if button == 'Yes':
                #Använder namnen
                header_list = df.iloc[0].tolist()
                data = df[1:].values.tolist()
            
            elif button == 'No':
                #Gör custom columner t.ex. column0, column1, etc
                header_list = ['column' + str(x) for x in range(len(data[0]))]

        #Om något fel uppstår, visa denna popup (error)
        except:
            sg.popup_error('Fel vid läsning av fil')
            return

    layout = [
        [sg.Table(values=data,
                  headings=header_list,
                  display_row_numbers=True,
                  auto_size_columns=False,
                  num_rows=min(25, len(data)))],

        [sg.Button('Skapa diagram'), sg.Button('Filtrera')]
    ]

    window = sg.Window('Tabell för din CSV Fil', layout, grab_anywhere=False)
    
    #Knappar för skapandet av graf, filtrering av tabell eller stapel diagram
    while True:
        event, values = window.read()

        if event == 'Skapa diagram':
            df = pd.read_csv(r"C:\Users\yosef.shiervani\Desktop\WebDev\PySimpleGUI-STOR Uppgift\pokemondata.csv - pokemondata.csv.csv")
            layout = [
                        [sg.Text('Välj en typ av graf som ska visas: '),
                        [sg.Button('Stapel Diagram'), sg.Button('Vanlig graf')]]
            ]
            
            window = sg.Window('Table', layout, grab_anywhere=False)

            #Stapel diagrammet
            plt.figure(figsize=(10, 5))
            plt.bar(df["Name"][:5], df["Attack"][:5])
            plt.title('Graph (Pokemon) - Name / Attack')
            plt.xlabel('Pokemon')
            plt.ylabel('Damage')

            plt.show()
        
        #Elif-sats för filtrering
        elif event == 'Filtrera':
            break
    
    #När allt är klart ska GUI:n försvinna
    window.close()