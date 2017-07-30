def find_buy_sell(prices):
    n = len(prices)
    i=0
    while i < n-1:
        while i < n-1 and prices[i+1] <= prices[i]:
            i += 1
        if i > n-1:
            break
        local_min=prices[i]
        i += 1

        while i < n-1 and prices[i+1] >= prices[i]:
            i += 1
        local_max=prices[i]
        i += 1

        yield local_min, local_max

def find_buy_sell_2(prices):
    local_min=prices[0]
    local_max=prices[0]
    for i, price in enumerate(prices):
        if price > prices[i+1]:
            local_min = price
            if i < len(prices)-2 and price[i+1] >= price[i+2]:
                local_max = price[i+1]
        continue

if __name__ == '__main__':
    for buy, sell in find_buy_sell([100,180,262,317,40,194,207]):
        print 'Buy at {0} and sell at {1}'.format(buy, sell)