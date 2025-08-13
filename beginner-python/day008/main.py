from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")


user_continue = "yes"

print(logo)
while user_continue == "yes":

    direction_invalid = True
    while direction_invalid:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == "encode" or direction == "decode":
            direction_invalid = False
        else:
            print("invalid input!")

    text = input("Type your message:\n").lower()

    shift_invalid = True
    while shift_invalid:
        shift = input("Type the shift number:\n")
        if shift.isnumeric():
            shift_invalid = False
            shift = int(shift)
        else:
            print("invalid input!")

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    user_continue = input("Would you like to go again? type 'yes' or 'no': ").lower()
    if user_continue != "yes":
        print("ok, bye")