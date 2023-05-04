from typing import get_args
from re import compile, Pattern

from .layout_map import KeyboardsType, LanguagesType, LayoutMap

KeyboardLayout: tuple[str] = get_args(KeyboardsType)
LanguageLayout: tuple[str] = get_args(LanguagesType)

class KeyChanger:
    def __init__(self, key_layout: KeyboardsType, lang_1: LanguagesType, lang_2: LanguagesType) -> None:
        self.key_layout: str = key_layout
        self.lang_1: str = lang_1
        self.lang_2: str = lang_2

        self.lang_1_pattern: Pattern
        self.lang_2_pattern: Pattern
        lang_1_map: str
        lang_2_map: str

        if self.key_layout in LayoutMap:
            if self.lang_1 in LayoutMap[self.key_layout]:
                _ = LayoutMap[self.key_layout][self.lang_1]
                self.lang_1_pattern = compile(_[0])
                lang_1_map = _[1]
            else:
                raise ValueError("Language not found: " + self.lang_1)

            if self.lang_2 in LayoutMap[self.key_layout]:
                _ = LayoutMap[self.key_layout][self.lang_2]
                self.lang_2_pattern = compile(_[0])
                lang_2_map = _[1]
            else:
                raise ValueError("Language not found: " + self.lang_2)
        else:
            raise ValueError("Keyboard layout not found: " + self.key_layout)

        self.translation_table_1to2 = str.maketrans(lang_1_map, lang_2_map)
        self.translation_table_2to1 = str.maketrans(lang_2_map, lang_1_map)

    def translate(self, string: str) -> str:
        return string.translate(self.translation_table_1to2)

    __call__ = translate

    def reverse(self, string) -> str:
        return string.translate(self.translation_table_2to1)

    def auto(self, string) -> str:
        lang_1_count = 0
        lang_2_count = 0

        for c in string:
            if self.lang_1_pattern.match(c):
                lang_1_count += 1
            elif self.lang_2_pattern.match(c):
                lang_2_count += 1

        if lang_2_count > lang_1_count:
            return string.translate(self.translation_table_2to1)
        else:
            return string.translate(self.translation_table_1to2)
