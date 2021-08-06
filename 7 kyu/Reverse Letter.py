import re


def reverse_letter(string):
    filt = ' '.join(re.findall("[a-zA-Z]+", string)).replace(' ', '')
    result = list(reversed(filt))
    return "".join(result)


print(reverse_letter('ab23c'))
print(reverse_letter('ultr53o?n'))
