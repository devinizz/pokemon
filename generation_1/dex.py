#!/usr/bin/env python3
from utils import *
from os import system

def getData(name):
  data = sh('cat pokered/data/pokemon/base_stats/' + name + '.asm')
  data = data.split('\n')
  base = '\n'.join(data[:9] + data[12:-2])

  evos = sh('cat pokered/data/pokemon/evos_moves.asm')
  begin = evos.find(name.capitalize() + 'EvosMoves:')
  end = evos.find('db 0\n\n', begin)
  return base + '\n' + evos[begin:end]

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
      system('grep "move ' + m + '" pokered/data/moves/moves.asm')
  else:
    print(data)
elif args.move:
  print('name, effect, power, type, accuracy, pp')
  system('grep "move ' + args.move.upper() + '" pokered/data/moves/moves.asm')
elif args.type:
  system('grep "db ' + args.type.upper() + '" pokered/data/types/type_matchups.asm')
elif args.weak:
  system('grep "db...............' + args.weak.upper() + '" pokered/data/types/type_matchups.asm')
else:
  parser.print_help()
  exit()

