## Translate text from character keyboard layout.

- **key-changer - version 2.1**

**มันคืออะไร อันนี้ก็ไม่แน่ใจเหมือนกัน**  
> สรุปแบบเข้าใจง่ายๆคือ มันคือการตัวแปลงข้อความที่พิมพ์แบบปกติ แต่ดันลืมเปลี่ยน keboard layout มันเลยทำให้ข้อความออกมาแปลกๆ ซึ่ง package นี้จะมี function ที่ใช้แปลข้อความจาก keyboard layout หนึ่งไปอีก layout หนึ่ง  

---

### Keyboard layout ที่รองรับ
ตอนนี้ยังมีแค่ [QWERTY layout](https://en.wikipedia.org/wiki/QWERTY) : [Thai Kedmanee keyboard layout](https://en.wikipedia.org/wiki/Thai_Kedmanee_keyboard_layout)

---

### การติดตั้ง
**pip**
```bash
pip install key-changer
```

---

### การเรียกใช้งาน

**run**
```bash
python key_changer [en2th / th2en / auto / switch]
```

**เรียกใช้**
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

# คือการสลับแลกเปลี่ยนระหว่างกัน
print(key_changer.switch("ฟะ ะ้ฟะ ทนทำืะม vp^jfuqoYhkdHws]"))
# output : at that moment, อยู่ดีๆนํ้าก็ไหล
print(key_changer.switch("py'fusojk gdnv[=b[skp]t"))
# output : ยังดีหน่า เกือบชิบหายละ
```

**ถ้าต้องการกำหนดว่าถ้าไม่รู้จักตัวอักขระนี้จะให้แทนที่ด้วยตัวอะไร**
```py
key_changer.en2th("👍", not_know = "?")
# output : ?
```

**ในการเรียกใช้ auto มันจะตรวจสอบว่ามีตัวอักขระภาษาไหนมากกว่า ถ้ามันพบว่าทั้สองฝั่งเท่ากัน มันจะเลือก en2th เป็นค่าเริ่มต้น แต่เราก็ยังสามารถกำหนดค่าเองได้**
```py
print(key_changer.auto("l;ylfu สบายดี", default = key_changer.EN2TH))
# output : สวัสดี สบายดี
```

**ตัวแปรกำหนดค่า default ของ key_changer.auto**
| ตัวแปร | แปลจาก | ไปเป็น |
| --- | --- | --- |
key_changer.EN2TH | QWERTY layout | Thai Kedmanee keyboard layout 
key_changer.TH2EN | Thai Kedmanee keyboard layout | QWERTY layout
