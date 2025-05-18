  const keymap = {
    en: '`1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?',
    th: '_ๅ/-ภถุึคตจขชๆไำพะัีรนยบลฃฟหกดเ้่าสวงผปแอิืทมใฝ%+๑๒๓๔ู฿๕๖๗๘๙๐"ฎฑธํ๊ณฯญฐ,ฅฤฆฏโฌ็๋ษศซ.()ฉฮฺ์?ฒฬฦ',
    th2: '_=๒๓๔๕ู๗๘๙๐๑๖็ตยอร่ดมวแใฌฺ้ทงกัีานเไขบปลหิคสะจพ฿+"/,?ุๅ.()-%๊ฤๆญษึฝซถฒฯฦํ๋ธำณ์ืผชโฆฑฎฏฐภัศฮฟฉฬ',
  }

function translate(input, selectedOption=Auto) {
  var result = "";

  for (var i = 0; i < input.length; i++) {
    var char = input[i];
    var translatedChar = char;

    if (selectedOption === "Auto") {
      var enIndex = keymap.en.indexOf(char);
      var thIndex = keymap.th.indexOf(char);
      if (enIndex !== -1) {
        translatedChar = keymap.th[enIndex];
      } else if (thIndex !== -1) {
        translatedChar = keymap.en[thIndex];
      }
    } else if (selectedOption === "ENtoTH") {
      var index = keymap.en.indexOf(char);
      if (index !== -1) {
        translatedChar = keymap.th[index];
      }
    } else if (selectedOption === "THtoEN") {
      var index = keymap.th.indexOf(char);
      if (index !== -1) {
        translatedChar = keymap.en[index];
      }
    }

    result += translatedChar;
  }

  return result;
}
