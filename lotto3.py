import random

def determine_draft_order(teams_with_odds):
    # list the teams and their total balls
    teams = list(teams_with_odds.keys())
    odds = list(teams_with_odds.values())

    # define a the draft order and sort out the team picked
    draft_order = []
    remaining_teams = teams.copy()  # teams that didn't have balls picked

    while remaining_teams:
        # Draw a team based on their odds (weights)
        chosen_team = random.choices(remaining_teams, weights=[teams_with_odds[team] for team in remaining_teams], k=1)[0]
        draft_order.append(chosen_team)
        remaining_teams.remove(chosen_team)  # Remove the selected team from the pool

    return draft_order

def reveal_draft_order(draft_order):
    # Reveal the draft order in reverse
    print("\nThe suspense is building...\n")
    for i in range(7, -1, -1):
        input(f"Press Enter to reveal pick number {i+1}...")  # Wait for user to press Enter
        print(f"Pick number {i+1}: {draft_order[i]}")
    
    # After revealing number 1, congratulate the first pick
    print(f"\nCongratulations to {draft_order[0]} with the #1 pick!\n")

# Enter total balls here
teams_with_odds = {
    "Carolina": 200, 
    "teapester725": 475,
    "Step Burrow I'm Stuck": 150, 
    "Griddy Up Owned By Step": 125, 
    "RomeO and Juwan": 175, 
    "3 Yard Monty": 140,  
    "Cheddarheads": 100, 
    "Berchild05 Owned by Step": 235 
}

# Determine the draft order
draft_order = determine_draft_order(teams_with_odds)

# Start the reveal process
reveal_draft_order(draft_order)

