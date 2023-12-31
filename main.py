# Sophia Tavio Perez
# Password encoder and decoder


# encode password by incrementing each digit by 3
def encoder(password):
    encoded_password = ""
    for num in password:
        current_num = int(num)
        encoded_password += str((current_num + 3) % 10)
    return encoded_password


def decode_password(input_password):   # Decode the password, subtracting 3 from each digit.
    decoded_password = ""
    for ch in input_password:
        cur_digit = int(ch)
        # Take mod 10 of the digit value minus 3, to ensure that the new digit is actually a digit.
        decoded_password += str((cur_digit - 3) % 10)
    return decoded_password

def main():
    keep_going = True
    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")

        option = int(input("Please enter an option: "))

        # encode password if 1 is chosen
        if option == 1:
            encoded_password = encoder(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!\n")
            keep_going = True
        # decode password if 2 is chosen
        elif option == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
            keep_going = True
        # exit program if 3 is chosen
        else:
            keep_going = False
            break


if __name__ == "__main__":
    main()



