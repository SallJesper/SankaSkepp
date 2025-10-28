from random import randint

water = 0
secretship = 1
hitwater = 2
hitship = 3
AtillE1 = ["A1", "B1", "C1", "D1", "E1"] #För for-loopar som kräver A-E
AtillE2 = ["A2", "B2", "C2", "D2", "E2"]
A1 = []
B1 = []
C1 = []
D1 = []
E1 = []
kolumner1 = []

A2 = []
B2 = []
C2 = []
D2 = []
E2 = []
kolumner2 = []

options1 = {"1":"Play vs AI","2":"Play vs a friend", "q":"Quit"} #Listor till menu
options2 = {"a":"Play again", "q":"Quit"} #Listor till menu

def splash():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("          Skepp Sänk")
    print()          
    print("     R.I.P BoatMcBoatface")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()

def create_grid():
    global A1
    global B1
    global C1
    global D1
    global E1
    global kolumner1
    global A2
    global B2
    global C2
    global D2
    global E2
    global kolumner2
    A1 = [0, 0, 0, 0, 0]
    B1 = [0, 0, 0, 0, 0]
    C1 = [0, 0, 0, 0, 0]
    D1 = [0, 0, 0, 0, 0]
    E1 = [0, 0, 0, 0, 0]
    kolumner1 = [A1, B1, C1, D1, E1]
    A2 = [0, 0, 0, 0, 0]
    B2 = [0, 0, 0, 0, 0]
    C2 = [0, 0, 0, 0, 0]
    D2 = [0, 0, 0, 0, 0]
    E2 = [0, 0, 0, 0, 0]
    kolumner2 = [A2, B2, C2, D2, E2]

def place_ships(player):
    for x in range(0, 5):
        place = input("Place ship: ")
        while True:
            match place[0]:
                case "A" | "B" | "C" | "D" | "E":
                    match place[1]:
                        case "1" | "2" | "3" | "4" | "5":
                            break
                        case _: print("Try again!")
                case _: print("Try again!")
        lista = choose_target(place, player)
        target = lista[int(place[1])-1]
        match target: #Ändrar brädet
            case 0:
                lista[int(place[1])-1] = secretship
            case 1:
                print("there is a ship here already")

def menu(title, prompt, options): #Menyfunktion
    print(title)
    for x in options:
        print(f"{x}) {options[x]}") #Printar alla options
    while True:
        print()
        mv = input(f"{prompt}") #Val av option
        if (mv in options) == True: #Valet finns med som en option
            print(f" You selected action {mv}) {options[mv]}")
            print()
            return(mv) #Returnerar valet
            break
        else:
            print("You have selected an incorrect option, try again") #Felaktigt val

def target_to_string(targets): #Funktion för att ändra koordinater till strängar
    string = ""
    for x in range(len(targets)):
        if targets[x] == water or targets[x] == secretship:
            string = string + "O  "
        elif targets[x] == hitwater:
            string = string + "*  "
        elif targets [x] == hitship:
            string = string + "X  "
    return string

def choose_target(target, player): #Ger tillbaka användbar lista
    if player == 1:
        match target[0]:
            case "A":
                return(A1)
            case "B":
                return(B1)
            case "C":
                return(C1)
            case "D":
                return(D1)
            case "E":
                return(E1)
            case _:
                print("Try Again")
    elif player == 2:
        match target[0]:
            case "A":
                return(A2)
            case "B":
                return(B2)
            case "C":
                return(C2)
            case "D":
                return(D2)
            case "E":
                return(E2)
            case _:
                print("Try Again")
        
def shoot_target(player): #Skjutfunktion
    while True: #Kollar att spelaren skrivit in giltiga koordinater
        if player == 1:
            shoot = input("Player 2: shoot target: ")
        elif player == 2:
            shoot = input("Player 1: shoot target: ")
        match shoot[0]:
            case "A" | "B" | "C" | "D" | "E":
                match shoot[1]:
                    case "1" | "2" | "3" | "4" | "5":
                        break
                    case _: print("Try again!")
            case _: print("Try again!")
    lista = choose_target(shoot, player)
    target = lista[int(shoot[1])-1]
    match target: #Ändrar brädet
        case 0:
            lista[int(shoot[1])-1] = hitwater
            print("Miss!")
        case 1:
            lista[int(shoot[1])-1] = hitship
            print("Hit!")
        case 2:
            print("You shot here already")
        case 3:
            print("Stop it they're already dead")
    
def view_targets(player): #Printar strängar av brädet med hjälp av target_to_string
    print()
    print("    1  2  3  4  5")
    print()
    string = ""
    a = 0
    if player == 1:
        for x in AtillE1:
            string = ""
            string = string + x + "   "
            string = string + target_to_string(kolumner1[a])
            print(string)
            a = a + 1
        print()
    if player == 2:
        for x in AtillE2:
            string = ""
            string = string + x + "   "
            string = string + target_to_string(kolumner2[a])
            print(string)
            a = a + 1
        print()

def user_actions(player): #Funktion för användaren
    view_targets(player)
    shoot_target(player)

        
def won_game(player): #Kollar om spelet är klart
    if player == 1:
        a = True
        for b in range(0, 5):
            for c in range(0, 5):
                if kolumner1[b][c] == 1:
                    a = False
    elif player == 2:
        a = True
        for b in range(0, 5):
            for c in range(0, 5):
                if kolumner2[b][c] == 1:
                    a = False
    return a

    

        
def main(): #Main
    splash()
    while True:
        mittval = menu("Select an action", "Option: ", options1)
        if mittval == "1":
            create_grid()
            
            
            place_ships(1)
        
        elif mittval == "2":
            create_grid()
            print("Player 1: place your ships")
            place_ships(1)
            for x in range(0,15):
                print()
            print("Player 2: place your ships")
            place_ships(2)
            for x in range(0,15):
                print()
            while True:
                user_actions(2)
                if won_game(2) == True:
                    print("Player 1 won!")
                    break
                user_actions(1)
                if won_game(1) == True:
                    print("Player 2 won!")
                    break
        elif mittval == "q":
            break

main()