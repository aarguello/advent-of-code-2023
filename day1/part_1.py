import sys

def main():

  calibration_documents = [ l.strip() for l in sys.stdin.readlines() ]
  result = 0

  for document in calibration_documents:
    first_digit = next(char for char in document if char.isdigit())
    last_digit = next(char for char in reversed(document) if char.isdigit())
    result += int(first_digit + last_digit)

  print(result)


main()
