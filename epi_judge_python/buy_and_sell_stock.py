from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    max_profit = 0
    minimum_price_so_far = float('inf')
    for price in prices:
        daily_profit = price - minimum_price_so_far
        max_profit = max(max_profit, daily_profit)
        minimum_price_so_far = min(minimum_price_so_far, price)

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
