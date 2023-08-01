// Initialize the map
function initMap() {
  var mapOptions = {
    center: { lat: 25.2623, lng: 82.9893 },
    zoom: 16,
    scrollwheel: true // Enable zooming on mouse scrolling
  };
  map = new google.maps.Map(document.getElementById('map'), mapOptions);

  // Loop through the incidents data and draw circles
  var incidents = JSON.parse('{{ incidents|safe }}');

  for (var i = 0; i < incidents.length; i++) {
    var incident = incidents[i];
    var incidentLocation = new google.maps.LatLng(incident.latitude, incident.longitude);
    var incidentCircle = new google.maps.Circle({
      strokeColor: "#FF0000",
      strokeOpacity: 0.2,
      strokeWeight: 2,
      fillColor: "#FF0000",
      fillOpacity: 0.35,
      map: map,
      center: incidentLocation,
      radius: 50,
      circleOptions: {
        numberOfPoints: 40 // Adjust the number of points for smoother boundaries
      }
    });
  }
}
