#Game
import time
import sys
import random
#intro
text_speed = 0.03 #change to 0 for testing, use 0.04 for playing
tRed =  '\033[91m' # Red Text
tGreen = '\033[32m' # Green Text
tGold = '\033[93m' # Gold Text
tCyan = '\033[96m' # Cyan Text
default_font = '\033[m' # reset to the defaults
Bold = '\033[1m' # make text bold

character_health = 100
strength = random.choice([30,35,40,45,50])
#All the important custom functions

def textslow(text1='',text2 ='',text3='',text4='',text5='',text6='',text7='',text8='',text9='',text10='',text11='',text12=''): #many parameters for compact code
    '''
    Prints character by character (retro style)
    '''
    text = text1 + text2 + text3 + text4 + text5 + text6 + text7 + text8 + text9 + text10 + text11 + text12
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(text_speed)

def showStats(): #stats function
    textslow('\n\nHere are you current stats:\n')
    print(tGold + '\n-------------------', tRed + '\n Strength: ' , strength , tGreen + '\n Health: ', character_health, tGold + '\n-------------------\n\n\n' + default_font)

def drumroll():
    for i in range(3):
        for char in '. ':
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.25)

def witch(): #THIS FUNCTION IS FOR THE WITCH
    global character_health, strength
    textslow('A witch just apeared in the middle of nowhere,\nAnd they will give you a random potion\nOne of the three potions that the witch will give you is | strength | health | or weakness |\nDrum roll please ')
    drumroll()
    random_potion = random.randint(1,3)
    if random_potion == 1: #Strength
        textslow('\n\nYou got 5 strength from the witch!')
        strength += 5
    elif random_potion == 2: #Health
        textslow('\n\nYou got 10 health from the witch!')
        character_health += 10
    else: #negative effects
        textslow('\n\nYou got a weakness potion that dealt 5 strength and 5 health!')
        character_health -= 5; strength -= 5
    showStats()

def mathprob(): ### THIS IS THE MATH PROBLEM
    global strength
    def inputNumber(message): #THIS IS ERROR CORRECTION FOR FOOL PROOF
        while True:
            try:
                userInput = int(input(message))
            except ValueError:
                print('\nPlease try again\n')
                continue
            else:
                return userInput 
                break
    num1 = random.randint(1,100); num2 = random.randint(1,100); num_ans = num1 + num2 #random number with its answer
    textslow('\nAdd these 2 numbers\n', str(num1), '\n+\n',str(num2),'\n\n')
    num_input = inputNumber('Enter sum here: ')
    if num_input == num_ans: #if answer is correct
        strength += 5
        textslow('\nYou are correct!\nYou will get 5 strength as a reward!')
        showStats()
    else: #if answer is wrong
        textslow('You are incorrect,\nbut as a little tip, you could improve your math skills.\n ')

def randomHouse(): #THIS FUNCTION IS FOR RANDOM HOUSE PLACE
    global character_health, strength
    textslow('You just found a random house!\nYou will now find a random potion that you will have to drink and make a decision about it\n\nLet\'s find out what colour is the potion '); drumroll()
    potion_colour = random.choice(['Red','Blue','Green','Purple','Yellow','Black'])
    textslow('\n\nThe colour is ', potion_colour)
    while True:
        textslow('\n\nWould you like to drink the random potion? (Y|N): ')
        yes = input().lower()
        if yes == 'y': #If its yes
            textslow('\nYou decided to drink the potion. Let\'s see what the effects are.\n')
            potion = random.choice(['h','s','d'])
            if potion == 'h': #health potion
                textslow('It was a health potion and you got 15 health for it\nCongrats.\n'); character_health += 15
            elif potion == 's': #strength potion
                textslow('It was a strength potion and you got 15 strength\nLucky person!\n'); strength += 15
            else: #damage potion
                textslow('Unfortunately you got a damage potion and your health has been reduced by 20\n'); character_health -= 20
            break
        elif yes =='n': #If its no
            textslow('You decided to skip the house, that means that you will not get anything.\n')
            break
    showStats()

start_health = 60; end_health = 190; enemy_damage = 20  #this is for the monster/final

