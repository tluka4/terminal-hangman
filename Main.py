import getpass
def printAccording(input):
    if miss == 0:
        print("""
           --------
           |      
           |      
           |      
           |      
           |
        =========  
""")


    elif miss == 1:
        print("""
            --------
            |      ( )
            |      
            |      
            |      
            |
         =========  
 """)

    elif miss == 2:

     print("""
                --------
                |      ( )
                |       |
                |       
                |      
                |
             =========  
     """)

    elif miss == 3:
        print("""
                    --------
                    |      ( )
                    |      /|
                    |       
                    |      
                    |
                =========  
        """)
    elif miss == 4:
         print("""
            --------
            |      ( )
            |      /|\\
            |      
            |      
            |
         =========  
 """)
    elif miss == 5:
         print("""
            --------
            |      ( )
            |      /|\\
            |       /
            |      
            |
         =========  
 """)
    elif miss == 6:
         print("""
            --------
            |      ( )
            |      /|\\
            |       /\\
            |      
            |
         =========  
 """)





print("Player 1 please input a word.")


player1_word = getpass.getpass("-> ")

underline = []
wordtrack = []

for i in player1_word:
    if i == " ":
        underline.append(" ")
        wordtrack.append(i)
        continue

    underline.append("_")
    wordtrack.append(i)


print("Your word is: ")
print(''.join(underline))

curr_counter = 0
miss = 0
flip = 2


while curr_counter < 7:
    print("Player 2 guess a letter.")
    player2_letter = input("Input Letter: ")


    if player2_letter in wordtrack:
        for index,l in enumerate(wordtrack):
            if player2_letter == l:
                underline[index] = l
            if underline == wordtrack:
                flip = 1
                break 

    else: 
        miss += 1
        if miss == 6:
            flip = 0


    printAccording(miss)

    print(''.join(underline))
    curr_counter += 1

    if flip == 0 or flip == 1:
        break


if flip == 0:
    print("Player 2 did not guess the word!")
    print("The correct word was: " + str(''.join(wordtrack)) + "!")

elif flip == 1:
    print("Player 2 guessed the word correctly!")