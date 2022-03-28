# -*- encoding: utf-8 -*-

from .keyboard_map import *

len_range = range(94)
th_unicode_range  = 3585, 3675
en_unicode_range = 49, 126

def convert(text, lang_layout, to_lang_layout, standard_key_layout = standard_key_layout_default, not_know = not_know_default):
    text_ = ""
    for char in text:
        not_found = True
        for i in len_range:
            if char == keymap[standard_key_layout][lang_layout][i]:
                text_ += keymap[standard_key_layout][to_lang_layout][i]
                not_found = False
                break
        if not_found == True:
            if not_know == None:
                text_ += char
            else:
                text_ += not_know
    return text_

def auto(text, en_layout, th_layout, standard_key_layout = standard_key_layout_default, not_know = not_know_default, default = defualt_lang2lang):
    count_th = 0
    count_en = 0
    for char in text:
        unicode = ord(char)
        if unicode >= en_unicode_range[0] and unicode <= en_unicode_range[1]:
            count_en += 1
        elif unicode >= th_unicode_range[0] and unicode <= th_unicode_range[1]:
            count_th += 1
    if count_en > count_th:
        return convert(text, en_layout, th_layout, standard_key_layout = standard_key_layout, not_know = not_know)
    elif count_th > count_en:
        return convert(text, th_layout, en_layout, standard_key_layout = standard_key_layout, not_know = not_know)
    else:
        if default == EN2TH:
            return convert(text, en_layout, th_layout, standard_key_layout = standard_key_layout, not_know = not_know)
        elif default == TH2EN:
            return convert(text, th_layout, en_layout, standard_key_layout = standard_key_layout, not_know = not_know)
        else:
            raise ValueError("Invalid default")

def switch(text, lang_layout_1, lang_layout_2, standard_key_layout = standard_key_layout_default, not_know = not_know_default):
    text_ = ""
    for char in text:
        not_found = True
        for i in len_range:
            if char == keymap[standard_key_layout][lang_layout_1][i]:
                text_ += keymap[standard_key_layout][lang_layout_2][i]
                not_found = False
                break
            elif char == keymap[standard_key_layout][lang_layout_2][i]:
                text_ += keymap[standard_key_layout][lang_layout_1][i]
                not_found = False
                break
        if not_found == True:
            if not_know == None:
                text_ += char
            else:
                text_ += not_know
    return text_
