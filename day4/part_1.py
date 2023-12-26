import utils

def main():

  cards = utils.parse_cards()
  result = count_points(cards)

  print(result)


def count_points(cards):

  points = 0

  for winning, mine in cards:

    matches = len(mine.intersection(winning))

    if matches > 0:
      points += 2**(matches - 1)

  return points


main()
