# importing turtle library, permutations library, and time library
import turtle as t
from itertools import permutations
import time

t.speed(0)

#this is where I will be defining my variables / lists
coordinates = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
P1_coordinates=[]
P2_coordinates=[]
winsPattern =[('A1', 'A2', 'A3'),('A1', 'A3', 'A2'),('A2', 'A1', 'A3'),('A2', 'A3', 'A1'),('A3', 'A1', 'A2'),('A3', 'A2', 'A1'),
              ('B1', 'B2', 'B3'),('B1', 'B3', 'B2'),('B2', 'B1', 'B3'),('B2', 'B3', 'B1'),('B3', 'B1', 'B2'),('B3', 'B2', 'B1'),
              ('C1', 'C2', 'C3'),('C1', 'C3', 'C2'),('C2', 'C1', 'C3'),('C2', 'C3', 'C1'),('C3', 'C1', 'C2'),('C3', 'C2', 'C1'),
              ('A1', 'B1', 'C1'),('A1', 'C1', 'B1'),('B1', 'A1', 'C1'),('B1', 'C1', 'A1'),('C1', 'A1', 'B1'),('C1', 'B1', 'A1'),
              ('A2', 'B2', 'C2'),('A2', 'C2', 'B2'),('B2', 'A2', 'C2'),('B2', 'C2', 'A2'),('C2', 'A2', 'B2'),('C2', 'B2', 'A2'),
              ('A3', 'B3', 'C3'),('A3', 'B3', 'C3'),('B3', 'A3', 'C3'),('B3', 'C3', 'A3'),('C3', 'A3', 'B3'),('C3', 'B3', 'A3'),
              ('A1', 'B2', 'C3'),('A1', 'C3', 'B2'),('B2', 'A1', 'C3'),('B2', 'C3', 'A1'),('C3', 'A1', 'B2'),('C3', 'B2', 'A1'),
              ('A3', 'B2', 'C1'),('A3', 'C1', 'B2'),('B2', 'A3', 'C1'),('B2', 'C1', 'A3'),('C1', 'A3', 'B2'),('C1', 'B2', 'A3')]      

#this where I will be defining my functions
def square():
    t.pu()
    t.goto(-200,150)
    t.right(90)
    t.pd()
    for i in range(4):
        t.forward(320)
        t.left(90)

def grid():
    t.pu()
    t.goto(-100,150)
    t.pd()
    t.forward(320)
    t.pu()
    t.goto(10,150)
    t.pd()
    t.forward(320)
    t.pu()
    t.goto(120,40)
    t.right(90)
    t.pd()
    t.forward(320)
    t.pu()
    t.goto(120,-60)
    t.pd()
    t.forward(320)

def cross():
    t.right(45)
    t.pd()
    t.forward(70)
    t.backward(140)
    t.forward(70)
    t.left(90)
    t.forward(70)
    t.backward(140)

def circle():
    t.circle(40)

#this is where I recall my functions 
square()
grid()

#this is where the letters will be wrote for coordination 
#this is the letter "A"
t.pu()
t.goto(-240,70)
t.write("A",font=("Arial",40,"bold"))
#this is letter 'B"
t.goto(-240,-40)
t.write("B",font=("Arial",40,"bold"))
#this is for letter "C'"
t.goto(-240,-150)
t.write("C",font=("Arial",40,"bold"))
#for here on out it will be numbers 
#this is for number "1" 
t.goto(-170,150)
t.write("1",font=("Arial",40,"bold"))
#this is for the number "2"
t.goto(-60,150)
t.write("2",font=("Arial",40,"bold"))
#this is for the number "3"
t.goto(40,150)
t.write("3",font=("Arial",40,"bold"))

# definition for Player 1 grid for X
def Call_X_Func(coordinate):
        if (coordinate == "A1"):
            t.pu()
            t.goto(-150,95)
            t.pd()
            cross()
            t.pu()
            t.goto(10,150)
            t.right(45)
        elif (coordinate == "A2"):
            t.pu()
            t.goto(-45,95)
            t.pd()
            cross()
            t.pu()
            t.goto(10,150)
            t.right(45)
        elif (coordinate == "A3"):
            t.pu()
            t.goto(65,95)
            t.pd()
            cross() 
            t.pu()
            t.goto(10,150)
            t.right(45) 
        elif (coordinate == "B1"):
            t.pu()
            t.goto(-150,-10)
            t.pd()
            cross()
            t.pu()
            t.goto(10,150)
            t.right(45)  
        elif (coordinate == "B2"):
            t.pu()
            t.goto(-45,-10)
            t.pd()
            cross()  
            t.pu()
            t.goto(10,150)
            t.right(45)
        elif (coordinate == "B3"):
            t.pu()
            t.goto(65,-10)
            t.pd()
            cross() 
            t.pu()
            t.goto(10,150)
            t.right(45)
        elif (coordinate == "C1"):
            t.pu()
            t.goto(-150,-110)
            t.pd()
            cross() 
            t.pu()
            t.goto(10,150)
            t.right(45) 
        elif (coordinate == "C2"):
            t.pu()
            t.goto(-45,-110)
            t.pd()
            cross() 
            t.pu()
            t.goto(10,150)
            t.right(45)
        elif (coordinate == "C3"):
            t.pu()
            t.goto(65,-110)
            t.pd()
            cross()  
            t.pu()
            t.goto(10,150)
            t.right(45)  
