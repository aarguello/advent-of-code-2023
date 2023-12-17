import sys

def parse_games():

  games = []
  lines = [ l.strip() for l in sys.stdin.readlines() ]

  for line in lines:
    subsets = line.split(': ')[1].split('; ')
    game = parse_game(subsets)
    games.append(game)

  return games


def parse_game(subsets):

  game = []

  for raw_subset in subsets:
    subset = {}
    for cube in raw_subset.split(', '):
      amount, color = cube.split()
      subset[color] = int(amount)
    game.append(subset)

  return game
