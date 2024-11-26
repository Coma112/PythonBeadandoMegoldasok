def encodeMorse(text: str) -> str:
    morse_dict = {
        'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 
        'F': '.._.', 'G': '__.', 'H': '....', 'I': '..', 'J': '.___', 
        'K': '_._', 'L': '._..', 'M': '__', 'N': '_.', 'O': '___',
        'P': '.__.', 'Q': '__._', 'R': '._.', 'S': '...', 'T': '_', 
        'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._', 'Y': '_.__', 
        'Z': '__..', '1': '.____', '2': '..___', '3': '...__', 
        '4': '...._', '5': '.....', '6': '_....', '7': '__...', 
        '8': '___..', '9': '____.', '0': '_____', ' ': '/'
    }
    
    return ' '.join(morse_dict[char] for char in text.upper() if char in morse_dict)


def decodeMorse(code: str) -> str:
    morse_dict_reversed = {
        '._': 'A', '_...': 'B', '_._.': 'C', '_..': 'D', '.': 'E', 
        '.._.': 'F', '__.': 'G', '....': 'H', '..': 'I', '.___': 'J', 
        '_._': 'K', '._..': 'L', '__': 'M', '_.': 'N', '___': 'O',
        '.__.': 'P', '__._': 'Q', '._.': 'R', '...': 'S', '_': 'T', 
        '.._': 'U', '..._': 'V', '.__': 'W', '_.._': 'X', '_.__': 'Y', 
        '__..': 'Z', '.____': '1', '..___': '2', '...__': '3', 
        '...._': '4', '.....': '5', '_....': '6', '__...': '7', 
        '___..': '8', '____.': '9', '_____': '0', '/': ' '
    }
    
    return ''.join(morse_dict_reversed[code] for code in code.split() if code in morse_dict_reversed)

sentence = input()

def bTask():
    questionCount = 0 # Kérdő
    exclamationCount = 0 # Felszolító
    statementCount = 0 # Kijelentő

    sentences = [sentence.strip() for sentence in sentence.split('.') if sentence]

    for currentCentence in sentences:
        if (currentCentence.endswith("?")):
            questionCount += 1
        elif (currentCentence.endswith(".")):
            statementCount += 1
        else:
            exclamationCount += 1


 
def cTask():
    text = input()

    print(f"{text} -> {encodeMorse(text)}")

def dTask():
    code = input()

    print(f"{code} -> {decodeMorse(code)}")

cTask()
dTask()

