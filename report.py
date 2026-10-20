"""Таблица анкет, ошибки и статистика."""
from collections import Counter


def masked_phone(phone):
    # Прячем часть номера, оставляем код и последние две цифры.
    return f"+7 ({phone[1:4]}) ***-**-{phone[-2:]}"


def short_fio(fio):
    surname, *names = fio.split()
    return surname + " " + " ".join(word[0] + "." for word in names)


def show_report(accepted, rejected):
    ordered = sorted(accepted, key=lambda x: x["fio"])
    print(f"{'№':>3}  {'ФИО':<34}  {'Группа':<8}  Телефон")
    print("-" * 72)
    for number, person in enumerate(ordered, 1):
        print(f"{number:>3}  {person['fio']:<34}  {person['group']:<8}  {masked_phone(person['phone'])}")
    print("-" * 72)
    print(f"Принято: {len(accepted)} | Отклонено: {len(rejected)}")
    print("\nОтклонённые анкеты:")
    if not rejected:
        print("  Нет")
    for number, raw, reason in rejected:
        print(f"  строка {number}: {reason}\n    {raw}")
    print("\nПо группам:")
    for group, count in sorted(Counter(x["group"] for x in accepted).items()):
        print(f"  {group:<8} {count}")


if __name__ == "__main__":
    print("Модуль report.py выводит сведения по анкетам.")
