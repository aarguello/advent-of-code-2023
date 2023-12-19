import sys

digits_map = {
  '1': '1', 'one': '1',
  '2': '2', 'two': '2',
  '3': '3', 'three': '3',
  '4': '4', 'four': '4',
  '5': '5', 'five': '5',
  '6': '6', 'six': '6',
  '7': '7', 'seven': '7',
  '8': '8', 'eight': '8',
  '9': '9', 'nine': '9',
}

def main():

  calibration_documents = [ l.strip() for l in sys.stdin.readlines() ]
  result = 0

  for document in calibration_documents:
    first_digit = get_first_digit(document)
    last_digit = get_last_digit(document)
    result += int(first_digit + last_digit)

  print(result)


def get_first_digit(document):
  for i in range(len(document)):
    for word, digit in digits_map.items():
      if document[i:].startswith(word):
        return digit


def get_last_digit(document):
  for i in range(len(document)):
    for word, digit in digits_map.items():
      if document[0:len(document) - i].endswith(word):
        return digit


main()
