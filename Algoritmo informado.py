import random

def knapsack_ihb(capacity, weights, values, max_iterations):
    n = len(weights)
    # Punto de partida: solución aleatoria
    best_selection = [random.randint(0, 1) for _ in range(n)]
    best_value = sum([v for v, s in zip(values, best_selection) if s])
    # Iterar varias veces mejorando la solución actual
    for k in range(1, max_iterations+1):
        # Obtener las k mejores soluciones vecinas
        neighbors = []
        for i in range(n):
            neighbor = best_selection.copy()
            neighbor[i] = 1 - neighbor[i]
            value = sum([v for v, s in zip(values, neighbor) if s])
            if value > best_value:
                neighbors.append((value, neighbor))
        neighbors = sorted(neighbors, reverse=True)[:k]
        # Elegir una solución vecina al azar
        if len(neighbors) > 0:
            best_value, best_selection = random.choice(neighbors)
    # Devolver la mejor solución encontrada
    return best_value, best_selection

def main():
    weights = [95, 4, 60, 32, 23, 72, 80, 62, 65, 46]
    values = [55, 10, 47, 5, 4, 50, 8, 61, 85, 87]
    capacity = 269
    max_iterations = 100
    best_value, best_selection = knapsack_ihb(capacity, weights, values, max_iterations)
    print("Mejor valor de la mochila:", best_value)
    print("Elementos seleccionados:")
    for i, x in enumerate(best_selection):
        if x:
            print("- Elemento", i+1, "(peso:", weights[i], ", valor:", values[i], ")")

if __name__ == '__main__':
    main()
