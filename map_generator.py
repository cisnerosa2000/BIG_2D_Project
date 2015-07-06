import random
import numpy as np

x = 27
y = 13

grid = []
gridlist = []
def makegrid():
    global grid
    
    
    for i in range(x):
        grid.append(str(random.randint(0,9)))
                                     #^^^^^^^increase to generate less blocks, decrease to generate more
    my_grid = "".join(grid)
    return my_grid
    


        
with open('map.txt','w') as map_:
    for i in range(y):
        grid = []
        map_.write(   "%s \n" % makegrid() )
    