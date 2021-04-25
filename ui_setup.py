import PySimpleGUI as sg

class UI:
    
    pad = (30, 2)
    layout = [
        [sg.Button('PWN', size=(10, 2), pad=pad), sg.Button('Inject', size=(10, 2), pad=pad), sg.Button(
            'Reset', size=(10, 2), pad=pad), sg.Button('Quit', size=(10, 2), pad=pad)],
        [sg.Text(size=(100, 15), key='-OUTPUT-', background_color='#202124',grab=True)]]

    window = sg.Window('FancyRat', layout, size=(
        800, 480), font=('Hack-Regular', 14))

    window.BackgroundColor = '#081a2b'
    window.ButtonColor = (('#FFFFFF', '#ad460e'))