var htmlLang = document.documentElement.lang || "en";

// http://stackoverflow.com/questions/3514784/what-is-the-best-way-to-detect-a-mobile-device-in-jquery
function isMobile() {
  return ('ontouchstart' in document.documentElement);
}

// global, call isMobile only once
var deviceIsMobile = isMobile();

var grKBmessages = { 
  "accent-key": {
    "en": ";",
    "pt": "ç",
  }
}

// build keyboard
// see visual-keyboard-in-html.html

// returns: <div class="key" id="key_f">f<br>φ</div>

function buildKey(keyClass, id, english, greek) {
  if (keyClass === "spacer") {
    return '<div class="spacer"></div>';
  }
  
  if (keyClass !== "") {
    keyClass = " " + keyClass;
  }

  if (english !== "") {
    greek = "<br>" + greek;
  }

  var keyContent = "<span class='english'>" + english + "</span>" + greek;
  
  return '<div class="key' + keyClass + '" id="' + id + '">' + keyContent + '</div>';
}

// for use when clicking on Shift
function setKeyLabel(id, newLabel) {
  $("#" + id).html(newLabel);
}

function keyboardRow(keys) {
  var row = '<div class="keyboard-row">';

  for (var i = 0; i < keys.length; i++) {
    row += buildKey(keys[i].keyClass, keys[i].id, keys[i].english, keys[i].greek);
  }
  
  row += '</div>';
  return row;
}

var firstRow = [
  // { keyClass: "spacer", id: "", english: "", greek: "" },
  // { keyClass: "spacer", id: "", english: "", greek: "" },
  { keyClass: "combining", id: "key_apostrophe", english: "", greek: "<img src='/static/img/icons/combining-apostrophe.png' alt='c_ap'>" },
  { keyClass: "combining", id: "key_combining_accent", english: "", greek: "<img src='/static/img/icons/combining-accent.png' alt='c_acc'>" },
  { keyClass: "combining", id: "key_dash", english: "", greek: "-" },
  { keyClass: "accented", id: "key_i_dia", english: "", greek: "ϊ" },
  { keyClass: "accented", id: "key_u_dia", english: "", greek: "ϋ" },
  { keyClass: "accented", id: "key_i_dia_accented", english: "", greek: "ΐ" },
  { keyClass: "accented", id: "key_u_dia_accented", english: "", greek: "ΰ" },
];  

var secondRow = [
  // { keyClass: "spacer", id: "", english: "", greek: "" },
  { keyClass: "accented", id: "key_a_accented", english: "", greek: "ά" },
  { keyClass: "accented", id: "key_e_accented", english: "", greek: "έ" },
  { keyClass: "accented", id: "key_h_accented", english: "", greek: "ή" },
  { keyClass: "accented", id: "key_i_accented", english: "", greek: "ί" },
  { keyClass: "accented", id: "key_o_accented", english: "", greek: "ό" },
  { keyClass: "accented", id: "key_y_accented", english: "", greek: "ύ" },
  { keyClass: "accented", id: "key_w_accented", english: "", greek: "ώ" },
  { keyClass: "special", id: "key_backspace", english: "", greek: '<img src="/static/img/icons/leftarrow.png" alt="bksp">' },
];

var thirdRow = [
  { keyClass: "", id: "key_q", english: "q", greek: ";" },
  { keyClass: "", id: "key_w", english: "w", greek: "ς" },
  { keyClass: "", id: "key_e", english: "e", greek: "ε" },
  { keyClass: "", id: "key_r", english: "r", greek: "ρ" },
  { keyClass: "", id: "key_t", english: "t", greek: "τ" },
  { keyClass: "", id: "key_y", english: "y", greek: "υ" },
  { keyClass: "", id: "key_u", english: "u", greek: "θ" },
  { keyClass: "", id: "key_i", english: "i", greek: "ι" },
  { keyClass: "", id: "key_o", english: "o", greek: "ο" },
  { keyClass: "", id: "key_p", english: "p", greek: "π" },
];

var fourthRow = [
  // { keyClass: "spacer", id: "", english: "", greek: "" },
  { keyClass: "", id: "key_a", english: "a", greek: "α" },
  { keyClass: "", id: "key_s", english: "s", greek: "σ" },
  { keyClass: "", id: "key_d", english: "d", greek: "δ" },
  { keyClass: "", id: "key_f", english: "f", greek: "φ" },
  { keyClass: "", id: "key_g", english: "g", greek: "γ" },
  { keyClass: "", id: "key_h", english: "h", greek: "η" },
  { keyClass: "", id: "key_j", english: "j", greek: "ξ" },
  { keyClass: "", id: "key_k", english: "k", greek: "κ" },
  { keyClass: "", id: "key_l", english: "l", greek: "λ" },
  { keyClass: "", id: "key_;", english: grKBmessages["accent-key"][htmlLang], greek: "΄" },
];

