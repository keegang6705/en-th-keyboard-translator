from sys import path as sys_path
from os import path
sys_path.append(path.join(path.dirname(__file__), ".."))

import key_changer

translator = key_changer.KeyChanger("ANSI", "QWERTY", "Thai_Kedmanee")

print("KeyChanger.translate", end="")
if translator.translate("l;ylfu") == "สวัสดี":
    print(" - PASS")
else:
    print(" - FAIL")

print("KeyChanger.reverse", end="")
if translator.reverse("้ำสสน") == "hello":
    print(" - PASS")
else:
    print(" - FAIL")

print("KeyChanger.auto", end="")
if translator.auto(";yoouhvkdkLfu") == "วันนี้อากาศดี" and translator.auto("ะนกฟั ะ้ำ ไำฟะ้ำพ รห เนนก") == "today the weather is good":
    print(" - PASS")
else:
    print(" - FAIL")

print("KeyChanger.KeyboardLayout")
print(" -> " + str(key_changer.KeyboardLayout))

print("KeyChanger.LanguageLayout")
print(" -> " + str(key_changer.LanguageLayout))
