def main():
    print('hello calculator')
    a = 2
    b = 4
    c  = multiply(a,b)
    print(str(a) + " * " + str(b) + ' = ' + str(c))
    
def multiply(x,y):
    # do it wrong 
    #return x / y
    # do it right
    return x * y
    
if __name__ == '__main__':
    main()