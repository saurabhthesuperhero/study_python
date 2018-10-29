import csv
import os


def save_and_remove_header(filename):
    # CSV 파일을 읽어 헤더를 제거하고 저장
    # python 주석은 함수 바로 첫번째 줄에 추가

    csv_rows = []
    with open(os.path.join('baseballdatabank-master', 'core', filename), 'r', encoding='UTF-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if reader.line_num == 1:
                continue
            csv_rows.append(row)

    with open(os.path.join('baseballdatabank-master', 'header-removed', filename), 'w', newline='') as file:
        # newline='' : line 사이 공백 제거
        writer = csv.writer(file)

        for row in csv_rows:
            writer.writerow(row)


def main():
    os.makedirs(os.path.join('baseballdatabank-master', 'header-remove'), exist_ok=True)

    for filename in os.listdir(os.path.join('baseballdatabank-master', 'core')):
        if not filename.endswith('.csv'):
            continue

        print('saving file: ', filename)

        save_and_remove_header(filename)

    print('job completed..')


if __name__ == '__main__':
    main()