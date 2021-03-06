// keyboard is too complex, need to capture Ctrl-C, F5 reload, etc.
// giving up for now, and using simpler idea of replacing character by character

// replace two-character accent letters first
// in portuguese keyboards, since cedilha is next to L, it should also act
// as an accent prefix key

// semicolon, cedilha, and accent mark
var accentMap = {
  ";a": "ά",
  ";e": "έ",
  ";h": "ή",
  ";i": "ί",
  ";o": "ό",
  ";y": "ύ",
  ";v": "ώ",

  "ça": "ά",
  "çe": "έ",
  "çh": "ή",
  "çi": "ί",
  "ço": "ό",
  "çy": "ύ",
  "çv": "ώ",

  // "'a": "ά",
  // "'e": "έ",
  // "'h": "ή",
  // "'i": "ί",
  // "'o": "ό",
  // "'y": "ύ",
  // "'v": "ώ",

  // "΄a": "ά",
  // "΄e": "έ",
  // "΄h": "ή",
  // "΄i": "ί",
  // "΄o": "ό",
  // "΄y": "ύ",
  // "΄v": "ώ",

  "΄α": "ά",
  "΄ε": "έ",
  "΄η": "ή",
  "΄ι": "ί",
  "΄ο": "ό",
  "΄υ": "ύ",
  "΄ω": "ώ",

  "çα": "ά",
  "çε": "έ",
  "çη": "ή",
  "çι": "ί",
  "çο": "ό",
  "çυ": "ύ",
  "çω": "ώ",

  ";α": "ά",
  ";ε": "έ",
  ";η": "ή",
  ";ι": "ί",
  ";ο": "ό",
  ";υ": "ύ",
  ";ω": "ώ",

  // "'α": "ά",
  // "'ε": "έ",
  // "'η": "ή",
  // "'ι": "ί",
  // "'ο": "ό",
  // "'υ": "ύ",
  // "'ω": "ώ",


  
  ";A": "Ά",
  ";E": "Έ",
  ";H": "Ή",
  ";I": "Ί",
  ";O": "Ό",
  ";Y": "Ύ",
  ";V": "Ώ",

  "çA": "Ά",
  "çE": "Έ",
  "çH": "Ή",
  "çI": "Ί",
  "çO": "Ό",
  "çY": "Ύ",
  "çV": "Ώ",

  "ÇA": "Ά",
  "ÇE": "Έ",
  "ÇH": "Ή",
  "ÇI": "Ί",
  "ÇO": "Ό",
  "ÇY": "Ύ",
  "ÇV": "Ώ",

  // "'A": "Ά",
  // "'E": "Έ",
  // "'H": "Ή",
  // "'I": "Ί",
  // "'O": "Ό",
  // "'Y": "Ύ",
  // "'V": "Ώ",

  // "΄A": "Ά",
  // "΄E": "Έ",
  // "΄H": "Ή",
  // "΄I": "Ί",
  // "΄O": "Ό",
  // "΄Y": "Ύ",
  // "΄V": "Ώ",

  "΄Α": "Ά",
  "΄Ε": "Έ",
  "΄Η": "Ή",
  "΄Ι": "Ί",
  "΄Ο": "Ό",
  "΄Υ": "Ύ",
  "΄Ω": "Ώ",

  "çΑ": "Ά",
  "çΕ": "Έ",
  "çΗ": "Ή",
  "çΙ": "Ί",
  "çΟ": "Ό",
  "çΥ": "Ύ",
  "çΩ": "Ώ",

  "ÇΑ": "Ά",
  "ÇΕ": "Έ",
  "ÇΗ": "Ή",
  "ÇΙ": "Ί",
  "ÇΟ": "Ό",
  "ÇΥ": "Ύ",
  "ÇΩ": "Ώ",

  ";Α": "Ά",
  ";Ε": "Έ",
  ";Η": "Ή",
  ";Ι": "Ί",
  ";Ο": "Ό",
  ";Υ": "Ύ",
  ";Ω": "Ώ",
  
  // "'Α": "Ά",
  // "'Ε": "Έ",
  // "'Η": "Ή",
  // "'Ι": "Ί",
  // "'Ο": "Ό",
  // "'Υ": "Ύ",
  // "'Ω": "Ώ",
};

// replace cedilha and semi-colon to better-looking ' accent mark
var accentKeysMap = {
  // "'": "΄",  // apostrophe is used in απ' το and μ' αρέσει
  // ";": "΄",  // ; is the Greek question mark
  "ç": "΄",
  "Ç": "΄",
  "´": "΄",
};

var charMap = {
  "q": ";", "w": "ς", "e": "ε", "r": "ρ", "t": "τ", "y": "υ", "u": "θ", "i": "ι", "o": "ο", "p": "π",
  "a": "α", "s": "σ", "d": "δ", "f": "φ", "g": "γ", "h": "η", "j": "ξ", "k": "κ", "l": "λ",
  "z": "ζ", "x": "χ", "c": "ψ", "v": "ω", "b": "β", "n": "ν", "m": "μ",
  "Q": ";", "W": "Σ", "E": "Ε", "R": "Ρ", "T": "Τ", "Y": "Υ", "U": "Θ", "I": "Ι", "O": "Ο", "P": "Π",
  "A": "Α", "S": "Σ", "D": "Δ", "F": "Φ", "G": "Γ", "H": "Η", "J": "Ξ", "K": "Κ", "L": "Λ",
  "Z": "Ζ", "X": "Χ", "C": "Ψ", "V": "Ω", "B": "Β", "N": "Ν", "M": "Μ",
};
