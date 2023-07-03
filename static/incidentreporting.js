

var map;
function initMap() {
    var mapOptions = {
        center: { lat: 25.2623, lng: 82.9893 },
        zoom: 16,
        scrollwheel: true // Enable zooming on mouse scrolling
    };
    map = new google.maps.Map(document.getElementById('map'), mapOptions);

    // Add event listener to capture the selected location's coordinates
    map.addListener('click', function(event) {
      var latitudeInput = document.getElementById('latitude-input');
      var longitudeInput = document.getElementById('longitude-input');
      latitudeInput.value = event.latLng.lat();
      longitudeInput.value = event.latLng.lng();
    });
  }
  