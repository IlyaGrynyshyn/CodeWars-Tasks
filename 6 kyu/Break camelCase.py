def solution(s):
    result = ''
    for letter in s:
        if letter.isupper():
            result += " " + letter
        else:
            result += letter
    return result

print(solution('helloWorld'))