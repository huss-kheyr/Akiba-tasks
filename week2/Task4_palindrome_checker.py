words = input("Words: ")
reversed_word = words[::-1]

if words.lower() == reversed_word.lower():
    is_palindrome = True
else :
    is_palindrome = False
    
if is_palindrome == True:
    print("The word is a palindrome")
else :
    print("The word is not a palindrome")

