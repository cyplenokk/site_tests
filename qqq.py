def multi(x):
    return x * 3

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def hello(name):
    return f'Привет, {name}!'

def hello_2(name, lang):
    if lang == 'rus':
        return f'Привет, {name}!'
    else:
        return f'Hello, {name}!'

def hello_3(n):
    for i in n:
        print('Hello')

def div(n):
    result = [1, n]
    for i in range(2, n + 1):
        if n % i == 0:
            result.append(i)
    return len(result)


print(div(10))


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i

    return res


print(factorial(10))


def series(n):
    res = 0
    for i in range(1, n - 1):
        res += i
    res += (n - 1) * n
    return res


print(series(4))


def telephone(tel):
    if len(tel[2:]) == 10 and tel[0:1]:
        return True
    else:
        return False


print(telephone('+79774278898'))
