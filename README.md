# key-changer

Translate characters caused by typos because you forgot to change the keyboard language layout.

## Install
```
pip install key-changer
```

## Command
```
python3 -m key_changer --help
```

## Example
```python
import key_changer

translator = key_changer.KeyChanger("ANSI", "QWERTY", "Thai_Kedmanee")

translator.translate("l;ylfu")
# 'สวัสดี'

translator.reverse("้ำสสน")
# 'hello'

translator.auto(";yoouhvkdkLfu")
# 'วันนี้อากาศดี'

translator.auto("ะนกฟั ะ้ำ ไำฟะ้ำพ รห เนนก")
# 'today the weather is good'

key_changer.KeyboardLayout
# ('ANSI',)

key_changer.LanguageLayout
# ('QWERTY', 'Thai_Kedmanee', 'Thai_Pattachote')
```

---

## Current support

<table>
    <thead>
        <tr>
            <th>Keyboard layout</th>
            <th>Language layout</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=3>ANSI</td>
            <td>QWERTY</td>
        </tr>
        <tr>
            <td>Thai_Kedmanee</td>
        </tr>
        <tr>
            <td>Thai_Pattachote</td>
        </tr>
    </tbody>
</table>
