################################
# Header

__version__ = 'v1.1'
__author__ = 'mkow04'
__email__ = 'maciejkowalski04@proton.me'
__license__ = 'GPL v3'

################################
# Colors

# List convention: (Color-Code, ANSI-Code, Name)

COLORS = [
    ('&0', '\033[30m', 'Black'),
    ('&1', '\033[34m', 'Dark Blue'),
    ('&2', '\033[32m', 'Dark Green'),
    ('&3', '\033[36m', 'Dark Aqua'),
    ('&4', '\033[31m', 'Dark Red'),
    ('&5', '\033[35m', 'Purple'),
    ('&6', '\033[33m', 'Gold'),
    ('&7', '\033[37m', 'Gray'),
    ('&8', '\033[90m', 'Dark Gray'),
    ('&9', '\033[94m', 'Blue'),
    ('&a', '\033[92m', 'Green'),
    ('&b', '\033[96m', 'Aqua'),
    ('&c', '\033[91m', 'Red'),
    ('&d', '\033[95m', 'Light Purple'),
    ('&e', '\033[93m', 'Yellow'),
    ('&f', '\033[97m', 'White')
]

BACKGROUND_COLORS = [
    ('&B0', '\033[40m', 'Black Background'),
    ('&B1', '\033[44m', 'Dark Blue Background'),
    ('&B2', '\033[42m', 'Dark Green Background'),
    ('&B3', '\033[46m', 'Dark Aqua Background'),
    ('&B4', '\033[41m', 'Dark Red Background'),
    ('&B5', '\033[45m', 'Purple Background'),
    ('&B6', '\033[43m', 'Gold Background'),
    ('&B7', '\033[47m', 'Gray Background'),
    ('&B8', '\033[100m', 'Dark Gray Background'),
    ('&B9', '\033[104m', 'Blue Background'),
    ('&Ba', '\033[102m', 'Green Background'),
    ('&Bb', '\033[106m', 'Aqua Background'),
    ('&Bc', '\033[101m', 'Red Background'),
    ('&Bd', '\033[105m', 'Light Purple Background'),
    ('&Be', '\033[103m', 'Yellow Background'),
    ('&Bf', '\033[107m', 'White Background')
]

EFFECTS = [
    ('&k', '\033[8m', 'Obfuscate'),
    ('&l', '\033[1m', 'Bold'),
    ('&m', '\033[9m', 'Strikethrough'),
    ('&n', '\033[4m', 'Underline'),
    ('&o', '\033[3m', 'Italic'),
    ('&p', '\033[5m', 'Blink'),
    ('&q', '\033[2m', 'Dark'),
    ('&r', '\033[0m', 'Reset')
]

ESCAPE = [
    ('&/', '&', 'Escape')
]

ALL = COLORS + BACKGROUND_COLORS + EFFECTS + ESCAPE

################################
# Functions

def colmap(text: str = '') -> str:
    # Takes in a string containing color codes (as specified in the documentation)
    # and replaces them with ANSI codes accordingly.

    for col_code, ansi_code, desc in ALL:
        text = text.replace(col_code, ansi_code)

    text += '\033[0m'

    return text

def colprint(text: str = '', **kwargs: Any) -> None:
    # Prints a string after replacing color codes (as specified in the documentation)
    # with ANSI codes accordingly. Takes in arguments of the print() function.

    print(colmap(text), **kwargs)

################################
# Main run
# Shows an example of all colors

if __name__ == '__main__':

    print('\n'+colmap('&l&nThis is an example of all the available formatting:'))

    print('\n    '+colmap('&lColors:'))
    for col_code, ansi_code, desc in COLORS:
        print('        '+colmap(f'&l{col_code.replace("&","&/")}&r {col_code}{desc}'))

    print('\n    '+colmap('&lBackground Colors:'))
    for col_code, ansi_code, desc in BACKGROUND_COLORS:
        print('        '+colmap(f'&l{col_code.replace("&","&/")}&r {col_code}{desc}'))

    print('\n    '+colmap('&lEffects:'))
    for col_code, ansi_code, desc in EFFECTS:
        print('        '+colmap(f'&l{col_code.replace("&","&/")}&r {col_code}{desc}'))
    for col_code, ansi_code, desc in ESCAPE:
        print('        '+colmap(f'&l{col_code.replace("&","&/")}&r {col_code}{desc}'))

    print('')
