def calculate_batting_points(player):
    points = 0

    # adding points for score
    points += player['runs'] // 2

    # add points for half-centuary and centuary
    if player['runs'] >= 100:
        points += 10
    elif player['runs'] >= 50:
        points += 10
    
    # points based on strike rate
    strike_rate = player['runs'] / player['balls'] * 100
    if 80 <= strike_rate <= 100:
        points += 2
    elif strike_rate > 100:
        points += 4
    
    points += player['4']*1 + player['6']*2

    return points


def calculate_bowling_points(player):
    points = 0
    # Add points for each wicket
    points += player['wkts'] * 10
    
    # Additional points for wickets taken
    if player['wkts'] >= 5:
        points += 10
    elif player['wkts'] >= 3:
        points += 5
    
    # Points based on economy rate
    economy_rate = player['runs'] / player['overs']
    if 3.5 <= economy_rate <= 4.5:
        points += 4
    elif 2 <= economy_rate < 3.5:
        points += 7
    elif economy_rate < 2:
        points += 10
    
    # Points for fielding actions
    points += player['field'] * 10
    
    return points


