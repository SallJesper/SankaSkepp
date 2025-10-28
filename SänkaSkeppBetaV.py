from random import randint

water = 0
secretship = 1
hitwater = 2
hitship = 3
torpedo = 4
AtillE = ["A", "B", "C", "D", "E"] #För for-loopar som kräver A-E
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
        
        
def ai_choose_kolumn_ps():
   z = randint(0,4)
   match z:
        case 0:
           return(A2)
        case 1:
            return(B2)
        case 2:
            return(C2)
        case 3:
            return(D2)
        case 4:
            return(E2)
def ai_choose_kolumn_st():
   z = randint(0,4)
   match z:
        case 0:
           return(A1)
        case 1:
            return(B1)
        case 2:
            return(C1)
        case 3:
            return(D1)
        case 4:
            return(E1)

def ai_place_ships():
    for x in range(0, 5):
        while True:
            lista = ai_choose_kolumn_ps()
            y = randint(0,4)
            target = lista[y]
            match target:
                case 0:
                    lista[y] = secretship
                    break
def ai_shoot_target():
    lista = ai_choose_kolumn_st()
    y = randint(0,4)
    target = lista[y]
    match target: #Ändrar brädet
        case 0:
            lista[y] = hitwater
            print("Miss!")
        case 1:
            lista[y] = hitship
            print("Hit!")
        case 2:
            print("You shot here already")
        case 3:
            print("Stop it they're already dead")
        case 4:
            shoot_torpedo(1, randint(0,4))
def place_torpedo():
    for x in range(0,3):
        while True:
            lista = ai_choose_kolumn_ps()
            y = randint(0,4)
            if lista[y] == 0:
                lista[y] = torpedo
                break
        while True:
            lista = ai_choose_kolumn_st()
            y = randint(0,4)
            if lista[y] == 0:
                lista[y] = torpedo
                break
               
def shoot_torpedo(player,rad):
    lista = choose_target(rad, player)
    for x in range(0,5):
       match lista[x]:
            case 0:
               lista[x] = hitwater
            case 1:
                lista[x] = hitship
            case 4:
                lista[x] = hitwater
        

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
        if targets[x] == water or targets[x] == secretship or targets[x] == torpedo:
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
        case 4:
            print("You found a torpedo!")
            rad = input("Where fire torpedo?")
            shoot_torpedo(player,rad)
def view_targets(player): #Printar strängar av brädet med hjälp av target_to_string
    print()
    print("    1  2  3  4  5")
    print()
    string = ""
    a = 0
    if player == 1:
        for x in AtillE:
            string = ""
            string = string + x + "   "
            string = string + target_to_string(kolumner1[a])
            print(string)
            a = a + 1
        print()
    if player == 2:
        for x in AtillE:
            string = ""
            string = string + x + "   "
            string = string + target_to_string(kolumner2[a])
            print(string)
            a = a + 1
        print()

def user_actions(player): #Funktion för användaren
    view_targets(player)
    shoot_target(player)

def ai_actions():
    view_targets(1)
    ai_shoot_target()
        
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
            ai_place_ships()
            place_ships(1)
            place_torpedo()
            while True:
                input("press enter to continue")
                user_actions(2)
                if won_game(2) == True:
                    print("You defeated SeaNet, humanity is safe!")
                    print()
                    input("press enter to return to menu")
                    break
                input("press enter to continue")
                ai_actions()
                if won_game(1) == True:
                    print("Hasta la vista baby!")
                    print()
                    input("press enter to return to menu")
                    break
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
            place_torpedo()
            while True:
                user_actions(2)
                if won_game(2) == True:
                    print("Player 1 won!")
                    print()
                    input("press enter to return to menu")
                    break
                user_actions(1)
                if won_game(1) == True:
                    print("Player 2 won!")
                    print()
                    input("press enter to return to menu")
                    break
        elif mittval == "q":
            break

main()