from Tkinter import *
import random
import math
import subprocess 
from numpy import deg2rad

root = Tk()
root.title("The Game...")
root.geometry("1366x650+200+0")
canvas = Canvas()
canvas.config(width=1350,height=650,bg='light blue')

###import audio
gunshot_file = "/Users/cisnerosa/documents/Big_2D_Project/Gunshot.mp3"

###import audio



## create windows

ACR = PhotoImage(file='ACR.gif')
L85 = PhotoImage(file='L85.gif')
SCAR = PhotoImage(file='SCAR.gif')


AK74U = PhotoImage(file='AK74U.gif')
Bizon = PhotoImage(file='Bizon.gif')
KRISS = PhotoImage(file='KRISS.gif')
Uzi = PhotoImage(file='Uzi.gif')
UMP = PhotoImage(file='UMP.gif')


M249 = PhotoImage(file='M249.gif')
MG36 = PhotoImage(file='MG36.gif')
RPD = PhotoImage(file='RPD.gif')
M60 = PhotoImage(file='M60.gif')
M27 = PhotoImage(file='M27.gif')


L96 = PhotoImage(file='L96.gif')
M98 = PhotoImage(file='M98.gif')
SVD = PhotoImage(file='SVD.gif')
ScoutElite = PhotoImage(file='ScoutElite.gif')


in_range_crosshair = PhotoImage(file='Crosshair.gif')
not_in_range_crosshair = PhotoImage(file='Crosshair2.gif')
death_message = PhotoImage(file='death.gif')
reload_image = PhotoImage(file='reload.gif')


player_sprite = PhotoImage(file='Player.gif')
bullet_sprite = PhotoImage(file='Bullets.gif')
enemy = PhotoImage(file='Enemy.gif')
out_of_ammo = PhotoImage(file='no_ammo.gif')

block = PhotoImage(file='block.gif')
collide_block = PhotoImage(file='collision_block.gif')
sky_tile = PhotoImage(file='Sky.gif')

### Load sprites


global devmode
devmode = False



### allow guns to be accessed with the string that results from storing names in the text file


gun_lookup = {
    
    #name that is used to signify in the text file:PhotoImage variable name
    
    "ACR":ACR,
    "L85":L85,
    "SCAR":SCAR,
    
    
    "HK417":M27,
    
    
    "Bizon":Bizon,
    "AK74U":AK74U,
    "Vector":KRISS,
    "UMP":UMP,
    "Uzi":Uzi,
    
    
    "M249":M249,
    "MG36":MG36,
    "RPD":RPD,
    "M60":M60,
    "M27":M27,
    
    
    "L96":L96,
    "SVD":SVD,
    "ScoutElite":ScoutElite,
    "M98":M98,
    
    
    ##To be continued as Evan finishes sprites


}
### ^^^ allow guns to be accessed with the string that results from storing names in the text file ^^^


global firing
global bullet_list 
firing = False
bullet_list = []

def make_level():
    global tile_list
    coords = [25,25]
    tile_list = []
    with open('map.txt') as tilemap:
        while True:
            c = (tilemap.read(1))
            if not c:
                break
                
           
           
            if c == """\n""":
                coords[1] += 50
                coords[0] = 25
                make = False
               
            elif c == '0':
                make = True
            elif c == '1':
                tileimg = collide_block
                make = True
            elif c == '2':
                tileimg = block
                make = True
               
            
            if make == True:
                if c != '0':
                    tile = canvas.create_image(*coords,image=tileimg)
                    
                    if c == '1':
                        canvas.itemconfig(tile,tags="player_collide")
                        tile_list.append(tile)
                    elif c == '2':
                        canvas.itemconfig(tile,tags="collide")
                    
                
                
                    
        
                coords[0] += 50
                
                         
            
make_level()



class Environment(object):
    def __init__(self,gravity,friction,jumping):
        self.gravity = gravity
        self.friction = friction
        self.jumping = jumping
        
class Ground(object):
    def __init__(self):
        pass
    def colliding(self):
        self.ground_bbox = canvas.bbox(player.the_player)
        self.collide_list = canvas.find_overlapping(*self.ground_bbox)
        
        for i in self.collide_list:
            if "ground" in canvas.gettags(i):
                return True
                break
        
    def draw_lines(self):
        global tile_list
        for tile in tile_list:
            self.tc = canvas.coords(tile)
            
            self.tile_line = canvas.create_line(self.tc[0]-25,self.tc[1]-30,self.tc[0]+25,self.tc[1]-30,fill="blue",tags="ground")
        
