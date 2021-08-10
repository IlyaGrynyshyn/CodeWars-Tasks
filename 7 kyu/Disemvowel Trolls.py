def disemvowel(string):
    abc = 'AaEeIiOoUu'
    for item in abc:
        string = string.replace(item,'')
    return string

print(disemvowel('Lol'))