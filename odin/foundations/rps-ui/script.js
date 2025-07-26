function getComputerChoice() {
    let rnd = Math.random() * 3;
    if (rnd <= 1) {
        return "rock";
    } else if (rnd <= 2) {
        return "paper";
    } else {
        return "scissors";
    }
}

function getHumanChoice() {
    while (true) {
        let choice = prompt("Chose rock/paper/scissors: ");
        choice = choice.trim().toLowerCase();
        if (choice === "rock" || choice === "paper" || choice === "scissors") {
            return choice;
        }
    }
}

let humanScore = 0;
let computerScore = 0;

function playRound(humanChoice) {
    computerChoice = getComputerChoice();
    const messageElement = document.querySelector("#message");

    if (humanChoice === computerChoice) {
        messageElement.textContent = "It's a tie! Both picked " + humanChoice;
        return;
    }
    if (humanChoice === "rock") {
        if (computerChoice === "paper") {
            messageElement.textContent = "You lose! Paper beats Rock.";
            computerScore++;
        } else {
            messageElement.textContent = "You win! Rock beats Scissors.";
            humanScore++;
        }
    } else if (humanChoice === "paper") {
        if (computerChoice === "rock") {
            messageElement.textContent = "You win! Paper beats Rock.";
            humanScore++;
        } else {
            messageElement.textContent = "You lose! Scissors beats Paper.";
            computerScore++;
        }
    } else {  // humanChoice === "scissors"
        if (computerChoice === "rock") {
            messageElement.textContent = "You lose! Rock beats Scissors.";
            computerScore++;
        } else {
            messageElement.textContent = "You win! Scissors beats Paper.";
            humanScore++;
        }
    }
    updateScores();
}

function updateScores() {
    const humanScoreSpan = document.querySelector("#human-score");
    const computerScoreSpan = document.querySelector("#computer-score");
    humanScoreSpan.textContent = humanScore;
    computerScoreSpan.textContent = computerScore;
}

updateScores();
