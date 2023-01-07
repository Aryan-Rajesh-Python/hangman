import random
from stage import stages,logo
from words import word_list
print(logo)
a=random.choice(word_list)
lives=6
lst2=[]
for i in range(len(a)):
    lst2.append("_")
end_of_game=False
while(end_of_game==False):
    b=input("Guess a letter: ")
    b=b.lower()
    if b in a:
        print(f"You have already guessed {b}.")
    for i in range(len(a)):
        letter=a[i]
        if(letter==b):
            lst2[i]=letter
    if b not in a:
        print("You have guessed the wrong word. So you are gonna loose a life!")
        lives-=1
        if(lives==0):
            end_of_game=True
            print("You Lost")
    print(f"{' '.join(lst2)}")
    if "_" not in lst2:
        end_of_game=True
        print("You Won")
    print(stages[lives])