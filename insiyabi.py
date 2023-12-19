i = 0
password = "sansa1234"
while i < 3:
    password_try = str(input("password: "))
    if password == password_try:
        print("welcome")
        break
    else:
        while i < 2:
            print("try again")
            break
    i = i + 1
    if i == 3:
        print("blocked")