import random


class Exchange(object):

    def __init__(self):
        self.name = 'casino'
        self.all_markets = []

    def generate_market(self, name):
        market = Market(name=name)
        market.generate_assets(5)
        market.update_assets()
        self.all_markets.append(market)


class Market(object):

    def __init__(self, name=''):
        self.name = name
        self.asset_list = []

    def generate_assets(self, num=10):
        # if num == 1:
        #     s, p, v = input('symbol, price, volatility: ').split(',')
        #     asset = Asset(symbol=s, price=int(p), volatility=int(v))
        #     self.asset_list.append(asset)
        # else:
        for _ in range(num):
            asset = Asset()
            asset.set_attributes()
            self.asset_list.append(asset)

    def update_assets(self, steps=300):
        for asset in self.asset_list:
            for _ in range(steps):
                asset.update_price()

    def display_assets(self):
        print()
        print('symbol, price, volatility')
        tmp = ' {0}    {1}      {2}'
        for asset in self.asset_list:
            print(tmp.format(asset.symbol, asset.price, asset.volatility))

    def get_price_history(self):
        return [asset.pricehistory for asset in self.asset_list]


class Asset(object):
                                                # set manually
    def __init__(self, symbol='AAAA', price=100, volatility=2):
        self.symbol = symbol
        self.price = price
        self.volatility = volatility
        self.price_history = []

    def set_price(self, price=0, stop=300):

        if price:
            self.price = price
        else:
            self.price = random.randrange(1, stop + 1)

    def set_symbol(self, symbol=''):

        if symbol:
            self.symbol = symbol
        else:
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            self.symbol = ''.join(random.choice(alphabet)
                                  for _ in range(4))  # manually set

    def set_volatility(self, volatility=0):

        if volatility:
            self.volatility = volatility
        else:
            chance = random.randint(1, 10)

            if chance <= 7:                     # 7 and volatility ranges
                roll = random.randint(1, 10)    # manually set
            else:
                roll = random.randint(10, 40)

            self.volatility = roll

    def set_attributes(self, price=0, symbol='', volatility=0):
        self.set_price(price)
        self.set_symbol(symbol)
        self.set_volatility(volatility)

    def update_price(self):
        chance = random.randint(0, 10)

        if chance > 5:
            move = random.randrange(self.volatility)
        elif chance < 5:
            move = -random.randrange(self.volatility)
        else:
            move = 0

        self.price += move

        if self.price < 0:
            self.price = 0

        self.price_history.append(self.price)