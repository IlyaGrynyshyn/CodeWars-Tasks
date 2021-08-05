def count_bits(n):
    _number = ''
    while n>0:
        _number += str(n%2)
        n = n//2
    return _number.count('1')

print(count_bits(1213))