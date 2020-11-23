import random


def k6():
  return random.randint(1,7)

def elsoguritas():
  return [k6(),k6(),k6(),k6(),k6()]


def masodikguritas(helyzet,ujra):
  for kocka in ujra:
      helyzet[kocka]=k6()
