def energy_per_day(kwh, days):
    if days == 0:
        return "На ноль делить нельзя"
    return kwh / days

# 1. Проверка assert
assert energy_per_day(56, 7) == 8.0
assert energy_per_day(56, 0) == "На ноль делить нельзя"
assert energy_per_day(100, 10) == 10.0  # Собственный корректный пример

# 2. Сортировка lambda
words = ["ход", "партия", "чемпионат"]
sorted_words = sorted(words, key=lambda word: len(word))

print(sorted_words)