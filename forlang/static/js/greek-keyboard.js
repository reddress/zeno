var codeMap = {
  "81": ":", "87": "Σ", "69": "Ε", "82": "Ρ", "84": "Τ", "89": "Υ", "85": "Θ", "73": "Ι", "79": "Ο", "80": "Π",
  "65": "Α", "83": "Σ", "68": "Δ", "70": "Φ", "71": "Γ", "72": "Η", "74": "Ξ", "75": "Κ", "76": "Λ",
  "90": "Ζ", "88": "Χ", "67": "Ψ", "86": "Ω", "66": "Β", "78": "Ν", "77": "Μ",
  "113": ";", "119": "ς",  "101": "ε",  "114": "ρ",  "116": "τ",  "121": "υ",  "117": "θ",  "105": "ι",  "111": "ο",  "112": "π",
  "97": "α", "115": "σ", "100": "δ", "102": "φ", "103": "γ", "104": "η", "106": "ξ", "107": "κ", "108": "λ",

  "122": "ζ", "120": "χ", "99": "ψ", "118": "ω", "98": "β", "110": "ν", "109": "μ",  
};

$(".greek-keyboard").keypress(function(event) {
  var code = (event.keyCode ? event.keyCode : event.which);
  var codeStr = code.toString();
  
  // console.log(code);
  var codesInput = $("#codes");
  codesInput.val(codesInput.val() + code + " ");

  // Accents
  // ; = 59
  // ' = 39

  // " = 58

  // boolean to turn on accent mode?
  
  if ((code >= 65 && code <= 90) || (code >= 97 && code <= 122)) {
    event.preventDefault();  // do not enter regular letter

    // insert simple letter only if present in codeMap
    if (codeMap[codeStr]) {
      // no good, only appends at end
      // $(this).val($(this).val() + codeMap[codeStr]);
      
      
      // delete selected text
      var currentText = $(this).val();
      console.log(window.getSelection());
      
      
      // http://stackoverflow.com/questions/1064089/inserting-a-text-where-cursor-is-using-javascript-jquery
      var caretPos = $(this)[0].selectionStart;
      // console.log(caretPos);
      
      currentText = $(this).val();

      $(this).val(currentText.substring(0, caretPos) + codeMap[codeStr] + currentText.substring(caretPos));

      // http://stackoverflow.com/questions/512528/set-cursor-position-in-html-textbox
      $(this)[0].setSelectionRange(caretPos + 1, caretPos + 1);
    }
  }
  
});
