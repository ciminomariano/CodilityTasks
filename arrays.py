from urllib3.connectionpool import xrange


def negative(temperatures):
    N = len(temperatures)
    days = 0
    for i in xrange(N):
        if temperatures[i] < 0:
            days += 1

    return days


def negative_without_indexes(temperatures):
    N = len(temperatures)
    days = 0
    for i in temperatures:
        if i < 0:
            days += 1

    return days


def check_existing_product(product, shopping):
    if product in shopping:
        return True


shopping = ['bread', 'butter', 'cheese']
temperatures = [0] * 365

temperatures[1] = 23
temperatures[0] = -5
temperatures[3] = -5
temperatures[4] = -10

shopping += ['eggs']

print(shopping)
print(temperatures)
negative_days = negative_without_indexes(temperatures)
print(negative_days)

product = 'bread'

exists = check_existing_product(product, shopping)

if exists:
    print("this products is in the list")
