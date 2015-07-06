###import dependencies
import os
import subprocess
from Tkinter import *


### game window should be 1366 x 650


### setting up window for home screen
main = Tk()
main.geometry("900x500+200+0")
main.title("The Game...")
### ^^^ 




explosion = PhotoImage(file='explosion.gif')
my_label= Label(main,image=explosion)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

global gun_dictionary
global class_made
class_made = False

gun_dictionary = {
    
    #Damage, Firerate, Ammo Capacity,range in px,mag cap,accuracy(smaller number is more accurate)
    
    #A firerate of 100 is about 600 rpm (slightly slower)
    
    "ACR":[20,70,90,400,30,5],
    "M16":[1,200,90,450,30,3],
    "SCAR":[1,150,90,700,30,2],
    "AK74":[1,200,90,400,30,7],
    "L85":[100,60,90,600,30,0],
    
    
    "Bizon":[1,60,192,300,64,14],
    "Vector":[1,70,96,300,32,9],
    "UMP":[1,70,96,300,32,15],
    "Uzi":[1,30,96,300,32,30],
    "AK74U":[1,80,96,300,30,12],
    
    
    "MK14":[1,1,45,300,15,2],
    "SKS":[40,1,45,300,15,3],
    "AR10":[1,1,60,300,20,1],
    "G3":[1,1,60,300,20,2],
    "HK417":[1,1,60,900,20,1],
    
    
    "RPD":[20,100,200,600,100,15],
    "M60":[20,50,200,600,100,30],
    "M249":[20,120,200,600,100,20],
    "M27":[20,30,200,600,100,10],
    "MG36":[20,50,200,600,100,13],
    
    
    "M1014":[1,200,18,200,6,9],
    "Spas-12":[1,200,18,200,6,11],
    "DBV-12":[1,120,24,200,8,7],
    "Mossberg 590":[1,400,18,200,6,5],
    "Double Barrel":[1,300,12,200,2,4],
    
    
    #LONGEST possible in-game shot is ~1500 pixels
    
    "Barret M82":[1,300,30,1000,10,1],
    "ScoutElite":[1,600,15,900,5,1],
    "M98":[1,600,15,1550,5,1],
    "SVD":[1,400,45,800,15,1],
    "L96":[1,600,15,1400,5,1]
    
    
}

def start():
    main.destroy()
    
    os.system('python Big_Game.py')
    

        
