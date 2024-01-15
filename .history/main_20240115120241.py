from staff import staffz
import datetime
unique_number1 = input('enter your staff unique number? ')
name = input("your name")
x = datetime.datetime.now()
y = x.hour == 8, 7, 6


staff1 = staffz("michael", "FOL2024001")
staff2 = staffz("Tobi", "FOL2024002")

if x != y:
    print("Welcome" + " " + name + " " + "You are late")
    print(x)
elif x == y:
    print("Welcome" + " " + name + " " + "You came early")
    print(x)
