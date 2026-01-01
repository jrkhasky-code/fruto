import time
import random
import sys
# costumes
costume1 = '''
 O    O
    ^  
    |  
 (__|__)'''
costume2 = '''
 "O    O"
     ^  
     |  
  (__|__)'''
costume3 = '''
 O    O
    ^  
  o | o
 (__|__)'''
costume4 = '''
 ^    ^
 O    O
    ^  
    |  
 (__|__)'''
costume5 = '''
 ^    ^
    ^  
    |  
 (__|__)'''
dead = '''
 x    x
    ^  
    |  '''
h = '''  ^   ^
    ^ z
    | z
 (__|__)'''
play = '''
 O    O
    ^  
    |  
 (__|_O)'''
print('this is the Fruto OS By: /////')
print(" Credits to //////")
E = int(input('plz enter "play" to play'))
if E == play:
    hunger = 40
    thirst = 40
    fishcapacity = 0
    love = 50
    tiredness = 50
    name = input('Fruto name:   ')
    ownername = input('Owner name:   ')
    print(f'''#1
                {costume1}''')
    time.sleep(2)
    print(f'''#2
                {costume2}''')
    time.sleep(2)
    print(f'''#3
                {costume3}''')
    time.sleep(2)
    print(f'''#4
                {costume4}''')
    time.sleep(2)
    print(f'''#5
                {costume5}''')
    time.sleep(2)
    costume = int(input('costume pick (1,2,3,4,5):   '))
    D = 10
    while D != 0:
        A = "Loading."
        print(A)
        time.sleep(0.2)
        B = "Loading.."
        print(B)
        time.sleep(0.2)
        C = "Loading..."
        print(C)
        D = D-1
    time.sleep(3)
    print("Loading Complete!")
    time.sleep(0.2)
    print(" This is Fruto")
    print(" take good care of him")
    if costume == 1:
        wakestate = costume1
    if costume == 2:
        wakestate = costume2
    if costume == 3:
        wakestate = costume3
    if costume == 4:
        wakestate = costume4
    if costume == 5:
        wakestate = costume5
    time.sleep(0.5)
    print(wakestate)
    print(f'hi {ownername} my name is {name}')
    chat = input("chat:   ")
    while chat != 'exit':
        while chat != 'sleep':
            hunger = hunger-1
            thirst = thirst-2
            love = love-1
            tiredness = tiredness-1
            print(wakestate)
            print('hunger:', hunger)
            print("fish:", fishcapacity)
            print('thirst:', thirst)
            print('love:', love)
            print('tiredness:', tiredness)
            chat = input(
                ' sleep, feed, water, play, fish, or just chat:    ').lower()
            if chat == 'exit':
                sys.exit(f"""{name} is sad you exited
 x    x
    ^  
    |""")
            if chat == 'feed':
                if fishcapacity > 0:
                    hunger = 40
                    fishcapacity = fishcapacity-1
            if hunger == 0:
                sys.exit(f""" {name} has starved 
x    x
   ^  
   |""")
            if chat == 'water':
                thirst = 40
            if thirst == 0:
                sys.exit(f''' {name} got to thirsty
x    x
   ^  
   | ''')
            if tiredness == 0:
                sys.exit(f'''{name} got too tired
{dead}''')
            if chat == 'fish':
                fish_weight = random.randint(1, 20)
                fishcapacity = fish_weight
            if chat == 'play':
                love = love+5
                print(play)
                time.sleep(2)
            if love == 0:
                sys.exit(f'''{name} got to lonely
{dead}''')
        if chat == 'sleep':
            print(h)
            tiredness = 50
            wake = input('wake?:    ').lower()
            if wake == 'yes':
                print(wakestate, '''
*yawn* good morning''')
                chat = wake
else:
    print('wrong  :(')
    E = int(input('Try Again:   '))
    if E == 1234:
        hunger = 40
    thirst = 40
    fishcapacity = 0
    love = 50
    name = input('Fruto name:   ')
    ownername = input('Owner name:   ')
    print(f'''#1
                {costume1}''')
    time.sleep(2)
    print(f'''#2
                {costume2}''')
    time.sleep(2)
    print(f'''#3
                {costume3}''')
    time.sleep(2)
    print(f'''#4
                {costume4}''')
    time.sleep(2)
    print(f'''#5
                {costume5}''')
    time.sleep(2)
    costume = int(input('costume pick (1,2,3,4,5):   '))
    D = 10
    while D != 0:
        A = "Loading."
        print(A)
        time.sleep(0.2)
        B = "Loading.."
        print(B)
        time.sleep(0.2)
        C = "Loading..."
        print(C)
        D = D-1
    time.sleep(3)
    print("Loading Complete!")
    time.sleep(0.2)
    print(" This is Fruto")
    print(" take good care of him")
    if costume == 1:
        wakestate = costume1
    if costume == 2:
        wakestate = costume2
    if costume == 3:
        wakestate = costume3
    if costume == 4:
        wakestate = costume4
    if costume == 5:
        wakestate = costume5
    time.sleep(0.5)
    print(wakestate)
    print(f'hi {ownername} my name is {name}')
    chat = input("chat:   ")
    while chat != 'exit':
        while chat != 'sleep':
            hunger = hunger-1
            thirst = thirst-2
            love = love-1
            print(wakestate)
            print('hunger:', hunger)
            print("fish:", fishcapacity)
            print('thirst:', thirst)
            print('love:', love)
            chat = input(
                ' sleep, feed, water, play, or just chat:    ').lower()
            if chat == 'exit':
                sys.exit(f"""{name} is sad you exited
 x    x
    ^  
    |""")
            if chat == 'feed':
                if fishcapacity > 0:
                    hunger = 40
                    fishcapacity = fishcapacity-1
            if hunger == 0:
                sys.exit(f""" {name} has starved 
x    x
   ^  
   |""")
            if chat == 'water':
                thirst = 40
            if thirst == 0:
                sys.exit(f''' {name} got to thirsty
x    x
   ^  
   | ''')
            if chat == 'fish':
                fish_weight = random.randint(1, 20)
                fishcapacity = fish_weight
            if chat == 'play':
                love = love+5
                print(play)
                time.sleep(2)
        if chat == 'sleep':
            print(h)
            wake = input('wake?:    ').lower()
            if wake == 'yes':
                print(wakestate, '''
*yawn* good morning''')
                chat = wake
            
