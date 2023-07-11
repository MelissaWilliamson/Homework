import random

lotto_number = random.sample(range(1, 50), 6)
bonus_ball = random.sample(range(1, 9), 2)
sorted_lotto_numbers = sorted(lotto_number) + sorted(bonus_ball)
print(sorted_lotto_numbers)