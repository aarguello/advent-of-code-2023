import utils

cache = {}

def main():

  cards = utils.parse_cards()
  result = sum([ count_card(cards, i) for i in range(len(cards)) ])

  print(result)


def count_card(cards, index):

  if not index in cache:

    winning, mine = cards[index]
    matches = len(mine.intersection(winning))

    total = 1

    for i in range(index + 1, index + 1 + matches):
      total += count_card(cards, i)

    cache[index] = total

  return cache[index]


main()
