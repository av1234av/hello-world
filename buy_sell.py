# Algorithm to find best price to buy and sell, given a list of prices
# e.g [100,180,262,317,40,194,207] will return buy at 100 & sell at 317, buy at  40 & sell at 207
# it is a same problem as finding local minima and local maxima
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


# O(nk) time, O(nk) space
def maxProfitsKtransactions(prices, k):
    profits = [[0 for d in range(len(prices))] for t in range(k + 1)]
    for t in range(1,k + 1):
        max_thus_far = float("-inf")
        for d in range(1, len(prices)):
            max_thus_far = max(max_thus_far, profits[t-1][d-1] - prices[d - 1])
            profits[t][d] = max(max_thus_far + prices[d], profits[t][d - 1])
    return profits[-1][-1]

def maxProfitsKtransactions_1(prices, k):
    buy_sell_iter = iter(find_buy_sell(prices))
    tot_profit=0
    t=0
    while t < k:
        buy, sell = next(buy_sell_iter)
        tot_profit += sell - buy
        t += 1
    return tot_profit

if __name__ == '__main__':
    prices=[5,11,3,50,60,90]
    # prices=[100,180,262,317,40,194,207]
    print('Total profit: {}'.format(maxProfitsKtransactions_1(prices, 2)))

    print('Total profit: {}'.format(maxProfitsKtransactions(prices, 2)))