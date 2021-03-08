'''
Problem statement: Find minimum coins needed for a given change.
https://runestone.academy/runestone/books/published/pythonds/Recursion/DynamicProgramming.html#:~:text=What%20is%20the%20smallest%20number,one%20dime%2C%20and%20three%20pennies.
'''

from collections import Counter
'''
Solution 1
'''
def make_change(coin_list, change):
    min_coins=[0]*(change+1)
    coins_used=[0]*(change+1)
    for cents in range(change+1):
        coin_count = cents
        new_coin=1

        for j in [c for c in coin_list if c<=cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin
    return min_coins[change], coins_used

'''
Solution 2
Recursive algo to find min number of coins needed for a given change.
Note: know_result list is to keep a cache of already found min coins for a given change. This reduces the recursion.
'''
def make_change_rec(coin_list, change, known_result):
    min_coins = change
    if change in coin_list:
        known_result[change]=1
        return 1
    elif known_result[change] > 0:
        return known_result[change]
    else:
        for i in [c for c in coin_list if c <= change]:
            num_coins = 1 + make_change_rec(coin_list, change - i, known_result)
            if num_coins < min_coins:
                min_coins = num_coins
                known_result[change]=num_coins
    return min_coins
'''
Solution 3
Greedy algo to find minimum number of coins needed for a given change. It works for US coins denomination 
but not for generic (with any type of coin distribution)
'''
def greedy_make_change(coin_list, change):
    coins = Counter()
    while change > 0:
        new_change = change - coin_list[-1]
        if new_change >= 0:
            change = new_change            
            coins[coin_list[-1]] += 1 
        else:
            coin_list.pop()
    return coins

if __name__ == '__main__':
    change = 63
    total_coins, coins_used=make_change([1,5,10,25], change)
    coin = change
    while coin > 0:
        c=coins_used[coin]
        print(c)
        coin = coin - c
    coins = greedy_make_change(coin_list=[1,5,10,25], change=change) # works
    print(coins)
    coins = greedy_make_change(coin_list=[1,5,10,21,25], change=change) # does not work
    print(coins)
    coins = make_change_rec(coin_list=[1,5,10,21, 25], change=change, known_result=[0]*64)
    print(coins)