"""Запуск: python main.py [путь к файлу с анкетами]."""
from pathlib import Path
import sys
from storage import load_anketas, save_results
from report import show_report


def main():
    # По умолчанию используем anketa.txt рядом с программой.
    filename = (Path(sys.argv[1]) if len(sys.argv) > 1 else
                Path(__file__).with_name("anketa.txt"))
    try:
        accepted, rejected = load_anketas(filename)
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return
    except (OSError, UnicodeError) as error:
        print(f"Не удалось прочитать файл: {error}")
        return
    show_report(accepted, rejected)
    try:
        save_results(accepted, rejected, filename.parent)
    except (OSError, UnicodeError) as error:
        print(f"Не удалось сохранить результаты: {error}")
        return
    print("\nСохранено: ok.txt и errors.txt")


if __name__ == "__main__":
    main()
