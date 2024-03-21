import random
from collections import Counter
import matplotlib.pyplot as plt

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def monte_carlo_simulation(num_trials):
    results = Counter([roll_dice() for _ in range(num_trials)])
    probabilities = {key: value / num_trials * 100 for key, value in results.items()}
    return probabilities

def plot_probabilities(probabilities):
    sorted_probabilities = sorted(probabilities.items())
    plt.bar([item[0] for item in sorted_probabilities], [item[1] for item in sorted_probabilities])
    plt.xlabel('Сума')
    plt.ylabel('Імовірність(%)')
    plt.title('Імовірність сум при киданні двох кубиків')
    plt.xticks(range(2, 13))
    plt.show()

if __name__ == "__main__":
    num_trials = 1000000
    probabilities = monte_carlo_simulation(num_trials)

    sorted_probabilities = sorted(probabilities.items())
    for key, value in sorted_probabilities:
        print(f'Сума {key}: {value:.2f}% ({value / 100:.2f})')

    plot_probabilities(probabilities)
