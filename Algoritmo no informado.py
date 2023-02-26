def knapsack(capacity, weights, values):
    n = len(weights)
    best_value = 0
    best_selection = [(values[i], weights[i], False) for i in range(n)]
    
    def explore(i, value, weight, selection):
        nonlocal best_value, best_selection
        
        if i == n:
            if value > best_value:
                best_value = value
                best_selection = selection.copy()
            return
        
        if weight + weights[i] <= capacity:
            # Select the i-th item
            selection[i] = (values[i], weights[i], True)
            explore(i+1, value+values[i], weight+weights[i], selection)
            selection[i] = (values[i], weights[i], False)
        
        # Do not select the i-th item
        explore(i+1, value, weight, selection)
        
    explore(0, 0, 0, best_selection)
    return best_value, best_selection


# Example usage
weights = [95, 4, 60, 32, 23, 72, 80, 62, 65, 46]
values = [55, 10, 47, 5, 4, 50, 8, 61, 85, 87]
capacity = 269

best_value, best_selection = knapsack(capacity, weights, values)

print("La selección óptima es:")
selected_items = [(i+1, item[0], item[1]) for i, item in enumerate(best_selection) if item[2]]
for item in selected_items:
    print(" - Elemento {} (valor={}, peso={})".format(*item))
print("Valor total de la mochila:", best_value)
