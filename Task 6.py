def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item_name, item_data in sorted_items:
        if total_cost + item_data['cost'] <= budget:
            total_cost += item_data['cost']
            total_calories += item_data['calories']
            selected_items.append(item_name)

    return {'selected_items': selected_items, 'total_cost': total_cost, 'total_calories': total_calories}


def dynamic_programming(items, budget):
    dp_table = [[0] * (budget + 1) for _ in range(len(items) + 1)]

    for i, (item_name, item_data) in enumerate(items.items(), 1):
        for w in range(1, budget + 1):
            if item_data['cost'] <= w:
                dp_table[i][w] = max(dp_table[i - 1][w], dp_table[i - 1][w - item_data['cost']] + item_data['calories'])
            else:
                dp_table[i][w] = dp_table[i - 1][w]

    selected_items = []
    total_calories = dp_table[len(items)][budget]

    w = budget
    for i in range(len(items), 0, -1):
        if total_calories <= 0:
            break
        if total_calories != dp_table[i - 1][w]:
            selected_items.append(list(items.keys())[i - 1])
            total_calories -= items[list(items.keys())[i - 1]]['calories']
            w -= items[list(items.keys())[i - 1]]['cost']

    return {'selected_items': selected_items, 'total_cost': budget - w, 'total_calories': dp_table[len(items)][budget]}


# Приклад використання:
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 150

greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

print("Greedy Algorithm Result:")
print(greedy_result)

print("\nDynamic Programming Result:")
print(dp_result)
