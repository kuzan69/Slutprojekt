import PySimpleGUI as sg

def login():
  
  #Färg för login sidan (theme)
  sg.theme('DarkGrey12')

  #Layouten eller GUI:n som visas på skärmen och dess storlek
  layout = [[sg.Text('Logga in')],
            [sg.Text('Användarnamn', size=(20, 2)), sg.InputText()],
            [sg.Text('Lösenord', size=(20, 2)), sg.InputText(password_char='*')],
            [sg.Button('Logga in'), sg.Button('Avbrut')]]

  window = sg.Window('Login fönster', layout)

  while True:
      event, values = window.read()

      #Avbrut funkar nu som (x) längst uppe åt höger, den stoppar koden
      if event == sg.WINDOW_CLOSED or event == 'Avbrut':
          break

      #Inloggning användarnamn och lösenord
      if values[0] == 'Kuzan' and values[1] == 'Kuzan':
          sg.popup('Inloggning Lyckades!')
          break

      #Om inloggning misslyckas (fel inloggning) ska denna popup visas på skärmen
      else:
          sg.popup('Fel vid inloggning, försök igen!')

  #När allt är klart ska GUI:n försvinna
  window.close()