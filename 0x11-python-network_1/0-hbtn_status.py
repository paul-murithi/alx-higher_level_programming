#!/usr/bin/python3
"""script that fetches URL using urllib"""

import urllib.request


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        bytes_content = response.read()
        content = bytes_content.decode('utf-8')
        print_str = '''Body response:
\t- type: {}
\t- content: {}
\t- utf8 content: {}'''.format(type(bytes_content), bytes_content, content)
        print(print_str)
