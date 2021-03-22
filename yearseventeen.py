import PySimpleGUI as sg

sg.theme('DarkAmber')
layout = [ [sg.Text("When did you turn 17? \n(don't use backspace or delete, just highlight and type over if new year needed)\n")],
           [sg.Text("Year of birth:"), sg.InputText(enable_events=True)],
           [sg.Text("You turned 17 in:\n")],
           [sg.Text(size=(15,1), key='-OUTPUT-')]]

window = sg.Window('Lesley Year 17 Calculator', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    s = values[0]
    s1 = int(s)
    s2  = s1 + 17   
    if values[0]:
        window['-OUTPUT-'].update(s2)
window.close()