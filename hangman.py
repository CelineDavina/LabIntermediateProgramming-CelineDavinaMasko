import os
os.system('cls')

kata_rahasia = "yippie"
chances = 6
tebaak = set()

while True:
    tebak_huruf = input("tebak 1 huruf: ").lower()
    if not tebak_huruf.isalpha() or len(tebak_huruf) != 1:
        print("masukkan hanya 1 HURUF")
        continue

    if chances > 0  and set(kata_rahasia):
        if tebak_huruf in tebaak:
            print("kamu sudah menebak huruf ini")
        elif tebak_huruf in kata_rahasia :
            kata_rahasia = kata_rahasia.replace(tebak_huruf, '')
            tebaak.add(tebak_huruf)
            print("benar")
        elif tebak_huruf not in kata_rahasia:
            print("salah")
            chances = chances - 1
            # print(chances)
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
    else :
        break
                