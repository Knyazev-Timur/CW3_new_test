import pytest
import datetime

from utils import read_json, get_date, get_model, get_sort_dict, get_list_items

def test_load_json():
    assert read_json("data/operations.json") is not None, "Json not loaded"

def test_get_date():
    assert get_date("2017-11-20").strftime("%d.%m.%Y") == "20.11.2017", "Ошибка обработки даты"

def test_get_model():
    assert get_model() is not None, "Экземпляры класса не созданы"

def test_get_sort_dict():
    assert get_sort_dict() is not None, "Словарь для сортировки не создан"

def test_get_list_items():
    assert len(get_list_items()) <= 5, "Неверная длинна списка на вывод"

