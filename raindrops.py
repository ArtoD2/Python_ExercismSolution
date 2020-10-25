def convert(number):
    value = ""
    if number % 3 == 0:
        value += "Pling"
    if number % 5 == 0:
        value += "Plang"
    if number % 7 == 0:
        value += "Plong"
    return value or str(number)