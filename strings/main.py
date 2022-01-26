# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = scorer_1 + " "+str(goal_0)+", "+scorer_2+" "+str(goal_1)
report = f'{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute'
player = scorer_1
space = player.find(" ")
first_name = player[:space]
last_name_len = len(player[space+1:])
name_short = f'{first_name[0]}. {player[-last_name_len:]}'
chant = (f'{first_name}! ')*(len(first_name)-1)+f'{first_name}!'
good_chant = chant[-1] != " "

