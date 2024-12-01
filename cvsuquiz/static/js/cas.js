alert("JavaScript is working!");
const textfocus = document.querySelector('.text');

  textfocus.addEventListener('mousedown', () => {
    textfocus.classList.add('active'); // Add active class on click

    // Remove active class after 5 seconds (5000ms)
    setTimeout(() => {
      textfocus.classList.remove('active'); // Remove active class after timeout
    }, 4000);
  });