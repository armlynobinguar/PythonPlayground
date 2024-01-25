# basic_probability_concepts.py

import math

def event_probability(event_outcomes, sample_space):
    """
    Calculate the probability of an event.

    Parameters:
    event_outcomes (int): Number of favorable outcomes for the event.
    sample_space (int): Total number of outcomes in the sample space.

    Returns:
    float: Probability of the event.
    """
    probability = event_outcomes / sample_space
    return probability

def conditional_probability(event_a, event_b, both_ab):
    """
    Calculate the conditional probability of event A given event B.

    Parameters:
    event_a (float): Probability of event A.
    event_b (float): Probability of event B.
    both_ab (float): Probability of both event A and B occurring.

    Returns:
    float: Conditional probability of A given B.
    """
    return both_ab / event_b if event_b > 0 else 0

def probability_union(event_a, event_b, both_ab):
    """
    Calculate the probability of either event A or event B occurring.

    Parameters:
    event_a (float): Probability of event A.
    event_b (float): Probability of event B.
    both_ab (float): Probability of both event A and B occurring.

    Returns:
    float: Probability of either A or B.
    """
    return event_a + event_b - both_ab

def probability_complement(event):
    """
    Calculate the probability of the complement of an event.

    Parameters:
    event (float): Probability of the event.

    Returns:
    float: Probability of the event not occurring.
    """
    return 1 - event

# Example usage
if __name__ == "__main__":
    # Probability of rolling a 4 with a single six-sided die
    probability_dice = event_probability(1, 6)
    print(f"Probability of rolling a 4: {probability_dice:.2f}")

    # Conditional probability
    # Example: Probability of picking a red card given it's a heart in a deck of cards
    prob_heart = 1/4  # Probability of picking a heart
    prob_red = 1/2   # Probability of picking a red card
    prob_heart_and_red = 1/4  # Probability of picking a red heart
    prob_red_given_heart = conditional_probability(prob_heart, prob_red, prob_heart_and_red)
    print(f"Probability of picking a red card given it's a heart: {prob_red_given_heart:.2f}")

    # Probability of the union of two events
    # Example: Probability of picking a heart or a king from a deck of cards
    prob_king = 4/52  # Probability of picking a king
    prob_heart_or_king = probability_union(prob_heart, prob_king, prob_heart_and_red)
    print(f"Probability of picking a heart or a king: {prob_heart_or_king:.2f}")

    # Probability of the complement of an event
    # Example: Probability of not rolling a 4 on a six-sided die
    prob_not_four = probability_complement(probability_dice)
    print(f"Probability of not rolling a 4: {prob_not_four:.2f}")
