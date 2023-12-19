import math, utils

def main():

  games = utils.parse_games()
  result = 0

  for game in games:
    fewest = get_fewest_cubes(game)
    result += get_cubes_power(fewest)

  print(result)


def get_fewest_cubes(game):

  fewest = { 'red': 0, 'green': 0, 'blue': 0 }

  for subset in game:
    for color, amount in fewest.items():
      if color in subset:
        fewest[color] = max(subset[color], amount)

  return fewest


def get_cubes_power(cubes):
  return math.prod(cubes.values())


main()
