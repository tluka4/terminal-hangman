import getpass

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

while curr_counter < 7:
    print("Player 2 guess a letter.")
    player2_letter = input("Input Letter: ")

    if player2_letter in wordtrack:
        for index,l in enumerate(wordtrack):
            if player2_letter == l:
                underline[index] = l
    print(''.join(underline))
    curr_counter += 1





=======
print("""
           --------
           |      
           |      
           |      
           |      
           |
        =========  
""")


# print("""
#            --------
#            |      
#            |      
#            |      
#            |      
#            |
#         =========  
# """)

# print("""
#            --------
#            |      ( )
#            |      
#            |      
#            |      
#            |
#         =========  
# """)
# print("""
#            --------
#            |      ( )
#            |       |
#            |       
#            |      
#            |
#         =========  
# """)

# print("""
#            --------
#            |      ( )
#            |      /|
#            |       
#            |      
#            |
#         =========  
# """)

# print("""
#            --------
#            |      ( )
#            |      /|\\
#            |      
#            |      
#            |
#         =========  
# """)

# print("""
#            --------
#            |      ( )
#            |      /|\\
#            |       /
#            |      
#            |
#         =========  
# """)

# print("""
#            --------
#            |      ( )
#            |      /|\\
#            |       /\\
#            |      
#            |
#         =========  
# """)


player1_word = input("Here: ")

