def balanced_brackets(s):
    l=[]
    balanced=True
    for c in s:
        if c in '({[':
            l.append(c)
        else:
            if l:
                top=l.pop()
                if not matches(top,c):
                    balanced = False
            else:
                balanced = False

    if balanced and not l:
        return True
    else:
        return False

def matches(open, close):
    open_list="({["
    close_list=")}]"
    return open_list.index(open) == close_list.index(close)

if __name__ == '__main__':
    if balanced_brackets('({[[()]]})'):
        print('Brackets are balanced')
    else:
        print('Unbalanced bracktes')