# definition for Player 2 grid for O                        
def Call_O_Func(coordinate): 
        if (coordinate == "A1"):
            t.pu()
            t.goto(-150,135) 
            t.pd() 
            circle() 
            t.pu()
            t.goto(10,150)
        elif (coordinate == "A2"):
            t.pu()
            t.goto(-45,135)
            t.pd()
            circle()  
            t.pu()
            t.goto(10,150)
        elif (coordinate == "A3"):
            t.pu()
            t.goto(65,135)
            t.pd()
            circle() 
            t.pu()
            t.goto(10,150)
        elif (coordinate == "B1"):
            t.pu()
            t.goto(-150,30)
            t.pd()
            circle()
            t.pu()
            t.goto(10,150)
        elif (coordinate == "B2"):
            t.pu()
            t.goto(-45,30)
            t.pd()
            circle()
            t.pu()
            t.goto(10,150)
        elif (coordinate == "B3"):
            t.pu()
            t.goto(65,30)
            t.pd()
            circle()
            t.pu()
            t.goto(10,150)
        elif (coordinate == "C1"):
            t.pu()
            t.goto(-150,-80)
            t.pd()
            circle() 
            t.pu()
            t.goto(10,150)
        elif (coordinate == "C2"):
            t.pu()
            t.goto(-45,-80)
            t.pd()
            circle()
            t.pu()
            t.goto(10,150) 
        elif (coordinate == "C3"):
            t.pu()
            t.goto(65,-80)
            t.pd()
            circle() 
            t.pu()
            t.goto(10,150)

# print("Length::",len(coordinates))
def grid_values(Player, answer):
    if Player =="P1": Call_X_Func(answer) 
    else: Call_O_Func(answer) 
i=0
n=len(coordinates)
# print(winsPattern)
while i < n:   
    # print("I:",i,"and N:", n)
    if i%2 == 0:
        print("Player 1: Which coordinates do you select?")
        print(coordinates)
        #This is the user input for the player 1 to choose 
        coordinate = input("I choose coordinate...:")
        if coordinate in coordinates:
            grid_values("P1",coordinate)   #This is where Player 1 to call "grid_values" function with  their coordinates 
            coordinates.remove(coordinate) #Removal of finished coordinates
            P1_coordinates.append(coordinate) #Adding Player 1 selected coordinates to check win pattern
            # print(P1_coordinates)
            # print(list(permutations(P1_coordinates, 3)))
            P1_coordinates_permutations=list(permutations(P1_coordinates, 3)) #Generating Player 1 permutations
            # print(P1_coordinates_permutations)
            i=i+1
            for perm in P1_coordinates_permutations:    #Loop to run through all Player 1 permutations
                # print(perm)
                if perm in winsPattern:      # Condition to check each permutation in winsPattern list
                    print("Player 1 wins")
                    time.sleep(30)
                    exit()
        else: print("ERROR: Invalid coordinate....!") 
    else:    
        print("Player 2: Which coordinates do you select?")
        print(coordinates)
        coordinate = input("I choose coordinate...:")
        if coordinate in coordinates:
            grid_values("P2",coordinate)    #This is where Player 2 to call "grid_values" function with  their coordinates
            coordinates.remove(coordinate)  #Removal of finished coordinates
            P2_coordinates.append(coordinate) #Adding Player 2 selected coordinates to check win pattern
            # print(P2_coordinates)
            # print(list(permutations(P2_coordinates, 3)))
            P2_coordinates_permutations=list(permutations(P2_coordinates, 3)) #Generating Player 2 permutations
            # print(P2_coordinates_permutations)
            i=i+1
            for perm in P2_coordinates_permutations:    #Loop to run through all Player 2 permutations
                # print(perm)
                if perm in winsPattern:     # Condition to check each permutation in winsPattern list
                    print("Player 2 wins")
                    time.sleep(30)
                    exit()
        else: print("ERROR: Invalid coordinate....!")
print("Both Players are tied....!")
wn = t.Screen()
wn.mainloop()
exit()    


