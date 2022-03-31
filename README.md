## Translate text from character keyboard layout.

- **key-changer - version 3.0**  

**GUI ready to use**  
- [py  version 0.5](https://github.com/keegang6705/en-th-keyboard-translator/blob/main/python_ui/en-th_key_ui.py)(for 2.0)  
- [exe version 0.5](https://github.com/keegang6705/en-th-keyboard-translator/blob/main/python_ui/key_trans_UI.exe)(for 2.0)  

---

**มันคืออะไร อันนี้ก็ไม่แน่ใจเหมือนกัน**  
-  สรุปแบบเข้าใจง่ายๆคือ มันคือการตัวแปลงข้อความที่พิมพ์แบบปกติ แต่ดันลืมเปลี่ยน keboard layout มันเลยทำให้ข้อความออกมาแปลกๆ ซึ่ง package นี้จะมี function ที่ใช้แปลข้อความจาก keyboard layout หนึ่งไปอีก layout หนึ่ง  

---

### Keyboard layout ที่รองรับ
| ANSI |
| --- |
| [QWERTY layout](https://en.wikipedia.org/wiki/QWERTY) |
| [Thai Kedmanee keyboard layout](https://en.wikipedia.org/wiki/Thai_Kedmanee_keyboard_layout) |
| [Thai Pattachote keyboard layout](https://en.wikipedia.org/wiki/Thai_Pattachote_keyboard_layout) |

---

### การติดตั้ง
**pip**
```bash
pip install key-changer
```
อัพเดทเป็น version 3.0 แล้ว 
  
[comment]: <> (version 3.0)  
---

### การเรียกใช้งาน

**เรียกใช้**

```py
# แปลง
key_changer.convert(text, lang_layout, to_lang_layout, standard_key_layout=, not_know=)
# แปลง แต่จะเลือกให้เองว่าจากภาษาไหนไปภาษาไหน แต่ก็ต้องการค่าที่ใช้ระบุ keyboard layout จากผู้ใช้งาน
key_changer.auto(text, en_layout, th_layout, standard_key_layout=, not_know=, default=)
# สลับ โดยข้อความที่ออกมาจะสลับเปลียนกันไปมา
key_changer.switch(text, lang_layout_1, lang_layout_2, standard_key_layout=, not_know=)
```

```py
import key_changer
from key_changer import EN2TH, TH2EN, ANSI_KEYBOARD, QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT, THAI_PATTACHOTE_LAYOUT

print(key_changer.convert("l;ylfu", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT))
# output : สวัสดี
print(key_changer.convert(";yoso7j' Cyogfbowxshv'oYhkc]h;r[;jkoYhkw,jws]", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT))
# output : วันหนึ่ง ฉันเดินไปห้องนํ้าแล้วพบว่านํ้าไม่ไหล

print(key_changer.convert("ทำ ฟืก เน ะน ฟืนะ้ำพ ิฟะ้พนนท", THAI_KEDMANEE_LAYOUT, QWERTY_LAYOUT))
# output : me and go to another bathroom
print(key_changer.convert("ห้ระม ะ้ำ ไฟะำพ กนำหืงะ ดสนไ", THAI_KEDMANEE_LAYOUT, QWERTY_LAYOUT))
# output : shit, the water doesn't flow

print(key_changer.auto("mew'fusojk wxshv'oYhkmujvnjodHwfh", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT))
# output : ทำไงดีหน่า ไปห้องนํ้าที่อื่นก็ได้
print(key_changer.auto("ดีแาม ไ้ำพำ ฟพำ ร เนรืเ ืำปะ", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT))
# output : fuck, where are i going next

print(key_changer.convert("ฉันก็ได้แต่นั่งรอหวังว่านํ้าจะไหล", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT))
# output : ฉันก็ได้แต่นั่งรอหวังว่านํ้าจะไหล

# คือการสลับแลกเปลี่ยนระหว่างกัน
print(key_changer.switch("ฟะ ะ้ฟะ ทนทำืะม vp^jfuqoYhkdHws]", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT))
# output : at that moment, อยู่ดีๆนํ้าก็ไหล
print(key_changer.switch("py'fusojk gdnv[=b[skp]t", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT))
# output : ยังดีหน่า เกือบชิบหายละ
```

**ถ้าต้องการกำหนดว่าถ้าไม่รู้จักตัวอักขระนี้จะให้แทนที่ด้วยตัวอะไร**
```py
print(key_changer.convert("👍", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT, not_know = "?"))
# output : ?
```

**ในการเรียกใช้ auto มันจะตรวจสอบว่ามีตัวอักขระภาษาไหนมากกว่า ถ้ามันพบว่าทั้งสองฝั่งเท่ากัน มันจะเลือก EN2TH เป็นค่าเริ่มต้น แต่เราก็ยังสามารถกำหนดค่าเองได้**
```py
print(key_changer.auto("l;ylfu สบายดี", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT, default = EN2TH))
# output : สวัสดี สบายดี
```

**ตอนนี้ในภาษาอังกฤษยังรองรับมาตรฐานคีย์บอร์ด ANSI**
```py
print(key_changer.auto("Cyow,jgxHowisivot", QWERTY_LAYOUT, THAI_KEDMANEE_LAYOUT, standard_key_layout = ANSI_KEYBOARD))
# output : ฉันไม่เป็นไรหรอนะ
```

**ตัวแปรกำหนดค่า**
| ชื่อ | ใช้ |
| --- | --- |
| EN2TH | default value of auto function |
| TH2EN | default value of auto function |
| ANSI_KEYBOARD | standard_key_layout |
| QWERTY_LAYOUT | layout |
| THAI_KEDMANEE_LAYOUT | layout |
| THAI_PATTACHOTE_LAYOUT | layout |
