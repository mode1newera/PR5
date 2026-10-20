"""Несколько простых проверок программы через pytest."""
from pathlib import Path
from validators import parse_line, check_fio, check_phone
from storage import load_anketas, save_results
from report import masked_phone, short_fio


def test_fio():
    assert check_fio("  иВанОВ   иВАН  ") == "Иванов Иван"


def test_phone():
    assert check_phone("8 (921) 123-45-67") == "79211234567"
    assert masked_phone("79211234567") == "+7 (921) ***-**-67"


def test_short_fio():
    assert short_fio("Иванов Иван Петрович") == "Иванов И. П."


def test_parser():
    good, error = parse_line("Иванов Иван;ivanov@mail.ru;89211234567;09с41")
    assert error is None and good["group"] == "09с41"
    bad, error = parse_line("Иванов;ivanov@mail.ru;89211234567;09с41")
    assert bad is None and "ФИО" in error


def test_read_and_save(tmp_path):
    source = Path(__file__).with_name("anketa.txt")
    accepted, rejected = load_anketas(source)
    assert len(accepted) == 6
    assert len(rejected) == 6
    save_results(accepted, rejected, tmp_path)
    assert len((tmp_path / "ok.txt").read_text(encoding="utf-8").splitlines()) == 6
    assert "строка" in (tmp_path / "errors.txt").read_text(encoding="utf-8")
