def listaSoma(lst):
    s = 0
    for elem in lst:
        s += elem
    return s

print(listaSoma([5, 4, 4]))