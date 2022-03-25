eng = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?']
thai = ['_', 'ๅ', '/', '-', 'ภ', 'ถ', 'ุ', 'ึ', 'ค', 'ต', 'จ', 'ข', 'ช', 'ๆ', 'ไ', 'ำ', 'พ', 'ะ', 'ั', 'ี', 'ร', 'น', 'ย', 'บ', 'ล', 'ฃ', 'ฟ', 'ห', 'ก', 'ด', 'เ', '้', '่', 'า', 'ส', 'ว', 'ง', 'ผ', 'ป', 'แ', 'อ', 'ิ', 'ื', 'ท', 'ม', 'ใ', 'ฝ', '%', '+', '๑', '๒', '๓', '๔', 'ู', '฿', '๕', '๖', '๗', '๘', '๙', '๐', '"', 'ฎ', 'ฑ', 'ธ', 'ํ', '๊', 'ณ', 'ฯ', 'ญ', 'ฐ', ',', 'ฅ', 'ฤ', 'ฆ', 'ฏ', 'โ', 'ฌ', '็', '๋', 'ษ', 'ศ', 'ซ', '.', '(', ')', 'ฉ', 'ฮ', 'ฺ', '์', '?', 'ฒ', 'ฬ', 'ฦ']

def change_key(text,type="auto1"):
  type_ = ["auto1","auto2","th>en","en>th","TH>EN","EN>TH"]
  if type not in type_:
        raise ValueError(f"Invalid type. Expected one of:{type_}")
  output =""
  for i in text:
      if type == "auto1":
            if i in eng:
                char = thai[eng.index(i)]
            elif i in thai:
                char = eng[thai.index(i)]
            else:
                char = " "
            output = str(output+char)
      if type == "auto2":
            if i in thai:
                char = eng[thai.index(i)]
            elif i in eng:
                char = thai[eng.index(i)]
            else:
                char = " "
            output = str(output+char)
      elif type == "th>en" or type == "TH>EN":
            if i in thai:
                char = eng[thai.index(i)]
            else:
                char = " "
            output = str(output+char)
      elif type == "en>th" or type == "EN>TH":
            if i in eng:
                char = thai[eng.index(i)]
            else:
                char = " "
            output = str(output+char)
  return output

