import re

def parse_whatsapp_log(path):
    with open(path) as f:
        content = f.readlines()

    text = ""
    for line in content:
        temp = line.split(':')
        temp = ':'.join(temp[:4]), ':'.join(temp[4:])
        text += re.sub(r'^https?:\/\/.*[\r\n]*', '', temp[1], flags=re.MULTILINE)

    return text
