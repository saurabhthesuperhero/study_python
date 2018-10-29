def extract_text(file_name):
    subtitle_content = []

    file = open(file_name, 'r')
    for line in file:
        line = line.replace('\n', '')
        if( len(line) < 3 and line.isnumeric()):
            continue
        elif line.count(':') > 2 and line.count('-->') > 0:
            continue
        elif line == '':
            continue
        else:
            subtitle_content.append(line)


def make_file(content, file_name, ext='txt'):
    with open(file_name + '.' + ext, 'w') as file:
        for line in content:
            file.write('%s\n' % line)

def main():
    file_name = 'subtitle.srt'
    subtitle_contents = extract_text(file_name)
    make_file(subtitle_contents, file_name, 'txt')
    print('completed')


if __name__ == '__main__':
    main()