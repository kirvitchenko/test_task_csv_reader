import argparse
import csv
from statistics import mean
from tabulate import tabulate


def get_complete_devices_list(files):
    """
    Получаем список словарей с данными устройств из сформированный из данных разных файлов
    """
    full_list = []
    for file in files:
        with open(file, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for device_dict in reader:
                full_list.append(device_dict)
    return full_list


def get_all_values_by_field(field, devices_list):
    """
    Получаем словарь со списками значений небходимого поля для каждого бренда
    """
    values_dict = {}
    for device in devices_list:
        if device["brand"] in values_dict:
            values_dict[device["brand"]].append(float(device[field]))
        else:
            values_dict[device["brand"]] = [float(device[field])]
    return values_dict


def get_report(report_type, values_dict):
    """
    Получаем отсортированный список и пронумерованный список кортежей c данными по необходимому типу отчета
    В параметре report_type указывается тип отчета и за счет ветвления выполнятся необходимая логика
    для формирования отчета
    :param report_type:
    :param values_dict:
    :return:
    """
    report_dict = {}
    if report_type == "average":
        for device_field in values_dict:
            report_dict[device_field] = round(mean(values_dict[device_field]), 2)
    sorted_report = sorted(report_dict.items(), key=lambda x: x[1], reverse=True)
    table_data = [
        (i + 1, brand, rating) for i, (brand, rating) in enumerate(sorted_report)
    ]
    return table_data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Скрипт для анализа csv-файла")

    parser.add_argument(
        "--files", nargs="+", required=True, help="Список CSV файлов для анализа"
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=["average-rating"],
        help='Параметр --report должен быть в формате "<тип>-<поле>", например "average-rating"',
    )

    args = parser.parse_args()
    try:
        type_of_report, field = args.report.split("-")
    except ValueError:
        parser.error(
            'Параметр --report должен быть в формате "<тип>-<поле>", например "average-rating"'
        )

    devices_list = get_complete_devices_list(args.files)
    report_dict = get_all_values_by_field(field, devices_list)
    result = get_report(type_of_report, report_dict)

    print(tabulate(result, headers=["Бренд", "Средний рейтинг"], tablefmt="grid"))
