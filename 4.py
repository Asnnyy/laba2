import random
c = ["красный цвет", "синий цвет", "жёлтый цвет"]
r_c1 = random.choice(c)
r_c2 = random.choice(c)
print(r_c1, r_c2)
if (r_c1 == "красный цвет" and r_c2 == "синий цвет") or (r_c1 == "синий цвет" and r_c2 == "красный цвет"):
    print("фиолетовый цвет")
elif (r_c1 == "красный цвет" and r_c2 == "жёлтый цвет") or (r_c1 == "жёлтый цвет" and r_c2 == "красный цвет"):
    print("оранжевый цвет")
elif (r_c1 == "синий цвет" and r_c2 == "жёлтый цвет") or (r_c1 == "жёлтый цвет" and r_c2 == "синий цвет"):
    print("зелёный цвет")
else:
    print("ошибка")
