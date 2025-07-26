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

function playRound(humanChoice, computerChoice) {
    if (humanChoice === computerChoice) {
        console.log("It's a tie! Both picked ", humanChoice);
        return;
    }
    if (humanChoice === "rock") {
        if (computerChoice === "paper") {
            console.log("You lose! Paper beats Rock.");
            computerScore++;
        } else {
            console.log("You win! Rock beats Scissors.");
            humanScore++;
        }
    } else if (humanChoice === "paper") {
        if (computerChoice === "rock") {
            console.log("You win! Paper beats Rock.");
            humanScore++;
        } else {
            console.log("You lose! Scissors beats Paper.");
            computerScore++;
        }
    } else {  // humanChoice === "scissors"
        if (computerChoice === "rock") {
            console.log("You lose! Rock beats Scissors.");
            computerScore++;
        } else {
            console.log("You win! Scissors beats Paper.");
            humanScore++;
        }
    }
}

function playGame() {
    humanScore = 0;
    computerScore = 0;
    for (let i = 0; i < 5; i++) {
        let humanChoice = getHumanChoice();
        let computerChoice = getComputerChoice();
        playRound(humanChoice, computerChoice);
    }
    console.log(`Human: ${humanScore}; Computer: ${computerScore}`);
    if (humanScore > computerScore) {
        console.log("The human won. Enjoy your short term win...");
    } else if (humanScore < computerScore) {
        console.log("I won. Behold your new god, puny human!");
    } else {  // Tie.
        console.log("We tied... Soon enough, human.");
    }
}

playGame();

