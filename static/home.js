document.getElementById('search-form').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent default form submission
    
    // Get the search query
    var query = document.getElementById('search-input').value;
    
    // Redirect to the search result page with the query as a parameter
    window.location.href = "{% url 'search_result' %}?q=" + encodeURIComponent(query);
  });