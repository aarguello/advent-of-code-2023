import utils

capacity = {
  'red': 12,
  'green': 13,
  'blue': 14,
}

def main():

  games = utils.parse_games()
  result = 0

  for index, game in enumerate(games):
    if is_valid(game):
      result += (index + 1)

  print(result)


def is_valid(game):

  for subset in game:
    for color, count in subset.items():
      if count > capacity[color]:
        return False

  return True


main()
