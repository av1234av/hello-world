def reverse_number(n):
    num = 0
    while n>0:
        remain = n % 10
        num = num * 10 + remain
        n = n / 10
    return num


def reverse_string(s):
    return s[::-1]

if __name__ == '__main__':
    print reverse_number(1234567)
    print reverse_string("Hello World")