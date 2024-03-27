import random


def display_word(kata_rahasia, tebaak):
    display =""
    for letter in kata_rahasia:
        if letter.lower() in tebaak:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()
    

def hangman():
    global wins, losses
    words = ["yippie", "yeehaw", "hijau", "kuning", "merah"]

    while words: 
        kata_rahasia = random.choice(words)
        words.remove(kata_rahasia) 

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
                    wins += 1
                    print(*kata_rahasia)
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
            losses += 1
        print("Skor akhir: Menang =", wins, ", Kalah =", losses)
        if wins == 5:
            break 
        play_again = input("Main lagi? (y/n): ").lower()
        if play_again != 'y':
            break


    if not words: 
        print("KAMU MENEBAK SEMUANYA, KAMU MEMANGG.")
        

wins = 0
losses = 0

while True:  
    hangman()
    if wins == 5:
        break 
    play_again = input("yakin? (press n if u rlly dont wanna play): ").lower()
    if play_again != 'y':
        break

print("Terima kasih sudah bermain!")