environment = Environment(gravity=.5,friction=1,jumping=False)
ground = Ground()
ground.draw_lines()
class Loadout(object):
    def __init__(self):
        pass
        
    def class_determine(self):
        with open('class.txt','r') as player_loadout:
            file_lines = player_loadout.readlines()
            self.health = int(file_lines[0])
            self.damage = int(file_lines[1])
            self.firerate = int(file_lines[2])
            self.ammo = int(file_lines[3])
            self.range = int(file_lines[4])
            self.mag_cap = int(file_lines[5])
            self.accuracy = float(file_lines[6])
            self.weapon_type = str(file_lines[7])
            self.gun = file_lines[8]
        #print self.gun,self.health,self.damage,self.firerate,self.ammo,self.range,self.accuracy,self.weapon_type
        
            

class Bullets(object):
    def __init__(self,velocity,bimage,life):
        self.velocity = velocity
        self.bimage = bimage
        self.life = life
        
        

class Player(object):
    def __init__(self,coords,velocity,ammo,health,image,dmg,mag):
        self.coords = coords
        self.velocity = velocity
        self.ammo = ammo
        self.health = health
        self.image = image
        self.dmg = dmg
        self.mag = mag
    

    
    def player_loop(self):
        
       self.velocity[1] += environment.gravity
       
       if ground.colliding() == True:
           environment.gravity = 0
           if environment.jumping == False:
               self.velocity[1] = 0
           
       else:
           environment.gravity = .5
           environment.jumping = False
            
       if player.velocity[1] >= 2:
           player.velocity[1] = 2
      
       
       if self.health > 0:
           self.alive = True
           
       elif self.health <= 0:
           self.alive=False
           self.health = 0
       
       
      
      
      
      
      
       
       
       ### Update crosshair
       try:
           canvas.delete(self.crosshair)
           canvas.delete(self.health_bar_outline)
           canvas.delete(self.health_bar)
           canvas.delete(self.gun_image)
          
           
       except AttributeError:
           pass
           
           
       
       ### update mouse coordinates
       self.mx,self.my = canvas.winfo_pointerxy()
       self.mx, self.my = [self.mx-10,self.my-60]
       
       
       ### update mouse coordinates
      
       
       
       
       
       def crosshair_update():
           x2 = (self.mx - self.coords[0]) ** 2
           y2 = (self.my - self.coords[1]) ** 2
           
           xy2 = x2 + y2
           
           global distance
           distance = math.sqrt(xy2)
           
           if self.alive == False:
               self.crosshair = canvas.create_image(self.mx,self.my,image=death_message)
           elif self.alive == True and self.ammo <= 0 and self.mag <= 0:
               self.crosshair = canvas.create_image(self.mx,self.my,image=out_of_ammo)
           elif self.alive == True and self.mag == 0 and self.ammo > 0:
               self.crosshair = canvas.create_image(self.mx,self.my,image=reload_image)
           elif self.alive == True and int(distance) <= int(my_loadout.range) and self.mag > 0:
               self.crosshair = canvas.create_image(self.mx,self.my,image=in_range_crosshair)
           elif self.alive == True and int(distance) > int(my_loadout.range) and self.mag > 0:
               self.crosshair = canvas.create_image(self.mx,self.my,image=not_in_range_crosshair)
        
         
       crosshair_update()
       
       ###display gun
       self.coords = canvas.coords(self.the_player)
       self.gun_image = canvas.create_image(self.coords[0]+50,self.coords[1],image=gun_lookup[my_loadout.gun])
       
       ###display gun
       
     
           
       
      
       if self.velocity[0] > 0:
           self.velocity[0] -= .1
       elif self.velocity[0] < 0:
           self.velocity[0] += .1
           
       if self.velocity[1] > 0:
           self.velocity[1] -= .1
       elif self.velocity[1] < 0:
           self.velocity[1] += .1
               
       
           
       
       
       
       
      
      
      
       if self.coords[0] >= 1366 or self.coords[0] <= 0:
           self.velocity[0] *= -1
       if self.coords[1] >= 650 or self.coords[1] <= 0:
           self.velocity[1] *= -1
           
      
     
       my_bbox = canvas.bbox(self.the_player)
       the_overlap = canvas.find_overlapping(*my_bbox)
       
       print self.velocity
       
       
       for collision in the_overlap:
           global move
           if 'player_collide' in canvas.gettags(collision):
               dx = abs(canvas.coords(self.the_player)[0] - canvas.coords(collision)[0]  )
               dy = abs(canvas.coords(self.the_player)[1] - canvas.coords(collision)[1]  )
               #finds the distance between y's and distnace between x's
           
               
               
               if dy < dx:
                   #side hit
                   canvas.move(self.the_player,-self.velocity[0],-self.velocity[1])
                   self.velocity[0] *= -1 
               elif dy > dx and self.velocity[1] < 0:
                   canvas.move(self.the_player,-self.velocity[0],-self.velocity[1])
                   self.velocity[1] *= -.5
               
                   
           
           
        
           
   
          
          
           
               
                   
                   
          
               
           #if the distance between y's is less than the distance between x's, it was a side hit
               
           
           
            
               
               
       self.health_bar_outline = canvas.create_rectangle(self.coords[0]-50,self.coords[1]-50,self.coords[0]-50+my_loadout.health,self.coords[1]-70)
       self.health_bar = canvas.create_rectangle(self.coords[0]-50,self.coords[1]-50,self.coords[0]-50+self.health,self.coords[1]-70,fill='green')
       
       if len(bullet_list) >= 1000:
           canvas.delete(bullet_list[0].bimage)
           bullet_list.remove(bullet_list[0])
           
       
       
       
       canvas.move(self.the_player,self.velocity[0],self.velocity[1])
       root.after(10,self.player_loop)
    def fire(self):
        global firing
        global bullet_list
        global devmode
        
        
        
        mouseX,mouseY = canvas.winfo_pointerxy()
        mouse_location = [mouseX-6,mouseY-50]
        
        #gets mouse location^
        
        mouse_vector = [mouse_location[0] - self.coords[0],mouse_location[1] - self.coords[1]]
        
        #gets the vector between mouse and player^
        
        m1 = mouse_vector[0] ** 2
        m2 = mouse_vector[1] ** 2
        mouse_mag = math.sqrt(m1 + m2)
        
        #gets magnitude with pythagorean theorem
        
        norm = [mouse_vector[0] / mouse_mag,mouse_vector[1] / mouse_mag]
        #normalizes the vector
        
        
        norm[0] *= 10
        norm[1] *= 10
        
        #scales the vector to something more manageable
        
        
        

        if firing == True and self.mag > 0 and self.alive == True:
            
            #gcoords = canvas.coords(self.gun_image)
            
            acc = random.randint(-my_loadout.accuracy,my_loadout.accuracy)
            acc *= .01
            
            bullet_obj = Bullets(velocity = [norm[0],norm[1]+acc],bimage=canvas.create_image(*self.coords,image=bullet_sprite,tags=('bullet','%s' % self.dmg)),life=0)
            bullet_list.append(bullet_obj)
            self.mag -= 1
            
            #play = subprocess.call(["afplay", gunshot_file])
            ###^^^ currently lags the game an insane amount^^^
            
            
        
        
        
        root.after(my_loadout.firerate,self.fire)
        
        
        
        
        
    def make(self):
        self.the_player = canvas.create_image(*self.coords,image=self.image)
        self.points = 0
       


    def fire_loop(self):
        
        
       
        
        
        try:
            for bullet in bullet_list:
                bul_coords = canvas.coords(bullet.bimage)
                
                
                canvas.move(bullet.bimage,bullet.velocity[0],bullet.velocity[1])
                
                a2 = (canvas.coords(bullet.bimage)[0] - self.coords[0]) ** 2
                b2 = (canvas.coords(bullet.bimage)[1] - self.coords[1]) ** 2 
                
                c2 = a2 + b2
                
                c = math.sqrt(c2)

                
                if c >= my_loadout.range:
                    canvas.delete(bullet.bimage)
                    bullet_list.remove(bullet)

            
            
                bullet_bbox = canvas.bbox(bullet.bimage)
                
                
                
                if type(bullet_bbox) != NoneType:
                    
                    bullet_overlapping = canvas.find_overlapping(*bullet_bbox)
            
            
                    for i in bullet_overlapping:
                        if 'collide' in canvas.gettags(i) and bullet in bullet_list or 'player_collide' in canvas.gettags(i) and bullet in bullet_list:
                            canvas.delete(bullet.bimage)
                            bullet_list.remove(bullet)
                        
                    
               
                
                
                
        except AttributeError:
            pass
        root.after(1,self.fire_loop)








    def semi(self):
        mouseX,mouseY = canvas.winfo_pointerxy()
        mouse_location = [mouseX-6,mouseY-50]
        
        #gets mouse location^
        
        mouse_vector = [mouse_location[0] - self.coords[0],mouse_location[1] - self.coords[1]]
        
        #gets the vector between mouse and player^
        
        m1 = mouse_vector[0] ** 2
        m2 = mouse_vector[1] ** 2
        mouse_mag = math.sqrt(m1 + m2)
        
        #gets magnitude with pythagorean theorem
        
        norm = [mouse_vector[0] / mouse_mag,mouse_vector[1] / mouse_mag]
        #normalizes the vector
        
        
        norm[0] *= 10
        norm[1] *= 10
        
        #scales the normalized vector, change this to change bullet speed
        
        
        

        if self.mag > 0  and self.alive == True and my_loadout.weapon_type  != 'Shotgun \n':
            
            #gcoords = canvas.coords(self.gun_image)
            
            acc = random.randint(-my_loadout.accuracy,my_loadout.accuracy)
            acc *= .01
            
            bullet_obj = Bullets(velocity = [norm[0],norm[1]+acc],bimage=canvas.create_image(*self.coords,image=bullet_sprite,tags=('bullet','%s' % self.dmg)),life=0)
            bullet_list.append(bullet_obj)
            self.mag -= 1
            
            #play = subprocess.call(["afplay", gunshot_file])
            ###^^^ currently lags the game an insane amount^^^
        elif my_loadout.weapon_type == 'Shotgun \n' and self.alive == True and self.mag > 0:
            #gcoords = canvas.coords(self.gun_image)
            
            
            left_theta = deg2rad(my_loadout.accuracy)
            right_theta = deg2rad(-my_loadout.accuracy)
            
            left_cos = math.cos(left_theta)
            left_sin = math.sin(left_theta)
            
            right_cos = math.cos(right_theta)
            right_sin = math.sin(right_theta)
            
            
            
            left_x = norm[0] * left_cos - norm[1] * left_sin
            left_y = norm[0] * left_sin + norm[1] * left_cos            
            
            right_x = norm[0] * right_cos - norm[1] * right_sin
            right_y = norm[0] * right_sin + norm[1] * right_cos
            
            
            
            
            
            
            bullet_obj = Bullets(velocity = [left_x,left_y],bimage=canvas.create_image(*self.coords,image=bullet_sprite,tags=('bullet','%s' % self.dmg)),life=0)
            bullet_list.append(bullet_obj)
            
            bullet_obj = Bullets(velocity = [norm[0],norm[1]],bimage=canvas.create_image(*self.coords,image=bullet_sprite,tags=('bullet','%s' % self.dmg)),life=0)
            bullet_list.append(bullet_obj)
            
            bullet_obj = Bullets(velocity = [right_x,right_y],bimage=canvas.create_image(*self.coords,image=bullet_sprite,tags=('bullet','%s' % self.dmg)),life=0)
            bullet_list.append(bullet_obj)
            
            
            self.mag -= 1
            
            #play = subprocess.call(["afplay", gunshot_file])
            ###^^^ currently lags the game an insane amount^^^
            
            
        
        
        
    


        
        



