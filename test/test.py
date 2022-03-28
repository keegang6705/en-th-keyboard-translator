# -*- encoding: utf-8 -*-

from sys import path

path.append("..")

import key_changer
from key_changer import EN2TH, TH2EN, ANSI_KEYBOARD, QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT, THAI_PATTACHOTE_LAYOUT

# --------------------

print(key_changer.convert("l;ylfu", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT))
print(key_changer.convert(";yoso7j' Cyogfbowxshv'oYhkc]h;r[;jkoYhkw,jws]", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT))

print(key_changer.convert("ทำ ฟืก เน ะน ฟืนะ้ำพ ิฟะ้พนนท", THAI_KEDMANEE_LAYOUT, QWERTY_LAYOUT))
print(key_changer.convert("ห้ระม ะ้ำ ไฟะำพ กนำหืงะ ดสนไ", THAI_KEDMANEE_LAYOUT, QWERTY_LAYOUT))

print(key_changer.auto("mew'fusojk wxshv'oYhkmujvnjodHwfh", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT))
print(key_changer.auto("ดีแาม ไ้ำพำ ฟพำ ร เนรืเ ืำปะ", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT))

print(key_changer.convert("ฉันก็ได้แต่นั่งรอหวังว่านํ้าจะไหล", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT))

print(key_changer.switch("ฟะ ะ้ฟะ ทนทำืะม vp^jfuqoYhkdHws]", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT))
print(key_changer.switch("py'fusojk gdnv[=b[skp]t", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT))

# --------------------
print("-" * 20)

print(key_changer.convert("👍", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT, not_know = "?"))

# --------------------
print("-" * 20)
print(key_changer.auto("l;ylfu สบายดี", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT, default = EN2TH))

# --------------------
print("-" * 20)
print(key_changer.auto("Cyow,jgxHowisivot", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT, standard_key_layout = ANSI_KEYBOARD))
