import sys
import day3_utils as utils

engine = [ l.strip() for l in sys.stdin.readlines() ]

def main():

  result = 0

  gears_positions = get_gears_positions()
  gears_by_number = get_gears_by_number()

  for gear in gears_positions:

    numbers_around_gear = []

    for number, gears in gears_by_number:
      if gear in gears:
        numbers_around_gear.append(number)

    if len(numbers_around_gear) == 2:
      result += int(numbers_around_gear[0]) * int(numbers_around_gear[1])

  print(result)


def get_gears_positions():

  gears_positions = []

  rows = len(engine)
  cols = len(engine[0])

  for i in range(rows):
    for j in range(cols):
      if is_gear(i, j):
        gears_positions.append((i, j))

  return gears_positions


def get_gears_by_number():

  gears_by_number = []
  numbers = utils.get_numbers_positions(engine)

  for i, j, value in numbers:
    borders = utils.get_borders(engine, (i, j), len(value))
    gears = [ (i, j) for (i, j) in borders if is_gear(i, j) ]
    gears_by_number.append((value, gears))

  return gears_by_number


def is_gear(i, j):
  return engine[i][j] == '*'


main()
