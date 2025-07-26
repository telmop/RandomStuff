let currentOperation = " ";
let firstOperand = null;
let toClearScreen = true;


function computeOperation(operation, number1, number2) {
    switch (operation) {
        case " ":
        case "=":
            return number2.toString();
        case "+":
            return (number1 + number2).toString();
        case "-":
            return (number1 - number2).toString();
        case "x":
            return (number1 * number2).toString();
        case "/":
            if (number2 === 0) {
                return "NaN";
            }
            return (number1 / number2).toString();
    }
}

function clickOperation(operation) {
    toClearScreen = true;
    let numberDiv = document.querySelector(".number-visor");
    if (firstOperand === null) {
        firstOperand = parseInt(numberDiv.textContent);
        numberDiv.textContent = "0";
    } else {  // Already a first operand. Do op.
        let secondOperand = parseInt(numberDiv.textContent);
        let result = computeOperation(currentOperation, firstOperand, secondOperand);
        if (operation === "=") {
            firstOperand = null;
        } else {
            firstOperand = parseInt(result);
        }
        numberDiv.textContent = result;
    }
    currentOperation = operation;
    let opDiv = document.querySelector(".current-operation");
    opDiv.textContent = currentOperation;
}

function clickNumber(number) {
    let numberDiv = document.querySelector(".number-visor");
    let prev_number = numberDiv.textContent.trim();
    numberDiv.textContent = (prev_number === "0" || toClearScreen) ? number : prev_number + number;
    toClearScreen = false;
}

function reset() {
    currentOperation = " ";
    document.querySelector(".current-operation").textContent = " ";
    firstOperand = null;
    document.querySelector(".number-visor").textContent = "0";
}

let opButtons = document.querySelectorAll(".operation");
opButtons.forEach((button) => button.addEventListener("click", () => clickOperation(button.textContent)));

let numButtons = document.querySelectorAll(".number");
numButtons.forEach((button) => button.addEventListener("click", () => clickNumber(button.textContent)));