def enemy():### THIS FUNCTION IS FOR THE ENEMY
    global character_health, strength, start_health, end_health, enemy_damage, monster_health
    monster_health = random.randint(start_health,end_health)
    monster_name = random.choice(['Rob', 'Rick', 'Bob', 'Michael', 'Boomer','Zoomer', 'Epic Games','Kirill', 'Eric', 'Shon','Chris','Jimmy','Thomas','Cray','Rose','Life good','Simon','Rusu','Daniel','Evan','Fridman','Max','John','Ryan','Trisha','Rachel','Armen','Liam','Noah','Lucas'])
    textslow('You have to fight an enemy because you chose the wrong path\nYou will have to use your strength to kill them\n\nThe name of the monster is: ', monster_name, '\nIf you win the battle, you will get a bit of strength and health as a reward\n\nUse your skills very wisely to not lose health because you will have to fight the final boss later.\nIf you die right now, then you will not be able to continue!\n\nThe monster has ', str(monster_health) , ' health, and deals ', str(enemy_damage), ' damage\nYou have ', str(character_health), ' health and you deal ', str(strength), ' damage')
    enemyBrain('enemy')
    if character_health > 0:
        showStats()
        start_health += 25; end_health += 25; enemy_damage += 10        

def enemyBrain(enemyORfinal = ''): # ENEMY BRAIN
    '''
    There are 2 types of enemy brains. One of them is for the enemies you verse throughout the game, and there is the final boss which has similar code to the enemy but is slightly altered. Which is distiguished with the parameter in the function.
    '''
    global character_health, strength, enemy_damage, monster_health, movement_counter
    if enemyORfinal == 'final':
        enemy_damage = 50
    random_strength = random.randint(5,10)
    while character_health > 0:
        action = input('\n\nUse Q to defend and E to attack: ').lower()
        if action == 'q': #Defend
            textslow('\nYou chose to defend,\n')
            monster_action = random.randint(1,2) # 50/50 chance of the action of the monster
            if monster_action == 1:
                textslow('The monster also chose to defend\n\nIn the end, nothing happened\n')
            elif monster_action == 2:
                character_health -= 10; monster_health -= 10
                textslow('The monster chose to attack, they only did 10 health of damage through your shield\nYou also ended up doing 10 damage to the monster because you caught him off guard\n')
                if monster_health > 0:
                    textslow('\n\nThe monster still has ', str(monster_health) ,' health left\nYou have ', str(character_health), ' health left\nKeep on trying\n')
                if enemyORfinal == 'enemy':
                    if monster_health <= 0: #If the monster dies
                        character_health += 50; strength += random_strength
                        textslow('\nGood job, you killed the monster!\nYou may continue on your journey\nYou will now get a random amount of strength from the monster and 50 health\nYou will get ' + Bold , str(random_strength) , default_font + ' strength!')
                        break
                elif enemyORfinal == 'final':
                    if monster_health <= 0: #If the monster dies
                        textslow('Good job, you killed the final boss!\n')  
                        break
            textslow('\nKeep on trying\n')                           
        elif action == 'e': #if action is e (attacking)
            monster_health -= strength
            textslow('\nYou chose to attack the monster.\nYou dealt ', str(strength), ' damage to the monster\n')
            monster_action = random.randint(1,2) #50/50 chance of luck
            if enemyORfinal == 'enemy':
                if monster_health <= 0: #If the monster dies
                    character_health += 50; strength += random_strength
                    textslow('\nGood job, you killed the monster!\nYou may continue on your journey\n\nYou will now get a random amount of strength from the monster and 50 health\nYou will get ' + Bold , str(random_strength) , default_font + ' strength!')
                    break
            elif enemyORfinal == 'final':
                if monster_health <= 0: #If the monster dies
                    textslow('Good job, you killed the final boss!\n')
                    break
            if monster_action == 1:
                textslow('The monster just watched you fight them\nHe was just lazy\n\nThe monster still has ', str(monster_health) ,' health left\nYou have ', str(character_health), ' health left\nKeep on trying\n')
            else: #If monster_action == 2:
                character_health -= enemy_damage
                textslow('The monster didn\'t like what you did so he also decided to attack you aswell. He did ', str(enemy_damage), ' health of damage to you.\n\nThe monster still has ', str(monster_health) ,' health left\nYou have ', str(character_health), ' health left\nKeep on trying\n')
    if character_health <= 0:
        movement_counter += 100
        textslow('\033[91m\033[1m\n\n\nUnfortunately you died. :(\nThat is game over for you.\n\n\n\033[96mThank you for playing Warrior!\n\n')

#part of map() function, there is no point for this to be repeated
xfactor = tRed + Bold + 'X' + default_font + tGold; checkmark = Bold + tCyan + '✓' + default_font + tGold; tiles = []
for i in range(121):
    tiles.append('?')
