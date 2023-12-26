import sys

def parse_cards():

  cards = []
  raw_cards = [ line.strip() for line in sys.stdin.readlines() ]

  for raw_card in raw_cards:
    winning, mine = raw_card.split(':')[1].split('|')
    cards.append((
      set(winning.split()),
      set(mine.split()),
    ))

  return cards
