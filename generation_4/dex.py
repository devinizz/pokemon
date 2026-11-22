#!/usr/bin/env python3
from utils import *
from os import system

parser = getParser()
args = parser.parse_args()

if args.pokemon:
  name = getName(args.pokemon)
  if not name:
    exit()
  data = sh('cat pokeplatinum/res/pokemon/' + name.lower() + '/data.json')

  if args.all:
    begin = data.find('learnset')
    end = data.find('evolutions')
    print(data[begin:end])
  elif args.evo:
    begin = data.find('learnset')
    end = data.find('by_tm')
    print(data[begin:end])
  else:
    end = data.find('safari_flee_rate')
    print(data[:end])
    begin = data.find('evolutions')
    end = data.find('offspring')
    print(data[begin:end])

elif args.move:
  move = sh('grep MOVE_' + args.move.upper() + ' pokeplatinum/generated/moves.txt').split()[0][5:]
  system('cat pokeplatinum/res/battle/moves/' + move.lower() + '/data.json')
elif args.type:
  system('grep "{ TYPE_' + args.type.upper() + '" pokeplatinum/src/battle/battle_lib.c')
elif args.weak:
  system('grep ", TYPE_' + args.weak.upper() + '," pokeplatinum/src/battle/battle_lib.c')
else:
  parser.print_help()
  exit()

