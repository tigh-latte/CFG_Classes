def age_validate(age):
    if age < 0:
        raise ValueError("Only positive numbers allowed!")
    assert 12 < age <= 19
    return True

def name_validate(name_str):
    if ',' not in name_str:
        raise ValueError("Incorrect Input: Missing ',' to separate name and surname.")

    name, surname = name_str.split(',')

    if not len(name):
        raise ValueError("Incorrect Input: Missing Name")

    if not len(surname):
        raise ValueError("Incorrect Input: Missing Surname")

# age_validate(-1)
# name_validate(',Bataglini')

isSuccessful = False

try:
    name = input("Please enter your name and surname separated by a comma: \n")
    name_validate(name)
    age = int(input("Please enter your age: \n"))
    age_validate(age)

except ValueError as exc:
    print("%s" % exc)

except AssertionError as exc:
    print("Yer too old or too young son, away you go")

else:
    with open("registration_file.txt", 'a+') as file:
        file.write("New member name: {} and age {}. \n".format(name, age))
        isSuccessful = True

finally:
    if isSuccessful:
        print("Registration process completed!")
    else:
        print("Could not complete registration. Please try again.")