# Morse code converter

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

def text_to_morse(text):
    morse = ""
    for char in text:
        if char.upper() in morse_code:
            morse += morse_code[char.upper()] + " "
        elif char == " ":
            morse += " "
    return morse.strip()

def morse_to_text(morse):
    text = ""
    morse_words = morse.split("   ")
    for morse_word in morse_words:
        morse_chars = morse_word.split(" ")
        for morse_char in morse_chars:
            for key, value in morse_code.items():
                if value == morse_char:
                    text += key
        text += " "
    return text.strip()

def main():
    print("Morse Code and Text Converter")

    while True:
        print("\n1. Text to Morse Code")
        print("2. Morse Code to Text")
        print("3. Quit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            text = input("\nEnter the text: ")
            morse = text_to_morse(text)
            print("Morse Code:", morse)
        elif choice == "2":
            morse = input("\nEnter the Morse code: ")
            text = morse_to_text(morse)
            print("Text:", text)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
