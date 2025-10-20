water = 0
secretship = 1
hitwater = 2
hitship = 3
test = ["A", "B", "C", "D", "E"]
A = [0, 0, 0, 0, 0]
B = [0, 0, 0, 0, 0]
C = [0, 1, 1, 1, 0]
D = [0, 0, 0, 0, 0]
E = [0, 0, 0, 0, 0]
kolumner = [A, B, C, D, E]

options1 = {"p":"Play", "q":"Quit"} #Listor till menu

def splash():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("          Skepp Sänk")
    print()          
    print("     a hit or miss game")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

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

def target_to_string(targets):
    string = ""
    for x in range(len(targets)):
        if targets[x] == water or targets[x] == secretship:
            string = string + "O  "
        elif targets[x] == hitwater:
            string = string + "*  "
        elif targets [x] == hitship:
            string = string + "X  "
    return string

def choose_target(target):
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
        
def shoot_target():
    shoot = input("Shoot target: ")
    lista = choose_target(shoot)
    target = lista[int(shoot[1])-1]
    match target:
        case 0:
            lista[int(shoot[1])-1] = hitwater
        case 1:
            lista[int(shoot[1])-1] = hitship
        case 2:
            print("You shot here already")
        case 3:
            print("Stop it they're already dead")

    
    
        
test = ["A", "B", "C", "D", "E"]
def view_targets():
    print("    1  2  3  4  5")
    print()
    string = ""
    a = 0
    for x in test:
        string = ""
        string = string + x + "   "
        string = string + target_to_string(kolumner[a])
        print(string)
        a = a + 1

def user_actions():
    while won_game() == False:
        view_targets()
        shoot_target()
    print("You have won the game!")
        
        
def won_game():
    a = True
    x = 0
    for b in range(0, 5):
        for c in range(0, 5):
            if kolumner[b][c] == 1:
                a = False
    return a
won_game()
        

def main():
    splash()
    while True:
        mittval = menu("Select an action", "Option: ", options1)
        if mittval == "p":
            user_actions()
        elif mittval == "q":
            break


