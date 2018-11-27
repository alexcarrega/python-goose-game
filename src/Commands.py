import cmd2

import Display
from Display import style_highlight as hl, style_prompt as prm, style_text as txt, style_head as head, ARROW, NOT, NEW_LINE
import Game
from Game import label
from Players import players

class Commands(cmd2.Cmd):
   prompt = f'{prm("goose-game")} {ARROW} '
   intro = NEW_LINE + head(f'Welcome to the {hl("The Goose Game Kata")}') + NEW_LINE

   doc_header = 'Available Commands (type help <topic> for more details)'

   def __init__(self):
      cmd2.Cmd.__init__(self,
         persistent_history_file='/tmp/python-goose-game.history',
         persistent_history_length=1000)

   @cmd2.with_argument_list
   def do_add(self, arg):
      TOKEN = "player"
      [token, name] = Commands._unpack(arg, 2)
      if token is None:
         Display.warn(f'Command {hl("add")} requires {hl("player")} <{hl("name")}>')
      elif not token == TOKEN:
         Display.error(f'Command {hl("add")} {hl(token)} unknown')
      elif name in players:
         Display.warn(f'{hl(name)}: already existing player')
      elif name is None:
         Display.error(f'Missing {hl("name")}')
      else:
         players[name] = 0
         Display.info(f'players: {", ".join([f"{hl(p)}" for p in players.keys()])}')

   def help_add(self):
      dinfo('\n'.join([hl('add player <name>'), 'Add a new player to the game is not already present', ]))

   def complete_add(self, text, line, bedidx, endidx):
      TOKEN = 'player'
      num_pos_arg = Commands._num_pos_arg(line)
      if not text and num_pos_arg == 0:
         return [TOKEN]
      elif text and num_pos_arg == 1:
         return [TOKEN] if TOKEN.startswith(text) else []

   @cmd2.with_argument_list
   def do_move(self, arg):
      [player_name, roll1, roll2] = Commands._unpack(arg, 3)
      player_label = hl(player_name)
      if player_name in players:
         roll1 = Commands._checkRoll(roll1, 'roll1')
         roll2 = Commands._checkRoll(roll2, 'roll2')
         if roll1 is not None and roll2 is not None:
            Display.text(Game.action(player_name, roll1, roll2))
      else:
         Display.error(f'Player {player_label} {NOT} found')

   def help_move(self):
      Display.info('\n'.join(['move <player-name> [rool1] [roll2]',
         'Make a move of player-name with the optional rool1 and roll2.',
         'If the rolls are not provided they are computed randomly' ]))

   def complete_move(self, text, line, bedidx, endidx):
      num_pos_arg = Commands._num_pos_arg(line)
      if not text and num_pos_arg == 0:
         return players.keys()
      elif text and num_pos_arg == 1:
         return [
            player
               for player in players.keys()
                  if player.startswith(text)
         ]
      elif not text and num_pos_arg < 3:
         return [ str(r) for r in range(1, 7)]
      else:
         return []

   def do_exit(self, line):
      Display.text('Bye!!!')
      return True

   def help_exit(self):
      Display.info('\n'.join([head('exit'), f'Exit from the game', ]))

   @staticmethod
   def _unpack(arg, num):
      return (arg + [None] * num)[:num]

   @staticmethod
   def _endswith(line, what):
      return line.strip().endswith(what)

   @staticmethod
   def _num_pos_arg(line):
      return line.strip().count(' ')

   @staticmethod
   def _checkRoll(roll, key):
      updRoll = Game.randomRoll() if roll == None else int(roll)
      if updRoll < 1 or updRoll > 6:
         Display.error(f'{hl(key)} value {NOT} valid: {updRoll}. Must be between {hl(1)} and {hl(6)}')
         return None
      else:
         return updRoll
