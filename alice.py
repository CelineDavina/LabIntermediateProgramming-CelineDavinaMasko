alice_txt = open(r"C:\Users\DNY123\Desktop\coding\LabIntermediateProgramming-CelineDavinaMasko\New folder\Alice.txt")
full_alice = alice_txt.read()

words_alice = full_alice.split()
total_words_alice = len(words_alice)
print("jumlah kata : ",total_words_alice)

set_words_alice = set(words_alice)
unique_words = len(set_words_alice)
print("total kata unik : ",unique_words)

words_txt = open(r"C:\Users\DNY123\Desktop\coding\LabIntermediateProgramming-CelineDavinaMasko\New folder\words.txt")
full_words = words_txt.read()
kataa = full_words.split()
set_kataa = set(kataa)
total_kataa = len(set_kataa)

difference = []
for i in set_words_alice:
    if i not in set_kataa:
        difference.append(i)

print("difference between alice and words file\n\n", difference)
print("\n\nbanyak kata yang typo : ", len(difference))

alice_txt.close()
words_txt.close()
