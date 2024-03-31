alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def ceaser_cipher(message, shift, direction):
    end_result = ""
    if direction == "decode":
        shift = -shift
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position+shift
            end_result += alphabet[new_position]
        else:
            end_result += char
    print(f"the {direction}d message is :{end_result}")


s_continue = True
while s_continue:
    a = input(
        "To ENCODE message type 'encode',to DECODE message type 'decode': ").lower()
    b = input("Enter your Message:").lower()
    c = int(input("Enter your Shift Number:"))
    c = c % 26
    ceaser_cipher(message=b, shift=c, direction=a)
    result = (
        input("Do you ant to continue encodeing or decoding your messages:")).lower()
    if result == "no":
        s_continue = False
        print("Have a good day!")
    if result == "yes":
        s_continue = True
