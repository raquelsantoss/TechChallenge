
expression = str(input('Digite a expressão que será analisada:'))
countParenthesesOpen = 0
countParenthesesClose = 0

for letter in range(0, len(expression)):
    if(expression[letter] == '('):
        countParenthesesOpen += 1
    elif(expression[letter] == ')'):
        countParenthesesClose += 1

    if(countParenthesesClose > countParenthesesOpen):   #validação para parênteses de sentido opostos ")("
        break 


if(countParenthesesOpen != countParenthesesClose):
    print('Incorrect')
else:
    print('Correct')

