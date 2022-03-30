import csv


def get_most_asked_by_maria(reader):
    maria_orders = {}
    for row in reader:
        if row[0] == 'maria':
            if row[1] in maria_orders:
                maria_orders[row[1]] += 1
            else:
                maria_orders[row[1]] = 1
    dishes = list(maria_orders.keys())
    counts = list(maria_orders.values())
    most_asked_count = max(counts)
    count_position = counts.index(most_asked_count)
    most_asked_dish = dishes[count_position]
    return most_asked_dish


def get_arnaldo_burger_count(reader):
    times_arnaldo_ate_hamburger = 0
    for row in reader:
        if row[0] == 'arnaldo' and row[1] == 'hamburguer':
            times_arnaldo_ate_hamburger += 1
    return times_arnaldo_ate_hamburger


def get_never_eaten_by_joao(reader):
    total_dishes = set()
    dishes_ordered_by_joao = set()
    for row in reader:
        if row[1] not in total_dishes:
            total_dishes.add(row[1])
        if row[0] == 'joao' and row[1] not in dishes_ordered_by_joao:
            dishes_ordered_by_joao.add(row[1])
    return total_dishes.difference(dishes_ordered_by_joao)


def get_joao_missing_days(reader):
    every_day = set()
    days_with_joao = set()
    for row in reader:
        if row[2] not in every_day:
            every_day.add(row[2])
        if row[0] == 'joao' and row[2] not in days_with_joao:
            days_with_joao.add(row[2])
    return every_day.difference(days_with_joao)


def analyze_log(path_to_file):
    try:
        with open(path_to_file) as file:
            reader = csv.reader(file)
            most_asked_by_maria = get_most_asked_by_maria(reader)
        with open(path_to_file) as file:
            reader = csv.reader(file)
            times_arnaldo_ate_hamburger = get_arnaldo_burger_count(reader)
        with open(path_to_file) as file:
            reader = csv.reader(file)
            dishes_joao_never_asked = get_never_eaten_by_joao(reader)
        with open(path_to_file) as file:
            reader = csv.reader(file)
            days_without_joao = get_joao_missing_days(reader)
        with open('data/mkt_campaign.txt', mode='w') as file:
            lines = [
                str(most_asked_by_maria) + '\n',
                str(times_arnaldo_ate_hamburger) + '\n',
                str(dishes_joao_never_asked) + '\n',
                str(days_without_joao)
            ]
            for line in lines:
                file.write(line)
    except FileNotFoundError:
        if path_to_file.split('.')[-1] != 'csv':
            raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


analyze_log('data/orders_1.csv')
