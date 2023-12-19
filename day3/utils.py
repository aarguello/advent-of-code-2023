
def get_numbers_positions(engine):

  numbers = []

  rows = len(engine)
  cols = len(engine[0])

  for i in range(rows):
    for j in range(cols):
      value = get_number_at_position(engine, i, j)
      if value:
        numbers.append((i, j, value))

  return numbers


def get_number_at_position(engine, i, j):

  if not engine[i][j].isdigit():
    return None

  # Make sure first digit is at (i, j)
  if j > 0 and engine[i][j - 1].isdigit():
    return None

  value, k = "", 0

  while is_valid_position(engine, i, j + k) and engine[i][j + k].isdigit():
    value += engine[i][j + k]
    k += 1

  return value


def get_borders(engine, start_position, length = 1):

  i, j = start_position
  borders = []

  # Above and below
  for k in range(j - 1, j + length + 1):
    borders.append((i - 1, k))
    borders.append((i + 1, k))

  # Left and right
  borders.append((i, j - 1))
  borders.append((i, j + length))

  return [ pos for pos in borders if is_valid_position(engine, *pos) ]


def is_valid_position(engine, i, j):
  return (
    0 <= i < len(engine) and
    0 <= j < len(engine[0])
  )
