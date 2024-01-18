# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(delim = ",") -> None:
    with open("input.csv", "r") as csv_input:
        data = [data for data in csv.DictReader(csv_input, delimiter=delim)]
    ...  # TODO Сериализовать в файл с отступами равными 4
    with open("output.json", "w") as data_output:
        json.dump(data, data_output, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
