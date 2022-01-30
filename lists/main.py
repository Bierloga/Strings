# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
def alphabetical_order (movie_list):
    return movie_list.sort()

def won_golden_globe (film, movie_list):
    if film in movie_list:
        return True
    else:
        return False

