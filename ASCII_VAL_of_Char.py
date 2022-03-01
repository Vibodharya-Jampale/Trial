


# Python Program to print ASCII value of A CHARACTER
# A-Z 65-90 and a-z 97-122

def Print_ASCII():    
    Input_Alpha= str(input("Input Your Alphabet for ASCII Value: "))

    print("The ASCII Value of your character",Input_Alpha, "is: ", ord(Input_Alpha))


Print_ASCII()