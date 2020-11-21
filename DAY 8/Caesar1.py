alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
    string = ""
    for letter in text:
        i = alphabet.index(letter)
        NewIndex = i + shift
        NewLetter = alphabet[NewIndex]
        string += NewLetter
    print(f"Your encryption {string}")

def decrypt(text,shift):
    string = ""
    for letter in text:
        position = alphabet.index(letter)
        NewPosition = position - shift
        NewLetter = alphabet[NewPosition]
        string += NewLetter
    print(f"Your decryption {string}")



choice = input("Enter your choice")
text = input("Enter text to encrypt: ").lower()
shift = int(input("Enter your shift number:"))
shift = shift%26
if choice == "decrypt":
    decrypt(text,shift)
elif choice == "encrypt":
    encrypt(text,shift)
