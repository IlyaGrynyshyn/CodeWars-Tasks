def first_non_repeating_letter(string):
    str = []
    for i in string:
        str.append(i.lower())
    for i in string:
        if str.count(i.lower()) == 1:
            return i
    return "''"

print(first_non_repeating_letter('PythonforallPythonMustforall'))
print(first_non_repeating_letter('tutorialspointfordeveloper'))
print(first_non_repeating_letter('AABBCC'))
print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))
