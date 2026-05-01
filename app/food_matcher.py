from difflib import get_close_matches

def match_food(food_name, database_names):

    matches = get_close_matches(
        food_name.lower(),
        [name.lower() for name in database_names],
        n=1,
        cutoff=0.6
    )

    if matches:

        matched = matches[0]

        for original in database_names:

            if original.lower() == matched:
                return original

    return None