## en-th-keyboard-translator
translate character en-th

**สรูปมันคืออะไร อันนี้ก็ไม่รู้เหมือนกัน**

---

## วิธีใช้

**run**
```bash
python key_changer [en2th / th2en / auto / switch]
```

**เรียกใช้ module**
```py
import key_changer

print(key_changer.en2th("l;ylfu"))
# output : สวัสดี
print(key_changer.en2th(";yoso7j' Cyogfbowxshv'oYhkc]h;r[;jkoYhkw,jws]"))
# output : วันหนึ่ง ฉันเดินไปห้องนํ้าแล้วพบว่านํ้าไม่ไหล

print(key_changer.th2en("ทำ ฟืก เน ะน ฟืนะ้ำพ ิฟะ้พนนท"))
# output : me and go to another bathroom
print(key_changer.th2en("ห้ระม ะ้ำ ไฟะำพ กนำหืงะ ดสนไ"))
# output : shit, the water doesn't flow

print(key_changer.auto("mew'fusojk wxshv'oYhkmujvnjodHwfh"))
# output : ทำไงดีหน่า ไปห้องนํ้าที่อื่นก็ได้
print(key_changer.auto("ดีแาม ไ้ำพำ ฟพำ ร เนรืเ ืำปะ"))
# output : fuck, where are i going next

print(key_changer.en2th("ฉันก็ได้แต่นั่งรอหวังว่านํ้าจะไหล"))
# output : ฉันก็ได้แต่นั่งรอหวังว่านํ้าจะไหล

print(key_changer.switch("ฟะ ะ้ฟะ ทนทำืะม vp^jfuqoYhkdHws]"))
# output : at that moment, อยู่ดีๆนํ้าก็ไหล
print(key_changer.switch("py'fusojk gdnv[=b[skp]t"))
# output : ยังดีหน่า เกือบชิบหายละ
```
