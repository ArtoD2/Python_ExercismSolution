def two_fer(name=''):
    if name == '':
        return 'One for you, one for me.'
    else:
        return f'One for {name}, one for me.'

#SECOND SIMPLER SOLUTION
#def two_fer(name='you'):
#    return f'One for {name}, one for me.'