def make_class():
    selection = Toplevel()
    selection.title("Create a Class")
    selection.geometry("600x400+350+0")
    selection.bind("<Button-1>",button_click)
    
    
    def choose_weapon():
        type_var = weapon_type.get()
        
        class Player_Class(object):
            def __init__(self,gun,health_plus,damage_plus):
                self.gun = gun
                self.health_plus = health_plus
                self.damage_plus = damage_plus
                
        
        
       
        my_class = Player_Class(gun="",health_plus=0,damage_plus=0)
       
       
        if type_var == 'Assualt Rifle':
            gun_menu = Menubutton(selection,text="Choose a Weapon")
            gun_menu.pack()
        
            gun_menu.menu = Menu(gun_menu,tearoff=0)
            gun_menu['menu'] = gun_menu.menu
            
            gun_menu.menu.add_command(label="ACR",command=lambda: gun_menu.config(text="ACR"))
            gun_menu.menu.add_command(label="M16",command=lambda: gun_menu.config(text="M16"))
            gun_menu.menu.add_command(label="AK74",command=lambda: gun_menu.config(text="AK74"))
            gun_menu.menu.add_command(label="SCAR-H",command=lambda: gun_menu.config(text="SCAR"))
            gun_menu.menu.add_command(label="L85",command=lambda: gun_menu.config(text="L85"))
            
        elif type_var == 'Submachine Gun':
            gun_menu = Menubutton(selection,text="Choose a Weapon")
            gun_menu.pack()
        
            gun_menu.menu = Menu(gun_menu,tearoff=0)
            gun_menu['menu'] = gun_menu.menu
            
            gun_menu.menu.add_command(label="AK74U",command=lambda: gun_menu.config(text="AK74U"))
            gun_menu.menu.add_command(label="Bizon",command=lambda: gun_menu.config(text="Bizon"))
            gun_menu.menu.add_command(label="Vector",command=lambda: gun_menu.config(text="Vector"))
            gun_menu.menu.add_command(label="UMP",command=lambda: gun_menu.config(text="UMP"))
            gun_menu.menu.add_command(label="Uzi",command=lambda: gun_menu.config(text="Uzi"))
        elif type_var == 'DMR':
            gun_menu = Menubutton(selection,text="Choose a Weapon")
            gun_menu.pack()
        
            gun_menu.menu = Menu(gun_menu,tearoff=0)
            gun_menu['menu'] = gun_menu.menu
            
            gun_menu.menu.add_command(label="MK14",command=lambda: gun_menu.config(text="MK14"))
            gun_menu.menu.add_command(label="SKS",command=lambda: gun_menu.config(text="SKS"))
            gun_menu.menu.add_command(label="AR10",command=lambda: gun_menu.config(text="AR10"))
            gun_menu.menu.add_command(label="G3",command=lambda: gun_menu.config(text="G3"))
            gun_menu.menu.add_command(label="HK417",command=lambda: gun_menu.config(text="HK417"))
        elif type_var == 'LMG':
            gun_menu = Menubutton(selection,text="Choose a Weapon")
            gun_menu.pack()
        
            gun_menu.menu = Menu(gun_menu,tearoff=0)
            gun_menu['menu'] = gun_menu.menu
            
            gun_menu.menu.add_command(label="RPD",command=lambda: gun_menu.config(text="RPD"))
            gun_menu.menu.add_command(label="M60",command=lambda: gun_menu.config(text="M60"))
            gun_menu.menu.add_command(label="M249",command=lambda: gun_menu.config(text="M249"))
            gun_menu.menu.add_command(label="M27",command=lambda: gun_menu.config(text="M27"))
            gun_menu.menu.add_command(label="MG36",command=lambda: gun_menu.config(text="MG36"))
        elif type_var == 'Shotgun':
            gun_menu = Menubutton(selection,text="Choose a Weapon")
            gun_menu.pack()
        
            gun_menu.menu = Menu(gun_menu,tearoff=0)
            gun_menu['menu'] = gun_menu.menu
            
            gun_menu.menu.add_command(label="M1014",command=lambda: gun_menu.config(text="M1014"))
            gun_menu.menu.add_command(label="Spas-12",command=lambda: gun_menu.config(text="Spas-12"))
            gun_menu.menu.add_command(label="DBV-12",command=lambda: gun_menu.config(text="DBV-12"))
            gun_menu.menu.add_command(label="Mossberg 590",command=lambda: gun_menu.config(text="Mossberg 590"))
            gun_menu.menu.add_command(label="Double Barrel",command=lambda: gun_menu.config(text="Double Barrel"))
        elif type_var == 'Sniper Rifle':
            gun_menu = Menubutton(selection,text="Choose a Weapon")
            gun_menu.pack()
        
            gun_menu.menu = Menu(gun_menu,tearoff=0)
            gun_menu['menu'] = gun_menu.menu
            
            
            
            gun_menu.menu.add_command(label="Barret M82",command=lambda: gun_menu.config(text="Barret M82"))
            gun_menu.menu.add_command(label="Scout Elite",command=lambda: gun_menu.config(text="ScoutElite"))
            gun_menu.menu.add_command(label="M98",command=lambda: gun_menu.config(text="M98"))
            gun_menu.menu.add_command(label="Dragunov SVD",command=lambda: gun_menu.config(text="SVD"))
            gun_menu.menu.add_command(label="L96",command=lambda: gun_menu.config(text="L96"))
        
        
    
   
        def check():
            if gun_menu["text"] != "Choose a Weapon":
                gun_menu.update()
                gun_menu.config(state=DISABLED)
                gun_menu.update()
                
                
                explanation = Label(selection,text=""" You now have 20 points to allocate to health and ammo reserve \n The following box is where you may enter your desired health boost \n Your ammo boost will be calculated automatically based on your health boost \n for example, allocation 10 points to health, 10 points will automatically be allocated to ammo""")
                explanation.pack()
                
                def player_read():
                    explanation.destroy()
                    read_it_button.destroy()
                    gun_menu.config(state=DISABLED)
                    
                    b = IntVar()
                    health_boost_entry = Entry(selection,textvariable=b)
                    health_boost_entry.pack()
                    
                    b.set(0)
                    def done():
                        global class_made
                        a = b.get()
                        if a <= 20:
                            health_boost_entry.config(state=DISABLED)
                            confirm_button.config(text="Health Chosen")
                            confirm_button.config(state=DISABLED)
                            health_boost_entry.update()
                            confirm_button.update()
                            
                            with open('class.txt','w') as custom_class:
                                
                                #Gun, health, total damage,firerate, total ammo
                                custom_class.write('%s \n'% (a+100) )# writes the players total health
                                custom_class.write('%s \n'% ( gun_dictionary[gun_menu["text"]][0] )) # writes the players damage
                                custom_class.write('%s \n'% ( gun_dictionary[gun_menu["text"]][1] )) #writes the players firerate
                                custom_class.write('%s \n'% ( gun_dictionary[gun_menu["text"]][2] + abs(a-20) )) # writes the ammo storage
                                custom_class.write('%s \n'% ( gun_dictionary[gun_menu["text"]][3] )) # writes the range
                                custom_class.write('%s \n'% ( gun_dictionary[gun_menu["text"]][4] )) # writes the mag capacity
                                custom_class.write('%s \n'% ( gun_dictionary[gun_menu["text"]][5] )) # writes the accuracy
                                custom_class.write('%s \n'% (type_var)) # writes the weapon type
                                custom_class.write('%s'% (gun_menu["text"]) ) # writes the gun name
                                
                                
                                
                            class_made = True
                            
                            
                            finished = Label(selection,text="Your class has been created, your weapon is the %s %s,\n your ammo boost is %s,\n and your total health is %s" % (gun_menu["text"],type_var,abs(a-20),a+100) )
                            finished.pack()
                            
                            finished_close = Button(selection,text="Close Window",command=selection.destroy)
                            finished_close.pack()
        
                            
                        
                        
                    
                    
                   
                   
                    confirm_button = Button(selection,text="Confirm?",command=done)
                    confirm_button.pack()
                    confirm_button.update()
                    
                
                read_it_button = Button(selection,text="Continue",command= player_read)
                read_it_button.pack()
                read_it_button.update()
                
            else:
                selection.after(10,check)
        check()
                
   
   
   
    def confirm_class():
        type_label.config(text="You have chosen your class.")
        type_label.config(state=DISABLED)
        weapon_type.config(state=DISABLED)
        confirm_button.config(text="Class Chosen",state=DISABLED)
        
        
        choose_weapon()
    
    weapon_type = Spinbox(selection,values=("Assualt Rifle","Submachine Gun","DMR","LMG","Shotgun","Sniper Rifle"),invalidcommand=button_click)
    type_label = Label(selection,text="Choose a weapon class using the up and down arrows.")
    confirm_button = Button(selection,text="Confirm?",command=confirm_class)
    
    type_label.pack()
    weapon_type.pack()
    confirm_button.pack()
    

    
