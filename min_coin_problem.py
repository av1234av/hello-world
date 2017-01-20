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

if __name__ == '__main__':
    change = 63
    total_coins, coins_used=make_change([1,5,10,25], change)
    coin = change
    while coin > 0:
        c=coins_used[coin]
        print c
        coin = coin - c