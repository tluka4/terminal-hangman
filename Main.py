print("Player 1 please input a word.")

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

underline = []

for i in player1_word:
    if i == " ":
        underline.append(" ")
        continue

    underline.append("_")


print("Your word is ")
print(''.join(underline))


### thiS is a test