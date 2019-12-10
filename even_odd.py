def even_out(ll):
    for i in ll:
        if i%2 == 0:
            yield i

if __name__ == '__main__':
    print ([i for i in [2,5,6,3,7,8,10,3,24,12,16] if i%2 == 0])
    print ([i for i in [2, 5, 6, 3, 7, 8, 10, 3, 24, 12, 16] if i % 2 == 1])