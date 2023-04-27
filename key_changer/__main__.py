import argparse
import key_changer

parser = argparse.ArgumentParser(
    prog="key_changer",
    description="Translate characters caused by typos because you forgot to change the keyboard language layout",
    epilog="version " + key_changer.__version__)

parser.add_argument("--layout", type=str, required=True, help="keyboard layout")
parser.add_argument("--lang1", type=str, required=True, help="language layout 1 (wrong text)")
parser.add_argument("--lang2", type=str, required=True, help="language layout 2")
parser.add_argument("--text", type=str, required=True, help="text for translation")
parser.add_argument("--auto", action="store_true", help="will be selected according to the number of characters detected")
parser.add_argument("--list", action="store_true", help="show list of keyboard layout and language layout")
parser.add_argument("--version", action="version", version="%(prog)s " + key_changer.__version__)

args = parser.parse_args()

if args.list:
    print("Keyboard")
    for i in key_changer.KeyboardLayout:
        print(f"    {i}")
    print("Language")
    for i in key_changer.LanguageLayout:
        print(f"    {i}")
    exit()

try:
    translator = key_changer.KeyChanger(args.layout, args.lang1, args.lang2)
    if args.auto:
        print(translator.auto(args.text))
    else:
        print(translator(args.text))
except Exception as e:
    print(str(e))
