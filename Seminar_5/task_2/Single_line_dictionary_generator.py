names = ["Геннадий", "Владимир", "Дмитрий"]
salary = [58600, 72100, 36800]
bonus = ["9.30%", "11.10%", "12.45%"]


def salary_gen(names: list[str], salary: list[int], bonus: list[str]) -> dict[str: float]:
    return {name: sale / 100 * bon for name, sale, bon in zip(names, salary, (float(i[:-1]) for i in bonus))}.items()


print(*(salary_gen(names, salary, bonus)))
