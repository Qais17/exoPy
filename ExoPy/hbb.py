message = 'TESTS'

abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','T','S','U','V','W','X','Y','Z']

def code(message, decallage):
    
    for i in message:
        
        print(i)
        index_initial = abc.index(i)
        print(index_initial)
        index_final = index_initial + int(decallage)
        print(index_final)