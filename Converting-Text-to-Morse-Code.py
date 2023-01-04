def to_morse(text):
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
    }
    morse_text = ""
    for char in text:
        char = char.upper()
        if char in morse_dict:
            morse_text += morse_dict[char] + " "
        else:
            morse_text += char + " "
    return morse_text


# Read user input
text = input("Enter text to convert to Morse code: ")

# Convert text to Morse code
morse_text = to_morse(text)

# Print the result
print(morse_text)
