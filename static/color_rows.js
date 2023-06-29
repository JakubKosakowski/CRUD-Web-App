var rows = document.querySelectorAll('tr');

// Iteruj przez wiersze i nadaj im odpowiednią klasę CSS
for (var i = 0; i < rows.length; i++) {
  if (i % 2 === 0) {
    rows[i].classList.add('even');
  } else {
    rows[i].classList.add('odd');
  }
}