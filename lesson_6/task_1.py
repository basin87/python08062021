def join_dict(x, y):
    united_dict = dict(zip(x, y))
    return united_dict


coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')
print(join_dict(coin, code))