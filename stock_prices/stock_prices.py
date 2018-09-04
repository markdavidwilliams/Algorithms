#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = -200
  for i in range(1, len(prices)):
      buying_price = prices[i-1]
      for j in range(i, len(prices)):
          if -buying_price + prices[j] > max_profit:
              max_profit = -buying_price + prices[j]
  return max_profit


if __name__ == '__main__':
  # You can test your implementation by running 
  # `python stock_prices.py [prices]` where prices is comprised of
  # space-separated integer values
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))