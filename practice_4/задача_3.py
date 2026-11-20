# Задание 3 kwargs
def person(**kwargs):
    name = kwargs.get("name", "Гость")
    age = kwargs.get("age", 0)
    return name, age


print(person(name="Анна", age=17))

print("-" * 20)