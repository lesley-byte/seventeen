import PySimpleGUI as sg

sg.theme('DarkAmber')
layout = [ [sg.Text("When did you turn 17? ")],
           [sg.Text("Year of birth:"), sg.Input(enable_events=True)],
           [sg.Text("You turned 17 in:\n")],
           [sg.Text(size=(30,1), key='-OUTPUT-')]]

window = sg.Window('Lesley Year 17 Calculator', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event is None:
        break
    try:
        s = values[0]
        s0 = float(s)
        s1 = int(s0)
        s2  = s1 + 17
        s3 = "*Enter a valid year of birth*"
    except ValueError:
        s = 0
        
        continue
    if values[0] and (s2 > 1000):
        window['-OUTPUT-'].update(s2)
        
    else:
        window['-OUTPUT-'].update(s3)
        continue
window.close()
#except ValueError:
#    print("invalid") 
