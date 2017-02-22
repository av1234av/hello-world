import csv
from collections import namedtuple
import time
from collections import OrderedDict

def remove_dups(my_list):
    q_list=set()
    for item in my_list:
        if item not in q_list:
            q_list.add(item)
    return q_list

def load_csv():
    with open("C:\\Temp\\prices.txt",'r') as f:
        stock_list=[]
        dreader=csv.DictReader(f, ['File', 'Time', 'Stock', 'Price'], delimiter=' ')
        for row in dreader:
            del row['File']
            stock_list.append(row)

        print stock_list
        lowest_price = min(stock_list, key=lambda x: float(x['Price']))
        highest_price = max(stock_list, key=lambda x: float(x['Price']))
        print lowest_price
        print highest_price

def load_namedtuples():
    Quote = namedtuple('Quote',['Time','Stock','Price'])

    with open("C:\\Temp\\prices.txt", 'r') as f:
        for row in f:
            ll.append(Quote(*(row.strip().split()[1:])))

    print 'total quotes: {}'.format(len(ll))
    print 'last entry {}'.format(ll[-1])

    t1=time.time()
    print 'total count after removing duplicates {0} took {1}'.format(len(remove_dups(ll)),time.time()-t1)


if __name__ == '__main__':
    load_csv()