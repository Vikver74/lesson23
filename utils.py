

def get_filter(data, value):
    with open(data) as file:
        res = filter(lambda line: value in line.lower(), file.readlines())
        with open('result.txt', 'w') as res_file:
            res_file.writelines(list(res))


def get_map(data, value):
    with open(data) as file:
        res = map(lambda line: parse_string(line)[value-1]+'\n', file.readlines())
        with open('result.txt', 'w') as res_file:
            res_file.writelines(list(res))


def get_unique(data):
    with open(data) as file:
        res = set(file.readlines())
        with open('result.txt', 'w') as res_file:
            res_file.writelines(list(res))


def get_sort(data, asc_dsc):
    with open(data) as file:
        res = sorted(file.readlines(), reverse=True if asc_dsc == 'dsc' else False)
        with open('result.txt', 'w') as res_file:
            res_file.writelines(list(res))


def get_limit(data, limit):
    with open(data) as file:
        res = [text for num, text in enumerate(file.readlines(), 1) if num <= limit]
        with open('result.txt', 'w') as res_file:
            res_file.writelines(res)


def parse_string(string):
    return string.split()
