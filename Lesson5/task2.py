# TODO импортировать необходимые модули
import csv, json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f:
        lines = [line for line in csv.DictReader(f)]
        # for line in lines:
        #     print(line)
      # TODO считать содержимое csv файла

      # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME,"w") as f1:
        json.dump(lines, f1, indent = 4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
