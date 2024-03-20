import os
os.system('cls')


def display_word(kata_rahasia, tebaak):
    display =""
    for letter in kata_rahasia:
        if letter.lower() in tebaak:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

kata_rahasia = "yippie"
chances = 7
tebaak = []
    

while chances > 0:
    print("\n", display_word(kata_rahasia, tebaak))
    tebak_huruf = input("tebak 1 huruf: ").lower()

    if not tebak_huruf.isalpha() or len(tebak_huruf) != 1:
        print("masukkan hanya 1 HURUF")
        continue

    if tebak_huruf in tebaak:
        print("kamu sudah menebak huruf ini")
        continue

    tebaak.append(tebak_huruf) 

    if tebak_huruf in kata_rahasia.lower() :
        print("benar")
        if all(letter in tebaak for letter in kata_rahasia.lower()):
            print("KAMU MENANG")
            break
    elif tebak_huruf not in kata_rahasia:
        print("salah")
        chances = chances - 1
        print("chances =", chances)
        if chances == 6:
            print("  +---+")
        elif chances == 5:
            print("  +---+")
            print("  O   |")
        elif chances == 4:
            print("  +---+")
            print("  O   |")
            print("  |   |")
        elif chances == 3:
            print("  +---+")
            print("  O   |")
            print("  |   |")
            print(" /|   |")
        elif chances == 2:
            print("  +---+")
            print("  O   |")
            print("  |   |")
            print(" /|\  |")
        elif chances == 1:
            print("  +---+")
            print("  O   |")
            print("  |   |")
            print(" /|\  |")
            print(" /    |")
        elif chances == 0:
            print("  +---+")
            print("  O   |")
            print("  |   |")
            print(" /|\  |")
            print(" / \  |")
            print("you lose")
if chances == 0:
    print("KAMU KALAH HAHAHAHA")