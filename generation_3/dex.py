#!/usr/bin/env python3
from utils import *
from os import system


parser = getParser()
args = parser.parse_args()

if args.pokemon:
  name = getName(args.pokemon)
  if not name:
    exit()
  query = 'SPECIES_' + name.upper()
  system('grep -A8 ' + query + ' pokeemerald/src/data/pokemon/species_info.h')
  system('grep ' + query + ' pokeemerald/src/data/pokemon/evolution.h')

  if args.evo or args.all:
    data = sh('cat pokeemerald/src/data/pokemon/level_up_learnsets.h')
    begin = data.find('s' + name.capitalize())
    end = data.find('LEVEL_UP_END', begin)
    print(data[begin:end])

  if args.all:
    data = sh('cat pokeemerald/src/data/pokemon/tmhm_learnsets.h')
    begin = data.find(query)
    end = data.find('} },', begin)
    print(data[begin:end])

    data = sh('cat pokeemerald/src/data/pokemon/tutor_learnsets.h')
    begin = data.find(query)
    end = data.find(',', begin)
    print(data[begin:end])

    data = sh('cat pokeemerald/src/data/pokemon/egg_moves.h')
    begin = data.find(name.upper())
    end = data.find(')', begin)
    print(data[begin:end])
elif args.move:
  system('grep -A11 MOVE_' + args.move.upper() + ' pokeemerald/src/data/battle_moves.h')
elif args.type:
  system('grep "^\\s*TYPE_' + args.type.upper() + '" pokeemerald/src/battle_main.c')
elif args.weak:
  system('grep ", TYPE_' + args.weak.upper() + '" pokeemerald/src/battle_main.c')
else:
  parser.print_help()
  exit()

