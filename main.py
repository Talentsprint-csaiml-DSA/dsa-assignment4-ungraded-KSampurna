# stable_marriage.py

def stable_marriage(n, boy_preferences, girl_preferences):
    # TODO: Implement the Gale-Shapley algorithm

    # Create a ranking dictionary for each girl
    girl_rankings = [
        {boy: rank for rank, boy in enumerate(pref)} for pref in girl_preferences
    ]

    # Initialize the status of boys and girls
    free_boys = list(range(1, n + 1))  # List of free boys
    boy_partners = [-1] * n           # Partner of each boy, -1 means unmatched
    girl_partners = [-1] * n          # Partner of each girl, -1 means unmatched
    next_proposal = [0] * n           # Tracks next girl each boy will propose to

    # Gale-Shapley algorithm
    while free_boys:
        boy = free_boys.pop(0)  # Pick the first free boy
        girl_index = next_proposal[boy - 1]  # Get the next girl to propose to
        girl = boy_preferences[boy - 1][girl_index]  # Get the girl's number
        next_proposal[boy - 1] += 1  # Increment boy's proposal index

        if girl_partners[girl - 1] == -1:  # If the girl is free
            # Engage the boy and the girl
            boy_partners[boy - 1] = girl
            girl_partners[girl - 1] = boy
        else:
            # The girl is currently matched; check if she prefers the new proposer
            current_partner = girl_partners[girl - 1]
            if girl_rankings[girl - 1][boy] < girl_rankings[girl - 1][current_partner]:
                # Girl prefers the new boy; update partnerships
                boy_partners[current_partner - 1] = -1  # Current partner becomes free
                free_boys.append(current_partner)      # Add current partner back to free boys

                # Engage the new boy and the girl
                boy_partners[boy - 1] = girl
                girl_partners[girl - 1] = boy
            else:
                # Girl prefers her current partner; reject the boy
                free_boys.append(boy)  # Boy remains free

    # Format the result as a list of tuples
    result = [(boy + 1, boy_partners[boy]) for boy in range(n)]
    return result


# Example usage
if __name__ == "__main__":
    n = 3
    boy_preferences = [[1, 2, 3], [2, 1, 3], [1, 2, 3]]
    girl_preferences = [[2, 1, 3], [1, 3, 2], [3, 1, 2]]

    result = stable_marriage(n, boy_preferences, girl_preferences)
    print("Stable Marriage Matching:", result)
  