var fifthRow = [
  // { keyClass: "shift", id: "key_shift", english: '<img src="/static/img/icons/uparrow.png">', greek: '_' },
  { keyClass: "shift", id: "key_shift", english: '', greek: '<img src="/static/img/icons/uparrow.png">' },
  { keyClass: "", id: "key_z", english: "z", greek: "ζ" },
  { keyClass: "", id: "key_x", english: "x", greek: "χ" },
  { keyClass: "", id: "key_c", english: "c", greek: "ψ" },
  { keyClass: "", id: "key_v", english: "v", greek: "ω" },
  { keyClass: "", id: "key_b", english: "b", greek: "β" },
  { keyClass: "", id: "key_n", english: "n", greek: "ν" },
  { keyClass: "", id: "key_m", english: "m", greek: "μ" },
  { keyClass: "shift", id: "key_shift_right", english: '', greek: '<img src="/static/img/icons/uparrow.png">' },
];

var sixthRow = [
  // { keyClass: "spacer", id: "", english: "", greek: "" },
  // { keyClass: "spacer", id: "", english: "", greek: "" },
  { keyClass: "space", id: "key_space", english: "", greek: "Space" },
];

$("#visual-keyboard").append(keyboardRow(firstRow));
$("#visual-keyboard").append(keyboardRow(secondRow));
$("#visual-keyboard").append(keyboardRow(thirdRow));
$("#visual-keyboard").append(keyboardRow(fourthRow));
$("#visual-keyboard").append(keyboardRow(fifthRow));
$("#visual-keyboard").append(keyboardRow(sixthRow));

// global variable, document.activeElement seems to take the div as the active
// element as it is clicked.

var focusedId = $('input')[0].id;  // by default, take first input element

$("input").focus(function() {
  focusedId = $(this)[0].id;
});

function removeSelection() {
  var selectStart = $("#answer")[0].selectionStart;
  var selectEnd = $("#answer")[0].selectionEnd

  if (selectEnd - selectStart > 0) {
    var text = $("#answer").val();
    $("#answer").val(text.slice(0, selectStart) + text.slice(selectEnd));
    $("#answer")[0].setSelectionRange(selectStart, selectStart);
    return true;
  }
}

// shift between uppercase (1) and lowercase (0)
var isUpper = 0;

$("div.key").click(function() {
  var keyId = $(this)[0].id;
  
  if (keyId === "key_shift") {
    isUpper = 1 - isUpper;
    relabelKeys();
    return;
  }

  if (keyId === "key_shift_right") {
    isUpper = 1 - isUpper;
    relabelKeys();
    return;
  }

  // global variable to manually keep track of last input selected
  // var focused = $("#" + focusedId);

  // always use #answer as the focused item
  var focused = $("#answer");


  // remove selection, if any
  var removedSelection = removeSelection();

  var caretPos = focused[0].selectionStart;
  
  var text = focused.val();

  // insert Greek letter, [0] refers to lowercase in keymap's array
  text = text.slice(0, caretPos) + keyMap[keyId][isUpper] + text.slice(caretPos);

  // return to lowercase
  if (isUpper === 1) {
    isUpper = 0;
    relabelKeys();
  }

  var chars = text.split("");
  
  // single characters
  for (var i = 0; i < text.length; i++) {
    chars[i] = charMap[chars[i]] || chars[i];
  }

  focused.val(chars.join(""));

  // replace characters to account for possible accents
  focused.val(replaceChars(focused.val()));

  // move caret position forward
  focused[0].setSelectionRange(caretPos + 1, caretPos + 1);

  //// TEST IF MOBILE KEYBOARD DOES NOT APPEAR
  // focused[0].focus();

  // clear if button was clicked
  if (keyId === "key_clear") {
    focused.val("");
  }

  if (keyId === "key_backspace") {
    var newCaretPos = caretPos;
    if (!removedSelection) {
      var textBeforeBackspace = focused.val();
      focused.val(textBeforeBackspace.slice(0, Math.max(0, caretPos-1)) + textBeforeBackspace.slice(caretPos));
      newCaretPos = Math.max(0, caretPos - 1);
    }
    focused[0].setSelectionRange(newCaretPos, newCaretPos);
  }

  // animate color change
  if (!$(this).hasClass("special")) {
    var thisKey = $(this);
    thisKey.addClass("highlight");
    window.setTimeout(function() {
      thisKey.removeClass("highlight");
    }, 100);
  }

  //// refocus
  // $("#answer").focus();

  // hide soft keyboard, remove caret from answer text box
  if (deviceIsMobile) {
    document.activeElement.blur();
  }
  
  //  checkAnswer();
});


