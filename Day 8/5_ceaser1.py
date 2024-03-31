alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def encode(message, shift):
    shifted = ""
    for letter in message:
        position = alphabet.index(letter)
        new_position = position+shift
        eachshifts = alphabet[new_position]
        shifted += eachshifts
    print(f"the encoded message is :{shifted}")


a = input("To ENCODE message type 'encode',to DECODE message type 'decode': ").lower()
b = input("Enter your Message:").lower()
c = int(input("Enter your Shift Number:"))

encode(message=b, shift=c)
