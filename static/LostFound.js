// script.js
document.getElementById('search-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const query = document.getElementById('query-input').value;
    const url = '/item-search/?query=' + encodeURIComponent(query);
    fetch(url)
      .then(response => response.text())
      .then(data => {
        document.getElementById('search-results').innerHTML = data;
      });
  });
  
  