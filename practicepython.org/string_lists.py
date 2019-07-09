
word = input("Insert word in i will check if it is a palindrome or not: ")

reverse_word = word[::-1]

if word == reverse_word: print("It is a palindrome!")
else: print("Sorry, it's not a palindrome.")
