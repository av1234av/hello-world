import itertools
from collections import defaultdict

class groupby(object):
    def __init__(self,iterable):
        self.it = iter(iterable)
        self.currkey = self.nextkey= self.currvalue = None

    def __iter__(self):
        return self

    def next(self):
        while self.currkey == self.nextkey:
            self.currvalue = next(self.it)
            self.currkey = self.currvalue
        self.nextkey = self.currkey
        return(self.currkey,self._grouper(self.nextkey))

    def _grouper(self, nextkey):
        while self.currkey == nextkey:
            yield self.currvalue
            self.currvalue = next(self.it)
            self.currkey = self.currvalue


def longest_substr(s):
    kount=1
    i=0
    start=1
    j=1
    while i < len(s) -1:
        if s[i] == s[i+1]:
            j += 1
        else:
            if j > kount:
                kount=j
                start=i-j+1
                j=1
        i += 1

    if j > kount:
        kount=j
        start=i-j+1

    return kount,start


def longest_substr1(s):
    max_len=1
    last_char=""
    current_len = 0
    for c in s:
        if c == last_char:
            current_len += 1
            max_len=max(max_len,current_len)
        else:
            current_len = 1
            last_char = c

    return max_len


if __name__ == '__main__':
    s='abbbccccccddddddddd'
    # print max([len(list(y)) for c, y in itertools.groupby('abbbccccccdddddddddddd')])
    print longest_substr1('abbbccccccddddddddd')

    print max([len(list(g)) for k,g in groupby(s)])