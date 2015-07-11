import random

x = 27
y = 13

grid = []
gridlist = []

choices = ['a','b','c','d','1','2','3','0','e','f','g']
def makegrid():
    global grid
    
    
    for i in range(x):
        chosen = random.choice(choices)
        grid.append(chosen)
                                     #^^^^^^^increase to generate less blocks, decrease to generate more
    my_grid = "".join(grid)
    return my_grid
    


        
with open('map.txt','w') as map_:
    for i in range(y):
        grid = []
        map_.write(   "%s \n" % makegrid() )
    