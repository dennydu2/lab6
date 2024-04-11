




def encode(n):
    x = []
    for i in str(n):
        x.append(int(i))
    for y in range(len(x)):
        x[y] = x[y]+3
        if x[y] >= 10:
            x[y] = str(x[y]%10)
        else:
            x[y] = str(x[y])
    return "".join(x)



def main():x
    choice = 0
    while choice != 3:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        choice = input("Please enter an option: ")
        if choice == "1":
            num = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        elif choice == "2":
            print("The encoded password is", encode(num),", and the original password is", decode(encode(num)))
        elif choice == "3":
            break



main()