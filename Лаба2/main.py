from inherit import Animal, Dog

print("Обычное животное ")
cat = Animal("Мурзик", 6, "Кошка")
cat.info()
cat.make_sound()
print()

print("Собака")
dog = Dog("Жулик", 7, "собака", "Овчарка", "Да")
dog.info()
dog.make_sound()
dog.guard_house()

print()

del cat
del dog
