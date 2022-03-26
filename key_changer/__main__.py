if __name__ != "__main__":
    exit()

from sys import argv
import key_changer

help_ = """python key_changer [en2th / th2en / auto / switch]"""
argv_len = len(argv)

if argv_len == 2:
    if argv[1] == "en2th":
        print(key_changer.en2th(input(">")))
    elif argv[1] == "th2en":
        print(key_changer.th2en(input(">")))
    elif argv[1] == "auto":
        print(key_changer.auto(input(">")))
    elif argv[1] == "switch":
        print(key_changer.switch(input(">")))
    else:
        print(help_)
else:
    print(help_)
