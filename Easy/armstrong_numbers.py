def is_armstrong_number(number):
    # convert number into string
    int_to_str = str(number)
    # return number length as value to square
    str_to_len = len(int_to_str)
    # split the string
    seperate = list(int_to_str)
    # invert into integer list for the loop
    lst_to_int_list = list(map(int,seperate)) 
    
    value = 0
    for x in lst_to_int_list:
        value += x ** str_to_len
    return value == number



    

        