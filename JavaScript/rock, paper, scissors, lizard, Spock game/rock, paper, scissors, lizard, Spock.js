function play(userChoice) {
    const choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock'];
    const computerChoice = choices[Math.floor(Math.random() * choices.length)];
    const resultText = document.getElementById('result-text');

    const result = getResult(userChoice, computerChoice);
    resultText.textContent = `You chose ${userChoice} \n computer chose ${computerChoice}. ${result}`;
}

function getResult(userChoice, computerChoice) {
    if (userChoice === computerChoice) {
        return 'It\'s a tie!';
    }

    if ((userChoice === 'Rock' && (computerChoice === 'Scissors' || computerChoice === 'Lizard')) ||
        (userChoice === 'Paper' && (computerChoice === 'Rock' || computerChoice === 'Spock')) ||
        (userChoice === 'Scissors' && (computerChoice === 'Paper' || computerChoice === 'Lizard')) ||
        (userChoice === 'Lizard' && (computerChoice === 'Spock' || computerChoice === 'Paper')) ||
        (userChoice === 'Spock' && (computerChoice === 'Scissors' || computerChoice === 'Rock'))) {
        return 'You win!';
    } else {
        return 'You lose!';
    }
}
