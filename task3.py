string = input("Input your phrase")

string = ' '.join(i[::-1] for i in string.split())

print(string)
