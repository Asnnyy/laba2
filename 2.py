n = int(input("Введите номер места"))
if (n % 2) != 0 and (n in range(35)):
    print("У Вас купе и нижнее место")
elif (n % 2) == 0 and (n in range(35)):
    print("У Вас купе и верхнее место")
elif (n % 2) == 0 and (n in range(35, 55)):
    print("У Вас боковое верхнее место")
elif (n % 2) != 0 and (n in range(35, 55)):
    print("У Вас боковое нижнее место")