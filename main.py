#**WAp to check if the given character is in lower case **

char = input("enter a character:")
if "a" <= char <= "z":
    print(f"{char} is lower case character")
else:
    if "A"<= char <= "Z":
        print(f"{char} is uppercase")
    else:
        print(f" {char} is not an alphabet")

# if char.islower():
#     print(f"{char} is lower case character")