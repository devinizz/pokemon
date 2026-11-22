#!/usr/bin/env python3
from utils import *
from os import system

def getData(name):
  data = sh('cat pokecrystal/data/pokemon/base_stats/' + name + '.asm')
  data = data.split('\n')
  base = '\n'.join(data[:9] + data[12:-2])

  evos = sh('cat pokecrystal/data/pokemon/evos_attacks.asm')
  begin = evos.find(name.capitalize() + 'EvosAttacks:')
  end = evos.find('db 0 ; no more level', begin)

  egg = sh('cat pokecrystal/data/pokemon/egg_moves.asm')
  begin2 = egg.find(name.capitalize() + 'EggMoves:')
  end2 = egg.find('db -1 ; end', begin2)
  return base + '\n' + evos[begin:end] + '\n' + egg[begin2:end2]

parser = getParser()
args = parser.parse_args()

if args.pokemon:
  name = getName(args.pokemon)
  if not name:
    exit()
  data = getData(name)
  if args.show_move:
    move = set()
    for i in data.split():
      move.add(i + ('' if i[-1] == ',' else ','))
    for m in sorted(list(move)):
      system('grep "move ' + m + '" pokecrystal/data/moves/moves.asm')
  else:
    print(data)
elif args.move:
  print('name, effect, power, type, accuracy, pp, effect_percentage')
  system('grep "move ' + args.move.upper() + '" pokecrystal/data/moves/moves.asm')
elif args.type:
  system('grep "db ' + args.type.upper() + '" pokecrystal/data/types/type_matchups.asm')
elif args.weak:
  system('grep "db...............' + args.weak.upper() + '" pokecrystal/data/types/type_matchups.asm')
else:
  parser.print_help()
  exit()

