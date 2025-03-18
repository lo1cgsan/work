def nwd1(a, b):
    while a != b:  # czy a jest różne od b
        if a > b:
            a = a - b
        else:
            b = b - a
    return a 
           
print(nwd1(16, 34))
