import sys, utils

engine = [ l.strip() for l in sys.stdin.readlines() ]

def main():

  result = 0
  numbers = utils.get_numbers_positions(engine)

  for i, j, value, in numbers:
    if is_part_number((i, j), value):
      result += int(value)

  print(result)


def is_part_number(position, value):

  borders = utils.get_borders(engine, position, len(value))

  return any(
    is_symbol(i, j) for i, j in borders
  )


def is_symbol(i, j):
  return engine[i][j] != '.' and not engine[i][j].isdigit()


main()
