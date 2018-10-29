import openpyxl

def find_parks_not_in_usa():
    wb = openpyxl.load_workbook('sample.xlsx')

    sheet = wb['Sheet1']

    parklist = []

    for row in sheet[2:sheet.max_row]:
        if row[5].value != 'US' :
            parklist.append(row)

    wb.close()
    return parklist


def make_file(parklist):
    with open('parklist.txt', 'w', encoding='UTF-8') as file:
        for park in parklist:
            park_str = make_parkstr(park)
            file.write(park_str)


def make_parkstr(park):
    result_str = ''

    for item in park:
        result_str += str(item.value) + '\t'

    return result_str


def main():
    parklist = find_parks_not_in_usa()
    make_file(parklist)
    print('parklist.txt created')


if __name__ == '__main__':
    main()