#! /bin/bash

INPUT=$1

if ! [[ "$INPUT" =~ ^d[0-9]+p(1|2)$ ]]; then
  echo "Can't parse input. Should be something like 'd3p1'."
  exit
fi

DAY="day${INPUT:1:1}"
PART="part_${INPUT:3:1}"

python3 ${DAY}/${PART}.py < ${DAY}/example.txt
