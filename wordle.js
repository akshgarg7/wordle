function checkGuess(target, guess) {
  let result = "";
  let m = {};

  // Populate the map with the count of each character in the target
  for (let char of target) {
    if (m[char]) {
      m[char]++;
    } else {
      m[char] = 1;
    }
  }

  for (let i = 0; i < guess.length; i++) {
    let g = guess[i];
    if (m[g] > 0 && target.includes(g)) {
      if (g === target[i]) {
        result += "G";
        m[g]--;
      } else {
        result += "Y";
        m[g]--;
      }
    } else {
      result += "W";
    }
  }

  return result;
}

// The playWordle function will be adapted to work in a web environment.
// Instead of using console input and output, it will interact with HTML elements.
function playWordle() {
  const wordBank = ["HEART", "CHART", "SMART", "START", "PARTY", "CHIEF", "BRIEF", "CRAFT", "GRACE", "BLAST"];
  const target = wordBank[Math.floor(Math.random() * wordBank.length)];
  const maxAttempts = 6;
  let attempts = 0;

  // Display welcome message and instructions
  document.getElementById('game-status').textContent = `Welcome to Wordle! You have ${maxAttempts} attempts to guess the correct 5-letter word.`;

  // Event listener for the guess submission
  document.getElementById('guess-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const guessInput = document.getElementById('guess-input');
    const guess = guessInput.value.toUpperCase();
    let result = '';

    if (guess.length !== 5) {
      document.getElementById('game-status').textContent = "Invalid input. Please enter a 5-letter word.";
      return;
    }

    result = checkGuess(target, guess);
    document.getElementById('guess-output').textContent = `${guess}\n${result}`;

    if (result === "GGGGG") {
      document.getElementById('game-status').textContent = "Congrats! You guessed the word correctly!";
      guessInput.disabled = true; // Disable further input after a correct guess
    } else {
      attempts++;
      if (attempts >= maxAttempts) {
        document.getElementById('game-status').textContent = `Sorry, you've run out of attempts. The correct word was ${target}.`;
        guessInput.disabled = true; // Disable further input after max attempts
      }
    }
  });
}

// Call playWordle when the window loads
window.onload = playWordle;
