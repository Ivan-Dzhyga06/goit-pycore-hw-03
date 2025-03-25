import random

def get_numbers_ticket(min, max, quantity):
    try: 
        if  not (1 <= min < max <= 1000):
            return 'Вкажіть числа у діапазоні від 1 до 1000'
        
        if quantity > (max - min + 1):
            return 'Кількість чисел білетів не може перевищувати діапазон'
        
        random_counts = random.sample(range(min, max + 1), quantity)
        return random_counts 
    
    except ValueError as e:
        return f"{e}"
    
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
