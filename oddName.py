"""
Harry
"""

while True:
    name = str(input("What is you name: "))

    if name.isalpha():
        print("Your name is {}".format(name))
        break

    else: name = str(input("What is your name: "))


print("end")