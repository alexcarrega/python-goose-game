import random

from Players import players

from Display import style_highlight as hl

START = 0
GOAL = 63
THE_BRIDGE = 6
THE_BRIDGE_JUMP = 12
THE_GOOSE = [5, 9, 14, 18, 23, 27]

START_LABEL = hl('Start')
THE_BRIDGE_LABEL = f'{hl("The")} {hl("Bridge")}'
THE_GOOSE_LABEL = f'{hl("The")} {hl("Goose")}'
GOAL_LABEL = hl(GOAL)
WIN_LABEL = hl('Wins!!')

def label(player_pos):
   if player_pos == START:
      return hl('Start')
   elif player_pos == THE_BRIDGE:
      return THE_BRIDGE_LABEL
   elif player_pos in THE_GOOSE:
      return f'{hl(player_pos)}, {hl("The")} {hl("Goose")}'
   else:
      return f'{hl(player_pos)}'

def action(player_name, roll1, roll2):
   player_label = hl(player_name)
   player_pos_orig = players[player_name]
   player_pos = player_pos_orig
   output = f'{player_label} rolls {hl(roll1)}, {hl(roll2)}. {player_label} moves from {label(player_pos)} to '
   player_pos += roll1 + roll2
   continue_turn = True
   while continue_turn:
      if player_pos == THE_BRIDGE:
         output += f'{THE_BRIDGE_LABEL}. {player_label} jumps to '
         player_pos = THE_BRIDGE_JUMP
      elif player_pos in THE_GOOSE:
         output += f'{label(player_pos)}. {player_label} moves again and goes to '
         player_pos += roll1 + roll2
      elif player_pos == GOAL:
         output += f'{GOAL_LABEL}. {player_label} {WIN_LABEL}'
         continue_turn = False
      elif player_pos > GOAL:
         player_pos = GOAL - (player_pos - GOAL)
         output += f'{GOAL_LABEL}. {player_label} bounces! {player_label} returns to '
      else:
         output += label(player_pos)
         continue_turn = False
   players[player_name] = player_pos
   for other_player_name in players.keys():
      if (other_player_name != player_name and players[other_player_name] == player_pos):
         output += f'. On {label(player_pos)} there is {label(other_player_name)}, who returns to {label(player_pos_orig)}'
         players[other_player_name] = player_pos_orig
         return output
   return output

def randomRoll():
   return random.randint(1, 6)
