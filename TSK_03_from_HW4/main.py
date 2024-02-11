
# Завдання з ДЗ-4 Третє завдання (не обов'язкове)
# Не встиг вчасно ,здаю зараз у 5му блоці

import colorama

import sys
import pathlib 
colorama.init(autoreset=True)
path=sys.argv[1]
 
print()
print(colorama.Fore.BLUE+path)

def lst_dr(path,tab=0):
    user_p=pathlib.Path(path)
    try:
        lst = user_p.iterdir()
        
        for i in lst:
            
            if i.is_dir():
                print(colorama.Fore.GREEN+ "    |"+("      "*tab)+"\\" + "-"*5 + i.name)
                lst_dr(i,tab+1)
            else:
                print(colorama.Fore.RED+"    |"+("      "*tab)+"\\" + "-"*2+i.name)
    except Exception:
        print("Invalid args.Pls try again.")    

lst_dr(path)
print()