tiles[60] = xfactor

def map():
    global text_speed
    original_speed = text_speed; text_speed = 0.02; count = 0
    textslow('\nHere is the map that shows all the locations you have been too\n\n')
    for i in tiles:
        if tiles[count] == xfactor:
            tiles[count] = checkmark
        count += 1
    coord = 121-11*(y)+x
    tiles[coord-1] = xfactor; xstart = 0; ystart = 11   
    colom1 = '|     |     |     |     |     |     |     |     |     |     |     |'
    colom2 = '|_ _ _|_ _ _|_ _ _|_ _ _|_ _ _|_ _ _|_ _ _|_ _ _|_ _ _|_ _ _|_ _ _|\n|     |     |     |     |     |     |     |     |     |     |     |'
    print(tGold + ' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n|     |     |     |     |     |     |     |     |     |     |     |')
    for i in range(10):
        print('|  ',end='')
        print(*tiles[xstart:ystart], sep = '  |  ', end='  |\n'  )
        print(colom2)
        xstart += 11; ystart += 11
    print('|  ',end='')
    print(*tiles[110:121], sep = '  |  ', end='  |\n'  )  #11th row
    print('|_ _ _|_ _ _|_ _ _|_ _ _|_ _ _|_ _ _|_ _ _|_ _ _|_ _ _|_ _ _|_ _ _|\n')
    textslow(default_font + 'Your current location is marked with: ', xfactor + default_font)
    textslow('\nPrevious locations have been marked with: ', checkmark + default_font, '\n\n')
    text_speed = original_speed

##############################################################################
############################      START      #################################
##############################################################################

textslow('Welcome to Warrior \nThe game where you will have to survive and kill different enemies to get a trophy in the end \nLet\'s jump right into the game!\n\nEnter your username:')
username = input(' ').capitalize() #ask user for name
textslow('\nHello ', username)
showStats() #introducing to the controls
textslow('To move around the game,\nYou will have to use WASD as a movement button\n\n| W being up | S being down | A being left | D being right | \n\nIf you would like to see where you are on the map and all the places you have visited, type "M" when asked for the movement input.\n\nBe AWARE of the enemies that might pop up in your adventure!\n\nThese are some suggestions about the game from the developer:\nThis is a 11x11 adventure game, try not to go back to the position you were previously and do not go to the corners first because there might be a surprise.\n\nGood Luck and Have Fun!\n\n')
                #############################################
                ############# Coordinate system #############
                #############################################

x = 6; y = 6 # this is the middle of the map
movement_counter = 0; movement_max = 30 #just to count moves and to make it so that the game will end sonner or later