def about():
    about_window = Toplevel()
    about_window.title("About the Game")
    about_window.geometry("600x500+350+100")
    
    aboutlabel = Label(about_window,text=""" 

    HOW TO PLAY:\n
    
    In the upper right is your HUD, it includes health, score, health, and your ammo, \n
    Kill enemies to gain points,\n
    Move with WASD, shoot with the left arrow, reload with R, \n
    Aim with the cursor, you can only fire if the cursor is in range of your weapon, for ease of shooting, \n
    If your cursor is in range of your weapon, it will be red, if not it will be black \n
    Enjoy The Game...! \n
    
    \n
    Created by Evan Berg and Adrian Cisneros \n 
    Developed by Adrian Cisneros
     \n Artwork by Evan Berg""")
    
    
    
    aboutlabel.pack()
    
    close_button_about = Button(text="Close",command=about_window.destroy)
    
    




def button_click(event):
    audio_file = "/Users/cisnerosa/documents/Big_2D_Project/Click_Noise.mp3"
    play = subprocess.call(["afplay", audio_file])
    
    
    

startbutton = Button(text="Start",command=start)
class_button = Button(text="Create Class",command=make_class)
about_button = Button(text="About The Game...",command=about)
main.bind("<Button-1>",button_click)

def access():
    if class_made == False:
        startbutton.config(state=DISABLED)
        startbutton.update()
        main.after(100,access)
        
    else:
        startbutton.config(state=NORMAL)
        startbutton.update()
    
        
access()



startbutton.pack(pady=50,fill='x')
class_button.pack(pady=50,fill='x')
about_button.pack(pady=50,fill='x')






### End of main window
main.mainloop()
### Don't write past here