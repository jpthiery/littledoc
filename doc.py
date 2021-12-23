import os

import littledoc

if __name__ == '__main__':
    current_path = os.path.dirname(os.path.abspath(__file__))
    documentation = littledoc.parse(current_path, 'smalldoc')
    print(littledoc.write(documentation))
