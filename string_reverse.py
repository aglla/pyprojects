#Reverses a inputted string
#@author Ambarish
#July 8, 2014

def reverse(a):
    '''
    Return the reverse of a string
    >>> reverse('python')
    'nohtyp'
    >>> reverse('code')
    'edoc'
    '''
    # you can iterate under a string....
    return a[::-1]

# you can pass a function as parameter to another function...
print ( reverse( input('Enter a string') ) )

