import PySimpleGUI as sg

sg.theme('DarkAmber')
layout = [ [sg.Text("when did you turn 17?")],
           [sg.Text("Year of birth:"), sg.InputText()],
           [sg.Button('Ok'), sg.Button('Cancel')]]

window = sg.Window('Year 17', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    s = values[0]
    s1 = int(s)
    s2  = s1 + 17
    sg.popup('you were 17 in', s2)
    
    
window.close()