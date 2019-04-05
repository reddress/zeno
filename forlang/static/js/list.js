$("#quizTitle").html(title);

var list = $("#list");

for (var i = 0; i < questions.length; i++) {
  var answers = questions[i].answer.join(" / ");
  list.append("<tr>");

  // if needed later, <td>" + (i + 1) + ".</td> produces line number
  list.append("<td>" + questions[i].prompt +
              "</td><td class='list-answer'>" + answers + "</td>");
  list.append("</tr>");
}