while movement_max > movement_counter: #The part where its all the brains
    if character_health <= 0:
        break #ends the whole while loop
    else:
        if x == 1: #left part of the map
            while True: 
                movement = input('\n\nUse |W|S|D| to move or |M| for map: ').lower() #should i put |M| for map?
                if movement == 'w':
                    y += 1; print(x,y); movement_counter += 1
                    break
                elif movement == 's':
                    y -= 1; print(x,y); movement_counter += 1
                    break
                elif movement == 'd':
                    x += 1; print(x,y); movement_counter += 1
                    break
                elif movement == 'm':
                    map()
        elif x == 11: # right side of the map
            while True:
                movement = input('\n\nUse |W|A|S| to move or |M| for map: ').lower()
                if movement == 'w':
                    y += 1; print(x,y); movement_counter += 1
                    break
                elif movement == 'a': 
                    x -= 1; print(x,y); movement_counter += 1
                    break
                elif movement == 's':
                    y -= 1; print(x,y); movement_counter += 1
                    break
                elif movement == 'm':
                    map()
        elif y == 1: #bottom part of the map
            while True:
                movement = input('\n\nUse |W|A|D| to move or |M| for map: ').lower()
                if movement == 'w':
                    y += 1; print(x,y); movement_counter += 1
                    break
                elif movement == 'a':
                    x -= 1; print(x,y); movement_counter += 1
                    break
                elif movement == 'd':
                    x += 1; print(x,y); movement_counter += 1
                    break               
                elif movement == 'm':
                    map()
        elif y == 11:#top part of the map
            while True:
                movement = input('\n\nUse |A|S|D| to move or |M| for map: ').lower()
                if movement == 'a':
                    x -= 1; print(x,y); movement_counter += 1
                    break
                elif movement == 's':
                    y -= 1; print(x,y); movement_counter += 1
                    break
                elif movement == 'd':
                    x += 1; print(x,y); movement_counter += 1
                    break
                elif movement == 'm':
                    map()
        else: # middle of the map
            while True:
                movement = input('\n\nUse |W|A|S|D| to move or |M| for map: ').lower()
                if movement == 'w':
                    y += 1; print(x,y); movement_counter += 1
                    break
                elif movement == 'a':
                    x -= 1; print(x,y); movement_counter += 1
                    break
                elif movement == 's':
                    y -= 1; print(x,y); movement_counter += 1
                    break
                elif movement == 'd':
                    x += 1; print(x,y); movement_counter += 1
                    break
                elif movement == 'm':
                    map()
        #################################        
        #  Determining the coordinates  #
        #################################
        if x == 7 and y == 6:#story
            textslow('I love the sound of beautiful birds chirping. It makes my life a little less depressing.\n\n')
        elif x == 6 and y == 7: #story
            textslow('Well, that\'s just great.\nMy shoes are now filled with sand!\n\n')
        elif x == 5 and y == 6:#story
            textslow('I found a cactus and a knife. Let\'s get some water.\n\n')
        elif x == 6 and y == 5:#story
            textslow('ARGH!\nWater everywhere!\n\n')
        elif x == 5 and y == 7:#witch
            witch()
        elif x == 5 and y == 5:#witch
            witch()
        elif x == 7 and y == 5:#witch
            witch()
        elif x == 7 and y == 7:#witch
            witch()
        elif x == 4 and y == 8:#story
            textslow('I\'m starting to see a lonely house beside a water geyser!!\n\n')
        elif x == 4 and y == 7:#story
            textslow('I\'m starting to see different villagers in the distance\nThis is so bad for my brain.\n\n')
        elif x == 4 and y == 6:#story
            textslow('Where are the monsters at?\n\n')
        elif x == 4 and y == 5:#story
            textslow('No sight of any animals right now,\n which means I wont die.\n\n')
        elif x == 4 and y == 4:#story
            textslow('BOOOOOOO!\nA ghost just passed by me! I should watch out next time!\n\n')
        elif x == 5 and y == 4: #enemy
            enemy()
        elif x == 6 and y == 4:#story
            textslow('Ya, probably shouldn\'t drink the water, it\'s really salty.\n\n')
        elif x == 7 and y == 4: #enemy
            enemy()
        elif x == 8 and y == 4:#story
            textslow('I am surrounded by killer sharks, going to die now. RIP\n\n')
        elif x == 8 and y == 5:#story
            textslow('Keep on swimming, keep on swimming.\n\n')
        elif x == 8 and y == 6:#story
            textslow('These are huge waves that I am in. It\'s like a tsunami!\n\n')
        elif x == 8 and y == 7:#story
            textslow('These are some interesting branches which I could make something out of them.\n\n')
        elif x == 8 and y == 8:#story
            textslow('This is such a beautiful scene. I wish I had a camera.\n\n')
        elif x == 7 and y == 8:#story
            textslow('I see a house in the distance.\n\n')
        elif x == 6 and y == 8:#witch
            witch()
        elif x == 5 and y == 8:#story
            textslow('Well, that\'s great,\nThere is a sand storm and I don\'t know what to do at the moment.\n\n')
        elif x == 3 and y == 9:#story
            textslow('My thirst is almost out. I NEED WATER!\n\n')
        elif x == 3 and y == 8:#Random House
            randomHouse()
        elif x == 3 and y == 7:#witch
            witch()
        elif x == 3 and y == 6:#story
            textslow('Oh my, QUICKSAND!\n I have to try and get out of this sand to not die\n'); time.sleep(0.75)
            textslow('Okay, I got out, that was pretty easy\n\n')
        elif x == 3 and y == 5:#enemy
            enemy()
        elif x == 3 and y == 4: #Math problem
            mathprob()
        elif x == 3 and y == 3:#witch
            witch()
        elif x == 4 and y == 3:#story
            textslow('BBB RRR!\n I am getting more hungry every second!\n\n')
        elif x == 5 and y == 3:#story
            strength += 5
            textslow('Some freshwater I can use\nYour strength has been increaed by 5\n\n')
        elif x == 6 and y == 3:#enemy
            enemy()
        elif x == 7 and y == 3:#story
            textslow('These are some pretty cool corals at the bottom!\n\n')
        elif x == 8 and y == 3:#enemy
            enemy()
        elif x == 9 and y == 3:#story
            textslow('ARGH! A jellyfish has been found, and I have to get out of here ASAP before I get stung!\n\n')
        elif x == 9 and y == 4:#Random House
            randomHouse()
        elif x == 9 and y == 5:#witch
            witch()
        elif x == 9 and y == 6:#Math problem
            mathprob()
        elif x == 9 and y == 7:#Random House
            randomHouse()
        elif x == 9 and y == 8:#enemy
            enemy()
        elif x == 9 and y == 9:#story
            textslow('No sign of humans anywhere, probably a bad thing...\n\n')
        elif x == 8 and y == 9:#witch
            witch()
        elif x == 7 and y == 9:#Random House
            randomHouse()
        elif x == 6 and y == 9:#enemy
            enemy()
        elif x == 5 and y == 9:#story
            textslow('It is boiling hot in this weather,\nIt\'s probably better in heaven.')
        elif x == 4 and y == 9:#enemy
            enemy()
        elif x == 2 and y == 10:#witch
            witch()
        elif x == 2 and y == 9:#story
            textslow('Oh my, there is a huge spide on my leg.\nLet\'s get him off me.\nThere we go.')
        elif x == 2 and y == 8:#witch
            witch()
        elif x == 2 and y == 7:#enemy
            enemy()
        elif x == 2 and y == 6:#Math problem
            mathprob()
        elif x == 2 and y == 5:#story
            textslow('What are these thick leaves? I can barely move in this forest!\n\n')
        elif x == 2 and y == 4:#witch
            witch()
        elif x == 2 and y == 3:#enemy
            enemy()
        elif x == 2 and y == 2:#Math problem
            mathprob()
        elif x == 3 and y == 2:#enemy
            enemy()
        elif x == 4 and y == 2:#Random House
            randomHouse()
        elif x == 5 and y == 2:#Math problem
            mathprob()
        elif x == 6 and y == 2:#story
            textslow('I just found a piece of wood floating, I will use that to regenerate my stamina.\n\n')
        elif x == 7 and y == 2:#witch
            witch()
        elif x == 8 and y == 2:#witch
            witch()
        elif x == 9 and y == 2:#Math problem
            mathprob()
        elif x == 10 and y == 2:#enemy
            enemy()
        elif x == 10 and y == 3:#witch
            witch()
        elif x == 10 and y == 4:#story
            textslow('I can see a HUGE whale right below me!\n\n')
        elif x == 10 and y == 5:#enemy
            enemy()        
        elif x == 10 and y == 6:#story
            textslow('That\'s a waterfall. FREE WATER!\n\n')        
        elif x == 10 and y == 7:#story
            textslow('Found some animals, time to kill them.\n\n')        
        elif x == 10 and y == 8:#witch
            witch()        
        elif x == 10 and y == 9:#story
            textslow('It feels like I\'ve been here for ages...\n\n')        
        elif x == 10 and y == 10:#witch
            witch()        
        elif x == 9 and y == 10 :#Math problem
            mathprob()        
        elif x == 8 and y == 10:#story
            textslow('This is a pretty cool flower, should I smell it?')
            while True:
                flower = input('\n\nYes or no?: ').lower()
                if flower == 'y' or flower == 'yes':
                    textslow('The flower gave you by accidently 5 strength. What luck!\n\n')
                    break
                elif flower == 'n' or flower == 'no':
                    textslow('The flower might have been dangerous, who knows...\n\n')
                    break
        elif x == 7 and y == 10:#story
            textslow('I just found an ancient ruin that holds warer, might come in handy.\n\n ')        
        elif x == 6 and y == 10:#story
            textslow('Great,\nThere are coyotes on my tail now.\nHopefully they will not hunt me down!\n\n')           
        elif x == 5 and y == 10:#enemy
            enemy()        
        elif x == 4 and y == 10:#story
            textslow('Is that a mirage?! A house just disappeared!\n\n')        
        elif x == 3 and y == 10:#story
            textslow('I am dying of thirst out here in the open!\n\n')       
        elif x == 2 and y == 10:#witch
            witch()  
        elif x == 1 and y == 9:#enemy
            enemy()      
        elif x == 1 and y == 8:#story
            textslow('AAAHHH!\n I just found a dead body buried in the sand.\n'); time.sleep(0.75)
            textslow('Welp, that was gross\n\n')       
        elif x == 1 and y == 7:#story
            textslow('There is a wild trader in the distance.\n Going to try to stay away from sight so he does not follow me.\n\n')
        elif x == 1 and y == 6:#story
            textslow('YO!\n Is that a GIANT CENTIPEDE! Sick \n\n')       
        elif x == 1 and y == 5:#enemy
            enemy()       
        elif x == 1 and y == 4:#story
            textslow('I should be aware of the small branches from the tall trees,\nThey might hit me\n\n')       
        elif x == 1 and y == 3:#story
            textslow('UGH!\nNo cellular connection! I am going to die from not having any connection. Not a single bar!\n\n')
        elif x == 3 and y == 1:#story
            textslow('I think I see something in the distance.\nSomething small...\n\n')
        elif x == 4 and y == 1:#witch
            witch()
        elif x == 5 and y == 1:#story
            textslow('I think there was a snake 5 meters away from me! I need to pay attention!\n\n')   
        elif x == 6 and y == 1:#story
            textslow('I am about to cross a sketchy bridge.')
            while True:
                decision = input('\n\nDo I cross it? (Y/N): ').lower()
                if decision == 'y':
                    textslow('I crossed it without dieing. Hooray!\n\n')
                    break
                elif decision == 'n':
                    textslow('I guess I will just go around it.\n\n')
                    break
        elif x == 7 and y == 1:#enemy
            enemy()
        elif x == 8 and y == 1:#story
            textslow('I think I see something in the distance...\n\n')          
        elif x == 9 and y == 1:#witch
            witch()
        elif x == 11 and y == 3:#story
            textslow('Oh no, the fog is thickening.\n\n')        
        elif x == 11 and y == 4:#Math problem
            mathprob()
        elif x == 11 and y == 5:#Random House
            randomHouse()
        elif x == 11 and y == 6:#story
            textslow('I\'m getting tired of swimming now.\n\n')        
        elif x == 11 and y == 7:#enemy
            enemy()
        elif x == 11 and y == 8:#Math problem
            mathprob()
        elif x == 11 and y == 9:#enemy
            enemy()
        elif x == 9 and y == 11:#Math problem
            mathprob()
        elif x == 8 and y == 11:#enemy
            enemy()
        elif x == 7 and y == 11:#witch
            witch()
        elif x == 6 and y == 11:#story
            textslow('Maybe I should find some sticks to make a fire.\n\n')
        elif x == 5 and y == 11:#witch
            witch()
        elif x == 4 and y == 11:#Math problem
            mathprob()
        elif x == 3 and y == 11:#witch
            witch()
        elif x == 6 and y == 6:#this is in case someone goes backwards to the starting position
            textslow('Looks like you went back to your starting position.\nTry not to do this because there is nothing here.\n\n*** You have been sent back to your previous location ***\n\n')
            if movement == 'w':
                y -= 1                
            elif movement == 'a':
                x += 1                
            elif movement == 's':
                y+= 1
            else: #this one is d
                x += 1
            movement_counter -= 1
        else: #prepare ready for the final boss
            movement_counter += 100
        if movement != 'm': #change the list ? to a check mark for the current location of the player
            count = 0
            for i in tiles:
                if tiles[count] == xfactor:
                    tiles[count] = checkmark
                count += 1
            coord = 121-11*(y)+x; tiles[coord-1] = xfactor

