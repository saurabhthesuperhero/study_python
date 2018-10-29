import re
import pyperclip

email_reg = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4}){1,2}
    )''', re.VERBOSE)

def find_match_list():
    text = pyperclip.paste()
    matches = []

    for email in email_reg.findall(text) :
        matches.append(email[0])

    return matches

def copy_result(matches):
    if len(matches) > 0 :
        pyperclip.copy('\n'.join(matches))
        print(matches)
    else :
        print('no data')

def main():
    matches = find_match_list()
    copy_result(matches)

main()