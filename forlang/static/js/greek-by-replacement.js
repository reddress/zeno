function replaceChars(text) {
  // first, replace accented letters
  for (var raw in accentMap) {
    text = text.replace(raw, accentMap[raw]);
  }
  
  // XXX
  
  var chars = text.split("");

  
  // single characters
  for (var i = 0; i < text.length; i++) {
    chars[i] = charMap[chars[i]] || chars[i];
  }
  return chars.join("");
}

$(".greek-keyboard").keyup(function(event) {
  var code = (event.keyCode ? event.keyCode : event.which);

  // left, right arrows, shift, home, end, tab
  if (code === 37 || code == 39 || code == 16 || code == 35 || code == 36 || code == 9) {
    return;
  }

  //// Check keycode
  // console.log(code);
  
  // if ((code >= 65 && code <= 90) || (code >= 97 && code <= 122) || code == 222) {
  var caretPos = $(this)[0].selectionStart;

  // console.log(caretPos);
  
  var text = $(this).val();
  
  $(this).val(replaceChars(text));

  // keep caret position
  $(this)[0].setSelectionRange(caretPos, caretPos);

  //  }  // end if

  // for use in quiz 
  // checkAnswer();
});
