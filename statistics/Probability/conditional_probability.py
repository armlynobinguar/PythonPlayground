# conditional_probability.py

def conditional_probability(event_a_prob, event_b_given_a_prob):
    """
    Calculate the conditional probability of event B given event A.

    Parameters:
    event_a_prob (float): Probability of event A.
    event_b_given_a_prob (float): Probability of event B given A has occurred.

    Returns:
    float: Conditional probability of event B given A.
    """
    return event_a_prob * event_b_given_a_prob

# Example 1: Probability of drawing a red card given that it's a heart
prob_heart = 13/52  # There are 13 hearts in a deck of 52 cards
prob_red_given_heart = 1  # All hearts are red
prob_red_if_heart = conditional_probability(prob_heart, prob_red_given_heart)
print(f"Example 1: Probability of drawing a red card given it's a heart: {prob_red_if_heart:.2f}")

# Example 2: Probability of testing positive for a disease given having the disease
prob_disease = 0.01  # Let's say 1% of the population has the disease
prob_positive_given_disease = 0.95  # Test is 95% accurate
prob_positive_if_disease = conditional_probability(prob_disease, prob_positive_given_disease)
print(f"Example 2: Probability of testing positive given having the disease: {prob_positive_if_disease:.2f}")

# Example 3: Probability of it raining given that it's cloudy
prob_cloudy = 0.3  # Assume there's a 30% chance of any day being cloudy
prob_rain_given_cloudy = 0.5  # 50% chance of rain on a cloudy day
prob_rain_if_cloudy = conditional_probability(prob_cloudy, prob_rain_given_cloudy)
print(f"Example 3: Probability of rain given it's cloudy: {prob_rain_if_cloudy:.2f}")

# Example 4: Probability of a computer being infected with a virus given it's running slow
prob_slow = 0.2  # Assume 20% of computers run slow
prob_virus_given_slow = 0.1  # 10% chance that a slow computer is infected with a virus
prob_virus_if_slow = conditional_probability(prob_slow, prob_virus_given_slow)
print(f"Example 4: Probability of a computer virus given a slow computer: {prob_virus_if_slow:.2f}")

# Example 5: Probability of a student passing an exam given that they have studied
prob_studied = 0.8  # Assume 80% of students studied for the exam
prob_pass_given_studied = 0.9  # 90% chance of passing if studied
prob_pass_if_studied = conditional_probability(prob_studied, prob_pass_given_studied)
print(f"Example 5: Probability of passing an exam given studying: {prob_pass_if_studied:.2f}")
