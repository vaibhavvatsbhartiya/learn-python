from scoring import calculate_batting_points, calculate_bowling_points

# Player data
players = [
    {'name': 'Virat Kohli', 'role': 'bat', 'runs': 112, '4': 10, '6': 0, 'balls': 119, 'field': 0},
    {'name': 'du Plessis', 'role': 'bat', 'runs': 120, '4': 11, '6': 2, 'balls': 112, 'field': 0},
    {'name': 'Bhuvneshwar Kumar', 'role': 'bowl', 'wkts': 1, 'overs': 10, 'runs': 71, 'field': 1},
    {'name': 'Yuzvendra Chahal', 'role': 'bowl', 'wkts': 2, 'overs': 10, 'runs': 45, 'field': 0},
    {'name': 'Kuldeep Yadav', 'role': 'bowl', 'wkts': 3, 'overs': 10, 'runs': 34, 'field': 0}
]

# Calculate and store each player's score
results = []
for player in players:
    if player['role'] == 'bat':
        score = calculate_batting_points(player)
        results.append({'name': player['name'], 'bat_score': score})
    elif player['role'] == 'bowl':
        score = calculate_bowling_points(player)
        results.append({'name': player['name'], 'bowl_score': score})

# Print each player's score
for result in results:
    print(result)
