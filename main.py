# Japan Goal Tracker 2.0
goal = 1000
current_savings = 0

print("--- Welcome! Your Journey begins ---")

while True:
    print(f"\nТекущие накопления: {current_savings} манат")
    print(f"Осталось до цели: {goal - current_savings} манат")
    
    user_input = input("\nВведите сумму дохода (или 'exit' для выхода): ")
    

    if user_input.lower() == 'exit':
        print("Программа закрыта. Удачи в накоплениях!")
        break
    
    try:
        income = float(user_input)
        current_savings += income
    except ValueError:
        print("Ошибка! Пожалуйста, вводи только числа или 'exit'.")

    if current_savings >= goal:
        print("🎊 ПОЗДРАВЛЯЮ! Ты достигла цели!🎊")
