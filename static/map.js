function initMap() {
  var mapOptions = {
      center: { lat: 25.2623, lng: 82.9893 },
      zoom: 16,
      scrollwheel: true // Enable zooming on mouse scrolling
  };
  map = new google.maps.Map(document.getElementById('map'), mapOptions);

  var myDiv = document.getElementById('myDiv');
  var incidentsData = JSON.parse(myDiv.getAttribute('data-mydata'));
  console.log(incidentsData);
}
