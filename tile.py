#Created on July 8 2014

#@author: Ambarish

#Find Cost of Tile to Cover W x H Floor 
#Calculate the total cost of tile it would take to cover a floor plan of 
#width and height, using a cost entered by the user.

def calc(cost,width,height):
    total = cost*width*height
    return total

cost = float(input("Enter cost per tile: "))
width = float(input("Enter width of room: "))
height = float(input("Enter height of room: "))
total = calc(cost,width,height)
print("The total cost for tiling is ", "$" + '{0:.2f}'.format(total))


