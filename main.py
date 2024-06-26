import sys
import os
from engine import Fractal

#https://moviepy.readthedocs.io/en/latest/getting_started/quick_presentation.html


def get_size_window(argv):
    if len(argv) < 4 or not argv[2].isdigit() or not argv[3].isdigit():
        return 1, 1
    return int(argv[2]), int(argv[3])


def main():
    if len(sys.argv) >= 2:
        frac = Fractal()
        if sys.argv[1] == 'help':
            print('''
1) main.py help
2) main.py path:str
    test load setting.json
3) main.py path:str sizeX:int sizeY:int mod:str ...
    mod: window - see fractal on every iter
            par:float(second move or 0)
         screenshot - make screenshot on <par> iter with name <name>
            par:int name:str''')
        elif os.path.exists(sys.argv[1]):
            try:
                ans = frac.load(sys.argv[1], get_size_window(sys.argv))
            except:
                print('Error: not valid')
                return
            if ans != 'ok':
                print(ans)
                return
            if len(sys.argv) >= 4:
                if sys.argv[4] == 'window':
                    from window import main as fun
                elif sys.argv[4] == 'screenshot':
                    from screenshot import main as fun
                else:
                    print('Error: not valid mod')
                    return
                fun(frac, get_size_window(sys.argv), sys.argv)
            else:
                print('All ok')
        else:
            print('Error: not valid path')
    print('Bye!')


if __name__ == '__main__':
    main()