// shift between uppercase and lowercase
function relabelKeys() {
  if (isUpper === 1) {
    setKeyLabel("key_i_dia", "Ϊ");
    setKeyLabel("key_u_dia", "Ϋ");
    setKeyLabel("key_i_dia_accented", "_");
    setKeyLabel("key_u_dia_accented", "_");

    setKeyLabel("key_a_accented", "Ά");
    setKeyLabel("key_e_accented", "Έ");
    setKeyLabel("key_h_accented", "Ή");
    setKeyLabel("key_i_accented", "Ί");
    setKeyLabel("key_o_accented", "Ό");
    setKeyLabel("key_y_accented", "Ύ");
    setKeyLabel("key_w_accented", "Ώ");
    
    setKeyLabel("key_q", "<span class='english'>Q</span><br>;");
    setKeyLabel("key_w", "<span class='english'>W</span><br>Σ");
    setKeyLabel("key_e", "<span class='english'>E</span><br>Ε");
    setKeyLabel("key_r", "<span class='english'>R</span><br>Ρ");
    setKeyLabel("key_t", "<span class='english'>T</span><br>Τ");
    setKeyLabel("key_y", "<span class='english'>Y</span><br>Υ");
    setKeyLabel("key_u", "<span class='english'>U</span><br>Θ");
    setKeyLabel("key_i", "<span class='english'>I</span><br>Ι");
    setKeyLabel("key_o", "<span class='english'>O</span><br>Ο");
    setKeyLabel("key_p", "<span class='english'>P</span><br>Π");

    setKeyLabel("key_a", "<span class='english'>A</span><br>Α");
    setKeyLabel("key_s", "<span class='english'>S</span><br>Σ");
    setKeyLabel("key_d", "<span class='english'>D</span><br>Δ");
    setKeyLabel("key_f", "<span class='english'>F</span><br>Φ");
    setKeyLabel("key_g", "<span class='english'>G</span><br>Γ");
    setKeyLabel("key_h", "<span class='english'>H</span><br>Η");
    setKeyLabel("key_j", "<span class='english'>J</span><br>Ξ");
    setKeyLabel("key_k", "<span class='english'>K</span><br>Κ");
    setKeyLabel("key_l", "<span class='english'>L</span><br>Λ");

    setKeyLabel("key_z", "<span class='english'>Z</span><br>Ζ");
    setKeyLabel("key_x", "<span class='english'>X</span><br>Χ");
    setKeyLabel("key_c", "<span class='english'>C</span><br>Ψ");
    setKeyLabel("key_v", "<span class='english'>V</span><br>Ω");
    setKeyLabel("key_b", "<span class='english'>B</span><br>Β");
    setKeyLabel("key_n", "<span class='english'>N</span><br>Ν");
    setKeyLabel("key_m", "<span class='english'>M</span><br>Μ");
  } else {
    setKeyLabel("key_i_dia", "ϊ");
    setKeyLabel("key_u_dia", "ϋ");
    setKeyLabel("key_i_dia_accented", "ΐ");
    setKeyLabel("key_u_dia_accented", "ΰ");

    setKeyLabel("key_a_accented", "ά");
    setKeyLabel("key_e_accented", "έ");
    setKeyLabel("key_h_accented", "ή");
    setKeyLabel("key_i_accented", "ί");
    setKeyLabel("key_o_accented", "ό");
    setKeyLabel("key_y_accented", "ύ");
    setKeyLabel("key_w_accented", "ώ");
    
    setKeyLabel("key_q", "<span class='english'>q</span><br>;");
    setKeyLabel("key_w", "<span class='english'>w</span><br>ς");
    setKeyLabel("key_e", "<span class='english'>e</span><br>ε");
    setKeyLabel("key_r", "<span class='english'>r</span><br>ρ");
    setKeyLabel("key_t", "<span class='english'>t</span><br>τ");
    setKeyLabel("key_y", "<span class='english'>y</span><br>υ");
    setKeyLabel("key_u", "<span class='english'>u</span><br>θ");
    setKeyLabel("key_i", "<span class='english'>i</span><br>ι");
    setKeyLabel("key_o", "<span class='english'>o</span><br>ο");
    setKeyLabel("key_p", "<span class='english'>p</span><br>π");

    setKeyLabel("key_a", "<span class='english'>a</span><br>α");
    setKeyLabel("key_s", "<span class='english'>s</span><br>σ");
    setKeyLabel("key_d", "<span class='english'>d</span><br>δ");
    setKeyLabel("key_f", "<span class='english'>f</span><br>φ");
    setKeyLabel("key_g", "<span class='english'>g</span><br>γ");
    setKeyLabel("key_h", "<span class='english'>h</span><br>η");
    setKeyLabel("key_j", "<span class='english'>j</span><br>ξ");
    setKeyLabel("key_k", "<span class='english'>k</span><br>κ");
    setKeyLabel("key_l", "<span class='english'>l</span><br>λ");

    setKeyLabel("key_z", "<span class='english'>z</span><br>ζ");
    setKeyLabel("key_x", "<span class='english'>x</span><br>χ");
    setKeyLabel("key_c", "<span class='english'>c</span><br>ψ");
    setKeyLabel("key_v", "<span class='english'>v</span><br>ω");
    setKeyLabel("key_b", "<span class='english'>b</span><br>β");
    setKeyLabel("key_n", "<span class='english'>n</span><br>ν");
    setKeyLabel("key_m", "<span class='english'>m</span><br>μ");
  }
}

