# -*- encoding: utf-8 -*-

from sys import path
path.append("..")

import key_changer

# --------------------

print(str(key_changer.__dir__()))

# --------------------

print(key_changer.en2th("l;ylfu"))
print(key_changer.en2th(";yoso7j' Cyogfbowxshv'oYhkc]h;r[;jkoYhkw,jws]"))

print(key_changer.th2en("ทำ ฟืก เน ะน ฟืนะ้ำพ ิฟะ้พนนท"))
print(key_changer.th2en("ห้ระม ะ้ำ ไฟะำพ กนำหืงะ ดสนไ"))

print(key_changer.auto("mew'fusojk wxshv'oYhkmujvnjodHwfh"))
print(key_changer.auto("ดีแาม ไ้ำพำ ฟพำ ร เนรืเ ืำปะ"))

print(key_changer.en2th("ฉันก็ได้แต่นั่งรอหวังว่านํ้าจะไหล"))

print(key_changer.switch("ฟะ ะ้ฟะ ทนทำืะม vp^jfuqoYhkdHws]"))
print(key_changer.switch("py'fusojk gdnv[=b[skp]t"))

# --------------------
print("-" * 20)

print(key_changer.en2th("👍", not_know = "?"))

# --------------------
print("-" * 20)
print(key_changer.auto("l;ylfu สบายดี", default = key_changer.EN2TH))