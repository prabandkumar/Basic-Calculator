function calculate() {
  const a = Number(document.getElementById("a").value);
  const b = Number(document.getElementById("b").value);
  const operator = document.getElementById("operator").value;
  let result = "";

  if (operator === "+") {
    result = a + b;
  } else if (operator === "-") {
    result = a - b;
  } else if (operator === "*") {
    result = a * b;
  } else if (operator === "/") {
    if (b === 0) {
      result = "Division by zero is not allowed";
    } else {
      result = a / b;
    }
  } else if (operator === "%") {
    result = a % b;
  } else {
    result = "Invalid operator";
  }

  document.getElementById("result").innerText = "Result: " + result;
}
