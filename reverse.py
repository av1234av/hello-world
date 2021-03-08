def reverse_number(n):
    num = 0
    while n>0:
        remain = n % 10
        num = num * 10 + remain
        n = n / 10
    return num

def reverse_recursive(s):
    if s:
        return reverse_recursive(s[1:]) + s[0]
    return ""

def reverse_string(s):
    return s[::-1]

def reverse_words(s):
    _s=s.strip()
    return ' '.join(_s.split()[::-1])

def _isPalindrome(p1, p2):
    if len(p1) < 2: return True
    if p1[0] != p2[-1]: return False
    return _isPalindrome(p1[1:], p2[:-1])

def palindrome(ss):
    s,p=ss.split(':')
    s = s.replace(" ","").upper()
    p = p.replace(" ","").upper()
    # if p.rfind(s[::-1]) == 1:
    if _isPalindrome(s,p):
        return '{0} is a palindrome'.format(ss)
    else:
        return '{0} is not a palindrome'.format(ss)

if __name__ == '__main__':
    # print reverse_number(1234567)
    # print reverse_string("Hello World")
    # print reverse_words("  the    sky is    blue  ")

    print(palindrome('Campus mottob:Bottoms up Mac'))

    print(reverse_recursive("Hello World"))
