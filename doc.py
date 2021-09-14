import os

import smalldoc

if __name__ == '__main__':
    current_path = os.path.dirname(os.path.abspath(__file__))
    documentation = smalldoc.parse(current_path, 'smalldoc')
    print(smalldoc.write(documentation))
