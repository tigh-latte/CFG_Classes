import inflect
p = inflect.engine()

number = input('\nSelect a number between 1 and 25:\n')

if int(number) > 25 or int(number) == 0:
    print("Value unrecognised! Please enter a number between 1 and 25")
    exit(0)

def game(number):
    num_list = []
    if len(number) == 1:
        number = '0' + number
    for i, digit in enumerate(number):
        num_word = p.number_to_words(digit[0]).capitalize()
        if i == 0:
            num_word += ' Ten'
        elif i == 1:
            num_word += ' One'
        if int(digit) != 1:
            num_word += 's'

        num_list.append(num_word)
    return(num_list)

print(', '.join(game(number)))