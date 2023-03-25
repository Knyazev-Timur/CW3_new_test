import datetime
import json
from json import JSONDecodeError
from typing import Optional

from model import Operation


def read_json(file_name) -> Optional[list]:
    """
    :param file_name: str
    :return: list
    получает имя JSON файла, считывает файл
    и возвращает список словарей
    """
    try:
        with open(file_name, 'r', encoding='UTF-8') as read_file:
            return json.load(read_file)
    except FileNotFoundError:
        return ['FileNotFoundError']
    except JSONDecodeError:
        return ['JSONDecodeError']


def get_date(date) -> object:
    """Получает строку yyyy-mm-dd
    возвращает экземпляр класса date"""
    date = datetime.datetime(int(date[:4]), int(date[5:7]), int(date[8:10]))
    return date


def get_card_name(from_) -> list:
    if from_ is None:
        return [None, None]
    else:
        from_list = from_.split()
    return from_list


def get_model() -> list:
    """Складывает все данные из JSON в класс Operation
    возвращает список с созданными экземплярами классса"""
    data_all = read_json("data/operations.json")

    if data_all is not None:
        operations = [
            Operation(
                id=data.get("id"),
                state=data.get("state"),
                date=get_date(data.get("date")),
                amount=data["operationAmount"]["amount"],
                currency=data["operationAmount"]["currency"]["name"],
                description=data.get("description"),
                card=get_card_name(data.get('from'))[0],
                from_=get_card_name(data.get('from'))[-1],
                to=data.get("to").split()[-1]
            ) for data in data_all]
    return operations


def get_sort_dict() -> dict:
    """
    Т.к. словарь не сортируемый, создается отдельный словарь,
    где ключ - экземпляр класса Operation, значение - дата.
    Из полученного словаря извлекаются значения items(), формируется список значений (data),
    данный список сортируется с параметром reverse=True и возвращается в виде dict
    """

    operations = get_model()
    for_sorted = {operation: operation.get_date() for operation in operations}
    return dict(sorted(for_sorted.items(), key=lambda x: x[1], reverse=True))


def get_list_items() -> list:
    """Извлекаются экземпляры класса из сортированного ранее списка,
    формируется список в 5 элементов, если платеж исполнен, и передается на вывод"""
    sorted_dict = get_sort_dict()
    for_input = []
    for i in sorted_dict.keys():
        if i.get_state() == "EXECUTED":
            for_input.append(i)
        if len(for_input) >= 5:
            break
    return for_input


def get_output(operations):
    """Функция вывода результата"""
    for operation in operations:
        if operation.get_from() is not None:
            print(
                f'{operation.get_date().strftime("%d.%m.%Y")} {operation.description}\n{operation.card} '
                f'{operation.get_from()} -> Счет {operation.get_to()}\n'
                f'{operation.amount} {operation.currency}\n')
        else:
            print(
                f'{operation.get_date().strftime("%d.%m.%Y")} {operation.description}\nСчет {operation.get_to()}\n'
                f'{operation.amount} {operation.currency}\n')


#get_output(get_list_items())
