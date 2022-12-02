# Define a dictionary that maps each hand shape to its corresponding score
HAND_SHAPES = {
  "Rock": 1,
  "Paper": 2,
  "Scissors": 3,
}

# Define a dictionary that maps each outcome to its corresponding score
OUTCOMES = {
  "Win": 6,
  "Loss": 0,
  "Draw": 3,
}

# Define a dictionary that maps each hand shape to the hand shape it defeats
DEFEATS = {
  "Rock": "Scissors",
  "Paper": "Rock",
  "Scissors": "Paper",
}

# Define a function that calculates the score for a round given the choices of each player
# and the outcome of the round
def calculate_score(opponent_choice, player_choice, outcome):
  # Calculate the score for the player's choice
  player_score = HAND_SHAPES[player_choice]

  # Calculate the score for the outcome of the round
  outcome_score = OUTCOMES[outcome]

  # Return the total score for the round
  return player_score + outcome_score

# Define the strategy guide
strategy_guide = [
  ["A", "Y"],
  ["B", "X"],
  ["C", "Z"],
]

# Define a variable to keep track of the total score
total_score = 0

# Go through each round in the strategy guide
for round in strategy_guide:
  # Determine the opponent's choice and the player's choice
  opponent_choice = round[0]
  player_choice = round[1]

  # Determine the outcome of the round
  if opponent_choice == player_choice:
    # If both players chose the same hand shape, the round ends in a draw
    outcome = "Draw"
  elif DEFEATS[opponent_choice] == player_choice:
    # If the opponent's choice defeats the player's choice, the player loses the round
    outcome = "Loss"
  else:
    # Otherwise, the player wins the round
    outcome = "Win"

  # Calculate the score for the round
  round_score = calculate_score(opponent_choice, player_choice, outcome)

  # Add the score for the round to the total score
  total_score += round_score

# Print the total score
print(total_score)
