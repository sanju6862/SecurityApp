var sendingLocation = false;
var watchID;
var intervalID;

function activateSendingLocation() {
    if (navigator.geolocation && !sendingLocation) {
        sendingLocation = true;
        document.getElementById("activateButton").disabled = true;
        document.getElementById("deactivateButton").disabled = false;

        getLocation();
        intervalID = setInterval(getLocation, 10000); // Retry every 10 seconds
    }
}

function getLocation() {
    navigator.geolocation.getCurrentPosition(sendLocationData, errorCallback, { enableHighAccuracy: true });
}

function sendLocationData(position) {
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;

    // Send the location data to the Django view as form data
    var formData = new FormData();
    formData.append('latitude', latitude);
    formData.append('longitude', longitude);

    fetch('/location_sender/', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function deactivateSendingLocation() {
    if (navigator.geolocation && sendingLocation) {
        sendingLocation = false;
        document.getElementById("activateButton").disabled = false;
        document.getElementById("deactivateButton").disabled = true;

        clearInterval(intervalID);
    }
}

function errorCallback(error) {
    console.error('Error:', error);

    // Retry getting the location after an error occurs
    getLocation();
}