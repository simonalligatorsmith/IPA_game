### Author = {'Simon_Smith':'https://github.com/simonalligatorsmith'} ###

# Thanks to RealPython @ https://realpython.com/pysimplegui-python/
#   for help getting started with the GUI

import random
# Install PySimpleGui if not already installed
try:
    import PySimpleGUI as sg

except ModuleNotFoundError:
    print("Importing the PySimpleGUI module so the game will display...")
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "PySimpleGui"])
    import PySimpleGUI as sg


### define IPA letters ###
vowels = {
        # Close vowels
        'i': {'closeness': 'close', 'backness': 'front',    'roundedness': 'unrounded'},
        'y': {'closeness': 'close', 'backness': 'front',    'roundedness': 'rounded'},
        'ɨ': {'closeness': 'close', 'backness': 'central',  'roundedness': 'unrounded'},
        'ʉ': {'closeness': 'close', 'backness': 'central',  'roundedness': 'rounded'},
        'ɯ': {'closeness': 'close', 'backness': 'back',     'roundedness': 'unrounded'},
        'u': {'closeness': 'close', 'backness': 'back',     'roundedness': 'rounded'},

        # Near-close vowels
        'ɪ': {'closeness': 'near-close', 'backness': 'front',   'roundedness': 'unrounded'},
        'ʏ': {'closeness': 'near-close', 'backness': 'front',   'roundedness': 'rounded'},
        'ʊ': {'closeness': 'near-close', 'backness': 'central', 'roundedness': 'rounded'},

        # Close-mid vowels
        'e': {'closeness': 'close-mid', 'backness': 'front',    'roundedness': 'unrounded'},
        'ø': {'closeness': 'close-mid', 'backness': 'front',    'roundedness': 'rounded'},
        'ɘ': {'closeness': 'close-mid', 'backness': 'central',  'roundedness': 'unrounded'},
        'ɵ': {'closeness': 'close-mid', 'backness': 'central',  'roundedness': 'rounded'},
        'ɤ': {'closeness': 'close-mid', 'backness': 'back',     'roundedness': 'unrounded'},
        'o': {'closeness': 'close-mid', 'backness': 'back',     'roundedness': 'rounded'},

        # Mid vowels
        'e̞': {'closeness': 'mid', 'backness': 'front',   'roundedness': 'unrounded'},
        'ø̞': {'closeness': 'mid', 'backness': 'front',   'roundedness': 'rounded'},
        'ə': {'closeness': 'mid', 'backness': 'central', 'roundedness': 'unrounded'},
        'ɤ̞': {'closeness': 'mid', 'backness': 'back',    'roundedness': 'unrounded'},
        'o̞': {'closeness': 'mid', 'backness': 'back',    'roundedness': 'rounded'},

        # (Note: the 'ɤ̞' diacritic appears discontiguous, but is ok when displayed in the Times New Roman font)

        # Open-mid vowels
        'ɛ': {'closeness': 'open-mid', 'backness': 'front',   'roundedness': 'unrounded'},
        'œ': {'closeness': 'open-mid', 'backness': 'front',   'roundedness': 'rounded'},
        'ɜ': {'closeness': 'open-mid', 'backness': 'central', 'roundedness': 'unrounded'},
        'ɞ': {'closeness': 'open-mid', 'backness': 'central', 'roundedness': 'rounded'},
        'ʌ': {'closeness': 'open-mid', 'backness': 'back',    'roundedness': 'unrounded'},
        'ɔ': {'closeness': 'open-mid', 'backness': 'back',    'roundedness': 'rounded'},

        # Near-open
        'æ': {'closeness': 'near-open', 'backness': 'front',    'roundedness': 'unrounded'},
        'ɐ': {'closeness': 'near-open', 'backness': 'central',  'roundedness': 'unrounded'},

        # Open
        'a': {'closeness': 'open', 'backness': 'front',   'roundedness': 'unrounded'},
        'ɶ': {'closeness': 'open', 'backness': 'front',   'roundedness': 'rounded'},
        'ä': {'closeness': 'open', 'backness': 'central', 'roundedness': 'unrounded'},
        'ɑ': {'closeness': 'open', 'backness': 'back',    'roundedness': 'unrounded'},
        'ɒ': {'closeness': 'open', 'backness': 'back',    'roundedness': 'rounded'},

}### End definitions for vowels ###

# Create an event loop for the
while True:

    # Choose a random symbol from 'vowels'
    IPA_symbol = random.choice(list(vowels.keys()))
    question_text = "What is / " + IPA_symbol + ' /?'

    # Create layout of the window (button positioning and such)
    layout = [
        [sg.Text(question_text, font='Times_New_Roman 30')],

        [
            sg.Combo(['close', 'near-close', 'close-mid', 'mid', 'open-mid', 'near-open', 'open']),
            sg.Combo(['front', 'central', 'back']),
            sg.Combo(['unrounded', 'rounded'])
        ],

        [sg.Button("OK", font='Times_New_Roman 20'), sg.Button("Exit", font='Times_New_Roman 20')]
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

    # Close the old window
    window.close()

    # End program if user closes window or
    # presses the Exit button
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Create a new question in the window
    elif event == "OK":
        continue
