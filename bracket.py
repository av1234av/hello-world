def balanced_brackets(s):
    l=[]

    for c in s:
        if c == '(':
            l.append(c)
        else:
            if l:
                l.pop()
            else:
                return False

    return not l

if __name__ == '__main__':
    if balanced_brackets('((())'):
        print 'Brackets are balanced'
    else:
        print 'Unbalanced bracktes'
