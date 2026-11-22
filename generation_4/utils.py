from subprocess import check_output
from argparse import ArgumentParser

def getParser():
  parser = ArgumentParser()
  parser.add_argument('--pokemon', '-p', type = str, help = 'pm id/name')
  parser.add_argument('--evo', '-e', action = 'store_true',
      help = "combine with -p, to show evo moves")
  parser.add_argument('--all', '-a', action = 'store_true',
      help = "combine with -p, to show tmhm, tutor, egg moves")
  parser.add_argument('--move', '-m', type = str, help = 'move name')
  parser.add_argument('--type', '-t', type = str, help = 'show type matchup')
  parser.add_argument('--weak', '-w', type = str, help = 'show type weakness')
  return parser

def sh(cmd):
  return check_output(cmd, shell = True).decode()

def getName(x):
  try:
    x = sh('grep -m1 SPECIES_' + x.upper() + ' pokeplatinum/generated/species.txt').split()[0][8:]
  except:
    print('Can not find pokemon', x)
    x = ''
  return x.lower()
