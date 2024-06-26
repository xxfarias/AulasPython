for i in range (1, 110):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "é divisível por 3 e 5")
    elif i % 3 ==0:
        print(i, "é divisivel por 3")
    elif i % 5 ==0:
        print(i, "é divisível por 5")
    else:
        print(i)