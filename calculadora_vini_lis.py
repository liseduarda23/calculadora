import PySimpleGUI as sg

layout = [ 
    [sg.Input('', key='-DISPLAY-', size=(12, 1))],
    [sg.B('1')],[sg.B('2')],[sg.B('3')],[sg.B('/')],
    [sg.B('4')],[sg.B('5')],[sg.B('6')],[sg.B('*')],
    [sg.B('7')],[sg.B('8')],[sg.B('9')],[sg.B('-')],
    [sg.B('.')],[sg.B('0')],[sg.B('=')],[sg.B('+')],   
]

janela = sg.Window('Calcualdora Lis / Vinicius Henrique', layout = layout, font='monospace 30')

while True:
    event, values = janela.read()

    if event == sg.WIN_CLOSED:
        break
