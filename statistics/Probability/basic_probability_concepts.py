# basic_probability_concepts.py

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

def coin_flip_probability(heads_count, total_flips):
    """
    Calculate the probability of getting a specific number of heads in coin flips.

    Parameters:
    heads_count (int): Desired number of heads.
    total_flips (int): Total number of coin flips.

    Returns:
    float: Probability of getting the specified number of heads.
    """
    from math import factorial

    def nCr(n, r):
        return factorial(n) / (factorial(r) * factorial(n - r))

    # Assuming a fair coin
    sample_space = 2 ** total_flips
    event_outcomes = nCr(total_flips, heads_count)
    return event_probability(event_outcomes, sample_space)

# Example usage
if __name__ == "__main__":
    # Probability of rolling a 4 with a single six-sided die
    probability_dice = event_probability(1, 6)
    print(f"Probability of rolling a 4: {probability_dice:.2f}")

    # Probability of getting 2 heads in 3 coin flips
    probability_coin = coin_flip_probability(2, 3)
    print(f"Probability of getting 2 heads in 3 coin flips: {probability_coin:.2f}")
