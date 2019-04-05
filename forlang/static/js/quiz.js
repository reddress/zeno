var htmlLang = document.documentElement.lang || "en";

var questions = [];
var prompt = "";

// http://stackoverflow.com/questions/3514784/what-is-the-best-way-to-detect-a-mobile-device-in-jquery
function isMobile() {
  return ('ontouchstart' in document.documentElement);
}

// global, call isMobile only once
var deviceIsMobile = isMobile();

var messages = {
  "complete": {
    "en": "Complete!",
    "pt": "Completo!",
  },
};

var currentQuestion = 0;

// used to control behavior of click on eraser and checkmark
var canErase = true;

function showQuestion() {
  // $("#prompt").html(questions[currentQuestion].prompt);
}

// global constant
var letterMap = {
  "ϊ": "Ϊ",
  "ϋ": "Ϋ",
  "ά": "Ά",
  "έ": "Έ",
  "ή": "Ή",
  "ί": "Ί",
  "ό": "Ό",
  "ύ": "Ύ",
  "ώ": "Ώ",
  "ε": "Ε",
  "ρ": "Ρ",
  "τ": "Τ",
  "υ": "Υ",
  "θ": "Θ",
  "ι": "Ι",
  "ο": "Ο",
  "π": "Π",
  "α": "Α",
  "σ": "Σ",
  "δ": "Δ",
  "φ": "Φ",
  "γ": "Γ",
  "η": "Η",
  "ξ": "Ξ",
  "κ": "Κ",
  "λ": "Λ",
  "ζ": "Ζ",
  "χ": "Χ",
  "ψ": "Ψ",
  "ω": "Ω",
  "β": "Β",
  "ν": "Ν",
  "μ": "Μ",
  
  "Ϊ": "ϊ",
  "Ϋ": "ϋ",
  "Ά": "ά",
  "Έ": "έ",
  "Ή": "ή",
  "Ί": "ί",
  "Ό": "ό",
  "Ύ": "ύ",
  "Ώ": "ώ",
  "Ε": "ε",
  "Ρ": "ρ",
  "Τ": "τ",
  "Υ": "υ",
  "Θ": "θ",
  "Ι": "ι",
  "Ο": "ο",
  "Π": "π",
  "Α": "α",
  "Σ": "σ",
  "Δ": "δ",
  "Φ": "φ",
  "Γ": "γ",
  "Η": "η",
  "Ξ": "ξ",
  "Κ": "κ",
  "Λ": "λ",
  "Ζ": "ζ",
  "Χ": "χ",
  "Ψ": "ψ",
  "Ω": "ω",
  "Β": "β",
  "Ν": "ν",
  "Μ": "μ",
};

// replace the first letter of the word with the opposite case
// (if lowercase, then capital, and vice versa)
function oppositeCase(word) {
  var firstLetter = word[0];
  var rest = word.slice(1);

  return letterMap[firstLetter] + rest;
}

// globally alter questions.answers to include the opposite lower/uppercase
// answer.

function addOppositeCase(question) {
  // make copy of questionAnswer
  var originalQuestionAnswer = question.answer.slice(0);
  
  // push opposite case of each answer to the "question.answer" array
  for (var i = 0; i < originalQuestionAnswer.length; i++) {
    question.answer.push(oppositeCase(originalQuestionAnswer[i]));
  }
}

for (var i = 0; i < questions.length; i++) {
  addOppositeCase(questions[i]);
}

function checkAnswer() {
  var answer = $("#answer").val().trim();
  var question = questions[currentQuestion];

  if ($.inArray(answer, question.answer) !== -1) {
    canErase = false;
    $("#result").html('<img src="/static/img/icons/checkmark.png" alt="check">');

    if (currentQuestion < questions.length - 1) {
      $("#nextQuestion").removeClass("hidden");
    } else {
      $("#prompt").html(messages["complete"][htmlLang]); 
      $("#back").removeClass("display-none");
      $("#nextQuestion").addClass("display-none");
    }
  } else if ($.inArray(answer, question.partial) !== -1) {
    canErase = false;
    $("#result").html('<img src="/static/img/icons/warning.png" alt="warning">');
    $("#nextQuestion").addClass("hidden");
  } else {
    canErase = true;
    $("#result").html('<img src="/static/img/icons/eraser.png" alt="erase">');
    $("#nextQuestion").addClass("hidden");
  }
}


$("#nextQuestion").click(function() {
  $("#answer").val("");
  checkAnswer();
  if (!deviceIsMobile) {
    $("#answer").focus();
  }

  currentQuestion++;
  showQuestion();
});

$("#showAnswer").click(function() {
  $("#answer").val(questions[currentQuestion].answer[0]);
  checkAnswer();
});

$("#result").click(function() {
  if (canErase) {
    $("#answer").val("");
    checkAnswer();
    if (!deviceIsMobile) {
      $("#answer").focus();
    }
  }
});

showQuestion();