if character_health > 0: # if character is applicable for the final boss
    monster_health = random.randint(300,500); monster_name = 'Epic Boomer' #monster health and name
    textslow('This is your turn to prove who you actually are\nYou have to use your strength to kill the FINAL BOSS!\nThis is not as easy as the previous enemies because the stats of this character is always random.\nTake a moment to think about all the accomplishment and success you had to just get to this spot.\nInfront of a huge crowd of 1 million people!\nThis is your moment!\n\nHere comes the final boss\nThe name of the final boss is: ', monster_name, '\nIf you win the battle, you will get a medal of all Warriors!!\nUse your skill very wisely to not lose health because this is your only time to shine!\nNo pressure\n\nThe monster has ',str(monster_health) , ' health and deals 50 damage\nWhile you have ', str(character_health), ' health and deal ', str(strength), ' damage\n')
    enemyBrain('final')
    if character_health > 0: # if the player wins
        textslow('\n\n\nCONGRATULATIONS ', username , '!!!!!!!\nYou won "Warriors" without dying!\nHere is your reward!\n')
        print('\n\n     /\      \n    /  \     \n   /____\    \n  /\    /\   \n /  \  /  \  \n/____\/____\ \n\n')
        textslow('Take it or leave it\n')
        textslow('\033[32m\nThank you for playing Warrior!')
