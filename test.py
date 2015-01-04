import sim


def test_market():
    chemical_sector = sim.Market()
    chemical_sector.generate_assets()

    for asset in chemical_sector.asset_list:
        print(asset.symbol, asset.price, asset.volatility)

    print()
    print('starting...')
    for asset in chemical_sector.asset_list:
        print('-' * 10)
        print(asset.symbol)
        for x in range(10):
            print(asset.price)
            asset.update_price()

    for asset in chemical_sector.asset_list:
        print(asset.symbol, asset.price, asset.volatility)


def test_asset():
    asset = sim.Asset()
    # print(asset.symbol)
    start = asset.price

    asset.set_volatility()
    # print(asset.volatility)

    tmp = []

    for _ in range(1000000):
        print(asset.price)
        asset.update_price()
        tmp.append(asset.price)

    print('start:', start)
    print('volatility:', asset.volatility)
    print('avg:', sum(tmp) / len(tmp))

#test_asset()


def test_interface():
    main = sim.Exchange()

    main.generate_market('chemical_sector')

    new_market = main.all_markets['chemical_sector']
    new_market.generate_assets()
    new_market.display_assets()

    for x in range(10):
        new_market.update_assets()
        new_market.update_assets()
        new_market.update_assets()

    return new_market


def new_test():
    x = sim.Market()

    x.generate_assets(5)

    x.display_assets()
    x.update_assets()
    x.display_assets()
    print()


def interface():
    market = sim.Market()
    market.generate_assets(5)
    while True:
        market.update_assets()  # generates 5 but returns 1 price_history
        asset_data = market.asset_list[0].price_history
        yield asset_data


