import random

options = ["JAKIE ZERO DEBILU", "kamień", "papier", "nożyce"]


playMode = input("1. Graj z graczem, 2. Graj z komputerem, 3. Komputer vs Komputer")

if playMode=="1":

    noWinner = True

    while noWinner:
        ou1 = int(input("Kamień 1, Papier 2, Nożyce 3"))
        ou2 = int(input("Kamień 1, Papier 2, Nożyce 3"))

        if ou1 == ou2:
            print(f"Remis, G1-{options[ou1]} : G2-{options[ou2]}")
        elif ou2 == 1 and ou1 == 3:
            print(f"Wygrywa gracz 2, G1-{options[ou1]} : G2-{options[ou2]}")
            noWinner = False
        elif ou2 == 1 and ou1 == 2:
            print(f"Wygrywa gracz 1, G1-{options[ou1]} : G2-{options[ou2]}")
            noWinner = False
        elif ou2 == 2 and ou1 == 1:
            print(f"Wygrywa gracz 2, G1-{options[ou1]} : G2-{options[ou2]}")
            noWinner = False
        elif ou2 == 2 and ou1 == 3:
            print(f"Wygrywa gracz 1, G1-{options[ou1]} : G2-{options[ou2]}")
            noWinner = False
        elif ou2 == 3 and ou1 == 1:
            print(f"Wygrywa gracz 1, G1-{options[ou1]} : G2-{options[ou2]}")
            noWinner = False
        elif ou2 == 2 and ou1 == 1:
            print(f"Wygrywa gracz 2, G1-{options[ou1]} : G2-{options[ou2]}")
            noWinner = False
        elif ou2 == 1 and ou1 == 2:
            print(f"Wygrywa gracz 1, G1-{options[ou1]} : G2-{options[ou2]}")
            noWinner = False
        elif ou2 == 3 and ou1 == 2:
            print(f"Wygrywa gracz 2, G1-{options[ou1]} : G2-{options[ou2]}")
            noWinner = False

if playMode=="2":

    noWinner = True

    while noWinner:
        ou1 = int(input("Kamień 1, Papier 2, Nożyce 3"))
        ou2 = random.randrange(0,3)

        if ou1 == ou2:
            print(f"Remis, G1-{options[ou1]} : K-{options[ou2]}")
        elif ou2 == 1 and ou1 == 3:
            print(f"Wygrywa Komputer, G1-{options[ou1]} : K-{options[ou2]}")
            noWinner = False
        elif ou2 == 1 and ou1 == 2:
            print(f"Wygrywa gracz, G1-{options[ou1]} : K-{options[ou2]}")
            noWinner = False
        elif ou2 == 2 and ou1 == 1:
            print(f"Wygrywa Komputer, G1-{options[ou1]} : K-{options[ou2]}")
            noWinner = False
        elif ou2 == 2 and ou1 == 3:
            print(f"Wygrywa gracz, G1-{options[ou1]} : K-{options[ou2]}")
            noWinner = False
        elif ou2 == 3 and ou1 == 1:
            print(f"Wygrywa gracz, G1-{options[ou1]} : K-{options[ou2]}")
            noWinner = False
        elif ou2 == 2 and ou1 == 1:
            print(f"Wygrywa Komputer, G1-{options[ou1]} : K-{options[ou2]}")
            noWinner = False
        elif ou2 == 1 and ou1 == 2:
            print(f"Wygrywa gracz, G1-{options[ou1]} : K-{options[ou2]}")
            noWinner = False
        elif ou2 == 3 and ou1 == 2:
            print(f"Wygrywa Komputer, G1-{options[ou1]} : K-{options[ou2]}")
            noWinner = False

if playMode=="3":

    noWinner = True

    while noWinner:
        ou1 = random.randrange(0,3)
        ou2 = random.randrange(0,3)

        if ou1 == ou2:
            print(f"Remis, G1-{options[ou1]} : G2-{options[ou2]}")
        elif ou2 == 1 and ou1 == 3:
            print(f"Wygrywa gracz 2, G1-{options[ou1]} : G2-{options[ou2]}")
            noWinner = False
        elif ou2 == 1 and ou1 == 2:
            print(f"Wygrywa gracz 1, G1-{options[ou1]} : G2-{options[ou2]}")
            noWinner = False
        elif ou2 == 2 and ou1 == 1:
            print(f"Wygrywa gracz 2, G1-{options[ou1]} : G2-{options[ou2]}")
            noWinner = False
        elif ou2 == 2 and ou1 == 3:
            print(f"Wygrywa gracz 1, G1-{options[ou1]} : G2-{options[ou2]}")
            noWinner = False
        elif ou2 == 3 and ou1 == 1:
            print(f"Wygrywa gracz 1, G1-{options[ou1]} : G2-{options[ou2]}")
            noWinner = False
        elif ou2 == 2 and ou1 == 1:
            print(f"Wygrywa gracz 2, G1-{options[ou1]} : G2-{options[ou2]}")
            noWinner = False
        elif ou2 == 1 and ou1 == 2:
            print(f"Wygrywa gracz 1, G1-{options[ou1]} : G2-{options[ou2]}")
            noWinner = False
        elif ou2 == 3 and ou1 == 2:
            print(f"Wygrywa gracz 2, G1-{options[ou1]} : G2-{options[ou2]}")
            noWinner = False



