"""Проверки и разбор одной анкеты."""


def check_fio(value):
    # Убираем лишние пробелы и делаем нормальный регистр.
    words = value.split()
    if len(words) < 2:
        raise ValueError("в ФИО меньше двух слов")
    return " ".join(words).title()


def check_email(value):
    email = value.strip().lower()
    if email.count("@") != 1:
        raise ValueError("в почте должна быть одна @")
    user, domain = email.split("@")
    if not user or not domain or "." not in domain:
        raise ValueError("неверно указана электронная почта")
    if domain.startswith(".") or domain.endswith("."):
        raise ValueError("неверный домен почты")
    if any(ch.isspace() for ch in email):
        raise ValueError("в почте есть пробелы")
    return email


def check_phone(value):
    digits = "".join(ch for ch in value if ch.isdigit())
    if len(digits) != 11:
        raise ValueError("в телефоне должно быть 11 цифр")
    if digits[0] not in "78":
        raise ValueError("телефон должен начинаться с 7 или 8")
    return "7" + digits[1:]


def check_group(value):
    group = "".join(value.split()).lower()
    if not group:
        raise ValueError("не указана группа")
    return group


def parse_line(line):
    """Возвращает анкету или ошибку в виде двух значений."""
    parts = line.split(";")
    if len(parts) != 4:
        return None, f"полей {len(parts)} вместо 4"
    fio, email, phone, group = parts
    try:
        person = {
            "fio": check_fio(fio),
            "email": check_email(email),
            "phone": check_phone(phone),
            "group": check_group(group),
        }
    except ValueError as error:
        return None, str(error)
    return person, None


if __name__ == "__main__":
    print(parse_line("Иванов Иван;ivanov@mail.ru;89211112233;09с41"))
