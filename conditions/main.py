# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line


def farm_action(weather, time_of_day, need_milking, location, season, slurry_tank_full, grass_status):
    if location == 'pasture' and weather == 'rainy':
        print('take cows to cowshed')
    elif need_milking == True:
        if location == 'cowshed':
            print('milk cows')
        else:
            print('"""take cows to cowshed')
            print('milk cows')
            print('take cows back to pasture"""')
    elif slurry_tank_full == True and weather != 'sunny' and weather != 'windy':
        if location == 'cowshed':
            print('fertilize_pasture')
        else:
            print(
                '"""take cows to cowshed\nfertilize_pasture\ntake cows back to pasture"""')
    elif grass_status == True and season == 'spring' and weather == 'sunny':
        if location == 'cowshed':
            print('mow grass')
        else:
            print('take cows to shed\nmow grass\ntake cows back to pasture')
    else:
        print('wait')


farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)
