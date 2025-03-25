import random

def get_numbers_ticket(min_val, max_val, quantity):
    try: 
        if not (1 <= min_val < max_val <= 1000):
            return "Вкажіть числа у діапазоні від 1 до 1000"

        if quantity > (max_val - min_val + 1):
            return "Кількість чисел не може перевищувати діапазон"

        random_counts = random.sample(range(min_val, max_val + 1), quantity)
        return random_counts 
    except ValueError as e:
        return f"Помилка: {e}"

lottery_numbers = get_numbers_ticket(1, 1000, 0)
print("Ваші лотерейні числа:", lottery_numbers)
