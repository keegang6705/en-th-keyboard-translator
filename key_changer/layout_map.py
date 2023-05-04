from typing import Literal

KeyboardsType = Literal["ANSI"]
LanguagesType = Literal["QWERTY", "Thai_Kedmanee", "Thai_Pattachote"]

LayoutMap = {
    "ANSI": {
        "QWERTY": (
            r'[a-zA-Z]',
            '`1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'    
        ),
        "Thai_Kedmanee": (
            r'[\u0E01-\u0E7F]',
            '_ๅ/-ภถุึคตจขชๆไำพะัีรนยบลฃฟหกดเ้่าสวงผปแอิืทมใฝ%+๑๒๓๔ู฿๕๖๗๘๙๐"ฎฑธํ๊ณฯญฐ,ฅฤฆฏโฌ็๋ษศซ.()ฉฮฺ์?ฒฬฦ'
        ),
        "Thai_Pattachote": (
            r'[\u0E01-\u0E7F]',
            '_=๒๓๔๕ู๗๘๙๐๑๖็ตยอร่ดมวแใฌฺ้ทงกัีานเไขบปลหิคสะจพ฿+"/,?ุๅ.()-%๊ฤๆญษึฝซถฒฯฦํ๋ธำณ์ืผชโฆฑฎฏฐภัศฮฟฉฬ'
        )
    }
}
