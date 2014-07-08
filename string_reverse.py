#Reverses a inputted string
#@author Ambarish
#July 8, 2014

def reverse(a):
    list1 = list(a)
    list2 = []
    for x in range(0, len(list1)):
        list2.append(list1.pop())
    result = ''.join(list2)         #joins list elements into a string
    return result

print("Enter a string: ", end = '')
string = input();
res = reverse(string)
print(res)
