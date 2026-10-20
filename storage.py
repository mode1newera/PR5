"""Чтение входного файла и сохранение двух результатов."""
from pathlib import Path
from validators import parse_line


def load_anketas(filename):
    accepted = []
    rejected = []
    path = Path(filename)
    # Пропускаем пустые строки, остальные проверяем.
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        person, error = parse_line(raw)
        if error:
            rejected.append((number, raw, error))
        else:
            accepted.append(person)
    return accepted, rejected


def save_results(accepted, rejected, output_folder):
    folder = Path(output_folder)
    # Файлы с результатами создаются заново при каждом запуске.
    with (folder / "ok.txt").open("w", encoding="utf-8") as file:
        for person in sorted(accepted, key=lambda x: x["fio"]):
            file.write(";".join(person[k] for k in ("fio", "email", "phone", "group")) + "\n")
    with (folder / "errors.txt").open("w", encoding="utf-8") as file:
        for number, raw, reason in rejected:
            file.write(f"строка {number}: {reason}\n    {raw}\n")


if __name__ == "__main__":
    print("Модуль storage.py читает анкеты и сохраняет результаты.")
