import numpy as np

def function(x):
    return (x - 6) ** 2 + 1

def gradient(x):
    return 2 * (x - 6)

def gradient_descent(starting_point, learning_rate, precision, max_iterations):
    x = starting_point
    for i in range(max_iterations):
        grad = gradient(x)
        next_x = x - learning_rate * grad
        print(f"Итерация {i+1}: x = {next_x}, f(x) = {function(next_x)}")
        if abs(next_x - x) < precision:
            print("Достигнута требуемая точность.")
            break
        x = next_x
    return x

if __name__ == "__main__":
    starting_point = 0.0
    learning_rate = 0.1
    precision = 1e-6
    max_iterations = 1000

    print("Старт...")
    minimum = gradient_descent(starting_point, learning_rate, precision, max_iterations)
    print(f"Минимум функции достигнут в x = {minimum}")