my_loadout = Loadout()
my_loadout.class_determine()

player = Player(coords=[400,100],velocity=[0,0],ammo=int(my_loadout.ammo),health=int(my_loadout.health),dmg=int(my_loadout.damage),image=player_sprite,mag=my_loadout.mag_cap)
player.make()
player.player_loop()
player.fire()
player.fire_loop()



text = Text(root)
text.config(width=15,height=8)
text.config(bg='grey')

def text_loop():
    text.config(state=NORMAL)
    text.delete(1.0,END)
    text.insert(INSERT,"Health: %s \n" % player.health)
    text.insert(INSERT,"Total Ammo: %s\n" % player.ammo)
    text.insert(INSERT,"Magazine: %s \n" % player.mag)
    text.insert(INSERT,"Score: %s " % player.points)

    
    text.config(state=DISABLED)
    root.after(1,text_loop)

text.place(x=1255,y=0)
text_loop()

### mapping keys 

def settrue(event):
    if my_loadout.weapon_type == 'Assualt Rifle \n' or my_loadout.weapon_type == 'Submachine Gun \n' or my_loadout.weapon_type == 'LMG \n':
        global firing
        firing = True
    else:
        player.semi()
        
def setfalse(event):
    global firing
    firing = False


root.bind('<ButtonPress-1>', settrue)
root.bind('<ButtonRelease-1>', setfalse)




    
def jump(event):
    global move
    print "trying!"
    if player.alive == True and environment.gravity == 0:
        environment.jumping = True
        canvas.move(player.the_player,0,-5)
        player.velocity[1] = -12
def move_right(event):
    global move
    
    if player.alive == True:
        player.velocity[0] += 3
def move_left(event):
    global move
    
    if player.alive == True:
        player.velocity[0] -= 3


    
    


def _reload_(event):
    if player.mag == 0 and player.ammo >= my_loadout.mag_cap:
        player.ammo -= my_loadout.mag_cap
        player.mag = my_loadout.mag_cap
        
    elif player.ammo > 0:
        ammo_to_give = my_loadout.mag_cap - player.mag
        if ammo_to_give <= player.ammo:
            player.mag += ammo_to_give
            player.ammo -= ammo_to_give
        else:
            player.mag += player.ammo
            player.ammo = 0
    
        
    


root.bind('<d>',move_right)
root.bind('<a>',move_left)
root.bind('<w>',jump)
root.bind('<r>',_reload_)

### mapping keys






#### close up application
canvas.pack()
root.mainloop()