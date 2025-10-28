water = 0
secretship = 1
hitwater = 2
hitship = 3
AtillE = ["A", "B", "C", "D", "E"] #För for-loopar som kräver A-E

A = []
B = []
C = []
D = []
E = []
kolumner = []

A2 = []
B2 = []
C2 = []
D2 = []
E2 = []
kolumner2 = []

options1 = {"p":"Play", "q":"Quit"} #Listor till menu
options2 = {"a":"Play again", "q":"Quit"} #Listor till menu
options3 = {"1":"1 Player", "2":"2 Players"} #Listor till menu

def splash():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("          Skepp Sänk")
    print()          
    print("     a hit or miss game")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()

def create_grid():
    global A
    global B
    global C
    global D
    global E
    global kolumner
    A = [0, 0, 0, 0, 0]
    B = [0, 0, 0, 0, 0]
    C = [0, 0, 0, 0, 0]
    D = [0, 0, 0, 0, 0]
    E = [0, 0, 0, 0, 0]
    kolumner = [A, B, C, D, E]

def place_ships():
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
        lista = choose_target(place)
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

def choose_target(target): #Ger tillbaka användbar lista
    match target[0]:
        case "A":
            return(A)
        case "B":
            return(B)
        case "C":
            return(C)
        case "D":
            return(D)
        case "E":
            return(E)
        case _:
            print("Try Again")
        
def shoot_target(): #Skjutfunktion
    while True: #Kollar att spelaren skrivit in giltiga koordinater
        shoot = input("Shoot target: ")
        match shoot[0]:
            case "A" | "B" | "C" | "D" | "E":
                match shoot[1]:
                    case "1" | "2" | "3" | "4" | "5":
                        break
                    case _: print("Try again!")
            case _: print("Try again!")
    lista = choose_target(shoot)
    target = lista[int(shoot[1])-1]
    match target: #Ändrar brädet
        case 0:
            lista[int(shoot[1])-1] = hitwater
        case 1:
            lista[int(shoot[1])-1] = hitship
        case 2:
            print("You shot here already")
        case 3:
            print("Stop it they're already dead")
    
def view_targets(): #Printar strängar av brädet med hjälp av target_to_string
    print()
    print("    1  2  3  4  5")
    print()
    string = ""
    a = 0
    for x in AtillE:
        string = ""
        string = string + x + "   "
        string = string + target_to_string(kolumner[a])
        print(string)
        a = a + 1
    print()

def user_actions(): #Funktion för användaren
    while won_game() == False:
        view_targets()
        shoot_target()
    print()
    print("You have won the game!")
    print()
        
def won_game(): #Kollar om spelet är klart
    a = True
    for b in range(0, 5):
        for c in range(0, 5):
            if kolumner[b][c] == 1:
                a = False
    return a
    if a == True:
        A = [0, 0, 0, 0, 0]
        B = [0, 0, 0, 0, 0]
        C = [0, 1, 1, 1, 0]
        D = [0, 0, 0, 0, 0]
        E = [0, 0, 0, 0, 0]

        
def main(): #Main
    splash()
   
    while True:
        mittval = menu("Select an action", "Option: ", options1)
        if mittval == "p":
            create_grid()
            place_ships()
            user_actions()
        elif mittval == "q":
            break

main()