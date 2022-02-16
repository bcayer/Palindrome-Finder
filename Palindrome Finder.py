# Brielle Cayer Lab2

print('Welcome to the Palindrome Finder!')
attempt = input('Please enter a word or phrase to test:\n>>')
palindromes = []

while attempt != '':
    cleanedAttempt = attempt.replace('.', '').replace('!', '').replace(',', '').replace(':', '').replace(';', '').replace('?', '').replace(' ', '')
    reverseAttempt = cleanedAttempt[::-1]
    if reverseAttempt.lower() == cleanedAttempt.lower():
        print('Yes,', attempt, 'is a palidrome!')
        palindromes.append(attempt)
    else:
       print('No, it does not seem', attempt, 'is a palindrome')
    attempt = input('Enter another word or phrase to test (or Enter to exit):\n>>')

print('Thank you for using the palindrome finder. You found the following palindromes:')

for p in palindromes:
    print(p)
