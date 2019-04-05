// when clicked, a key must produce the right character for the current state:
// 0: lowercase
// 1: uppercase (shift)
// 2: lowercase accented (; or cedilha)
// 3: uppercase accented 

var keyMap = {
  
  "key_q": [";", ";", ";", ";"],
  "key_w": ["ς", "Σ", "ς", "Σ"],
  "key_e": ["ε", "Ε", "έ", "Έ"],
  "key_r": ["ρ", "Ρ", "ρ", "Ρ"],
  "key_t": ["τ", "Τ", "τ", "Τ"],
  "key_y": ["υ", "Υ", "ύ", "Ύ"],
  "key_u": ["θ", "Θ", "θ", "Θ"],
  "key_i": ["ι", "Ι", "ί", "Ί"],
  "key_o": ["ο", "Ο", "ό", "Ό"],
  "key_p": ["π", "Π", "π", "Π"],

  "key_a": ["α", "Α", "ά", "Ά"],
  "key_s": ["σ", "Σ", "σ", "Σ"],
  "key_d": ["δ", "Δ", "δ", "Δ"],
  "key_f": ["φ", "Φ", "φ", "Φ"],
  "key_g": ["γ", "Γ", "γ", "Γ"],
  "key_h": ["η", "Η", "ή", "Ή"],
  "key_j": ["ξ", "Ξ", "ξ", "Ξ"],
  "key_k": ["κ", "Κ", "κ", "Κ"],
  "key_l": ["λ", "Λ", "λ", "Λ"],

  "key_z": ["ζ", "Ζ", "ζ", "Ζ"],
  "key_x": ["χ", "Χ", "χ", "Χ"],
  "key_c": ["ψ", "Ψ", "ψ", "Ψ"],
  "key_v": ["ω", "Ω", "ώ", "Ώ"],
  "key_b": ["β", "Β", "β", "Β"],
  "key_n": ["ν", "Ν", "ν", "Ν"],
  "key_m": ["μ", "Μ", "μ", "Μ"],
  "key_;": ["΄", "΄", "΄", "΄"],


  "key_a_accented": ["ά", "Ά", "ά", "ά"],
  "key_e_accented": ["έ", "Έ", "έ", "έ"],
  "key_h_accented": ["ή", "Ή", "ή", "ή"],
  "key_i_accented": ["ί", "Ί", "ί", "ί"],
  "key_o_accented": ["ό", "Ό", "ό", "ό"],
  "key_y_accented": ["ύ", "Ύ", "ύ", "ύ"],
  "key_w_accented": ["ώ", "Ώ", "ώ", "ώ"],

  "key_i_dia": ["ϊ", "Ϊ", "ϊ", "ϊ"],
  "key_u_dia": ["ϋ", "Ϋ", "ϋ", "ϋ"],
  "key_i_dia_accented": ["ΐ", "", "ΐ", "ΐ"],
  "key_u_dia_accented": ["ΰ", "", "ΰ", "ΰ"],  

  "key_apostrophe": ["'", "'", "'", "'"],
  "key_combining_accent": ["΄", "΄", "΄", "΄"],
  "key_dash": ["-", "-", "-", "-"],

  "key_shift": ["", "", "", ""],
  "key_clear": ["", "", "", ""],
  "key_backspace": ["", "", "", ""],
  "key_space": [" ", " ", " ", " "],

};
