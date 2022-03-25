# -*- encoding: utf-8 -*-

eng = [
    '`', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '0', '-', '=', 'q', 'w', 'e', 'r', 't', 'y', 'u',
    'i', 'o', 'p', '[', ']', '\\', 'a', 's', 'd', 'f',
    'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c',
    'v', 'b', 'n', 'm', ',', '.', '/', '~', '!', '@',
    '#', '$', '%', '^', '&', '*', '(', ')', '_', '+',
    'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
    '{', '}', '|', 'A', 'S', 'D', 'F', 'G', 'H', 'J',
    'K', 'L', ':', '"', 'Z', 'X', 'C', 'V', 'B', 'N',
    'M', '<', '>', '?'
]

thai = [
    '_', 'ๅ', '/', '-', 'ภ', 'ถ', 'ุ', 'ึ', 'ค', 'ต',
    'จ', 'ข', 'ช', 'ๆ', 'ไ', 'ำ', 'พ', 'ะ', 'ั', 'ี',
    'ร', 'น', 'ย', 'บ', 'ล', 'ฃ', 'ฟ', 'ห', 'ก', 'ด',
    'เ', '้', '่', 'า', 'ส', 'ว', 'ง', 'ผ', 'ป', 'แ',
    'อ', 'ิ', 'ื', 'ท', 'ม', 'ใ', 'ฝ', '%', '+', '๑',
    '๒', '๓', '๔', 'ู', '฿', '๕', '๖', '๗', '๘', '๙',
    '๐', '\"', 'ฎ', 'ฑ', 'ธ', 'ํ', '๊', 'ณ', 'ฯ', 'ญ',
    'ฐ', ',', 'ฅ', 'ฤ', 'ฆ', 'ฏ', 'โ', 'ฌ', '็', '๋',
    'ษ', 'ศ', 'ซ', '.', '(', ')', 'ฉ', 'ฮ', 'ฺ', '์',
    '?', 'ฒ', 'ฬ', 'ฦ'
]

EN2TH = 1
TH2EN = 2

len_range = range(94)
th_unicode_range  = 3585, 3675
en_unicode_range = 49, 126

def convert(text, l1, l2, not_know = None):
    text_ = ""
    for char in text:
        not_found = True
        for i in len_range:
            if char == l1[i]:
                text_ += l2[i]
                not_found = False
                break
        if not_found == True:
            if not_know == None:
                text_ += char
            else:
                text_ += not_know
    return text_

def en2th(text, not_know = None):
    return convert(text, eng, thai, not_know)

def th2en(text, not_know = None):
    return convert(text, thai, eng, not_know)

def auto(text, not_know = None, default = EN2TH):
    count_th = 0
    count_en = 0
    for char in text:
        unicode = ord(char)
        if unicode > en_unicode_range[0] and unicode < en_unicode_range[1]:
            count_en += 1
        elif unicode > th_unicode_range[0] and unicode < th_unicode_range[1]:
            count_th += 1
    if count_en > count_th:
        return convert(text, eng, thai, not_know)
    elif count_en < count_th:
        return convert(text, thai, eng, not_know)
    else:
        if default == EN2TH:
            return convert(text, eng, thai, not_know)
        elif default == TH2EN:
            return convert(text, eng, thai, not_know)

def switch(text, not_know = None):
    text_ = ""
    for char in text:
        not_found = True
        for i in len_range:
            if char == eng[i]:
                text_ += thai[i]
                not_found = False
                break
            elif char == thai[i]:
                text_ += eng[i]
                not_found = False
                break
        if not_found == True:
            if not_know == None:
                text_ += char
            else:
                text_ += not_know
    return text_
