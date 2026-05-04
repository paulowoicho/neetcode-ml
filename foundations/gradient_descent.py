class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:

        current_value = init
        for i in range(iterations):
            guess = 2 * current_value
            current_value -= learning_rate * guess
        
        return round(current_value, 5)