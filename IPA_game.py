### Author = {'Simon_Smith':'https://github.com/simonalligatorsmith'} ###

#Install PySimpleGui if not already installed
try:
    import PySimpleGUI as sg

except ModuleNotFoundError:
    print("Importing the PySimpleGUI module so the game will display...")
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "PySimpleGui"])
    import PySimpleGUI as sg

import random


### define IPA letters ###
vowels = {'i': {'closeness': 'close', 'backness': 'front', 'roundedness': 'unrounded'},
          'y': {'closeness': 'close', 'backness': 'front', 'roundedness': 'rounded'},
          'ɨ': {'closeness': 'close', 'backness': 'central', 'roundedness': 'unrounded'},
          'ʉ': {'closeness': 'close', 'backness': 'central', 'roundedness': 'rounded'},
          'ɯ': {'closeness': 'close', 'backness': 'back', 'roundedness': 'unrounded'},
          'u': {'closeness': 'close', 'backness': 'back', 'roundedness': 'rounded'},

          'ɪ': {'closeness': 'near-close', 'backness': 'front', 'roundedness': 'unrounded'},
          'ʏ': {'closeness': 'near-close', 'backness': 'front', 'roundedness': 'rounded'},
          'ʊ': {'closeness': 'near-close', 'backness': 'central', 'roundedness': 'rounded'},

          'e': {'closeness': 'close-mid', 'backness': 'front', 'roundedness': 'unrounded'},
          'ø': {'closeness': 'close-mid', 'backness': 'front', 'roundedness': 'rounded'},
          'ɘ': {'closeness': 'close-mid', 'backness': 'central', 'roundedness': 'unrounded'},
          'ɵ': {'closeness': 'close-mid', 'backness': 'central', 'roundedness': 'rounded'},
          'ɤ': {'closeness': 'close-mid', 'backness': 'back', 'roundedness': 'unrounded'},
          'o': {'closeness': 'close-mid', 'backness': 'back', 'roundedness': 'rounded'},

          ### Don't forget mid vowels thru open vowels!!! ###
          'ə': {'closeness': 'mid', 'backness': 'central', 'roundedness': 'unrounded'}
          }
# Template: {'closeness':'','backness':'','roundedness':''},


# Create an event loop
while True:
    # Choose a random symbol
    IPA_symbol = random.choice(list(vowels.keys()))
    question_text = "What is / " + IPA_symbol + ' /?'

    # Create layout of the window (button positioning and such)
    layout = [
        [sg.Text(question_text, font='Courier 30')],
        #  [sg.Button("\tu\t",font='Courier 20')],
        [
            sg.Combo(['close', 'near-close', 'close-mid', 'mid', 'open-mid', 'near-open', 'open']),
            sg.Combo(['front', 'central', 'back']),
            sg.Combo(['unrounded', 'rounded'])
        ],
        [sg.Button("OK", font='Courier 20'), sg.Button("Exit", font='Courier 20')]

    ]

    # Create the window
    window = sg.Window("IPA Game", layout, margins=(100, 50))

    # Extract values for vowel quality from dropdown
    event, values = window.read()
    closeness = values[0]
    backness = values[1]
    roundedness = values[2]

    # Python Terminal output for game
    print(
        '/' + IPA_symbol + '/' + "\tCloseness | Backness | Roundedness",

        '\nGuessed: ', closeness, '\t', backness, '\t', roundedness,

        '\nActual: ', vowels[IPA_symbol]['closeness'], '\t',
        vowels[IPA_symbol]['backness'], '\t',
        vowels[IPA_symbol]['roundedness'], '\n'
    )

    # End program if user closes window or
    # presses the Exit button
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Create a new question in the window
    elif event == "OK":
        continue

window.close()
