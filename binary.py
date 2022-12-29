from sys import exit as specexit
from os import system

while True:
  resl = [0, 0, 0, 0, 0, 0, 0, 0]

  try:
    num = int(input("number (max 255): "))
  except ValueError:
    print('a NUMBER, bro')
    continue

  if num > 255:
    print("too big, sorry")
    specexit(1)

  if num >= 128:
    num -= 128
    resl[0] = 1

  if num >= 64:
    num -= 64
    resl[1] = 1

  if num >= 32:
    num -= 32
    resl[2] = 1

  if num >= 16:
    num -= 16
    resl[3] = 1

  if num >= 8:
    num -= 8
    resl[4] = 1

  if num >= 4:
    num -= 4
    resl[5] = 1

  if num >= 2:
    num -= 2
    resl[6] = 1

  if num >= 1:
    num -= 1
    resl[7] = 1

  print(f"your binary code is {''.join(str(bit) for bit in resl)}")
  again = input("run again? (y/N) ")
  if again.strip() in ("y", "n", ""):
    if again == "y":
      system('clear || cls')
      continue
    else:
      break

specexit(0)
# made really lazily, so it sucks.
## i've just learnt there's a `bin()` function.
## hooray.
