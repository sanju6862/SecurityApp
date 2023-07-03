function initMapForIncident(latitude, longitude) {
    var mapContainer = document.querySelector('.map');
    var mapOptions = {
      center: { lat: latitude, lng: longitude },
      zoom: 12,
    };
    var map = new google.maps.Map(mapContainer, mapOptions);
    var marker = new google.maps.Marker({
      position: { lat: latitude, lng: longitude },
      map: map,
    });
  }
  
function zoomIn(button) {
    var mediaContainer = button.parentNode.parentNode;
    var mediaElement = mediaContainer.querySelector('img');
    var currentZoomLevel = getCurrentZoomLevel(mediaElement);

    if (currentZoomLevel < 3) {
        var newZoomLevel = currentZoomLevel + 0.5;
        applyZoom(mediaElement, newZoomLevel);
        enableImageDragging(mediaContainer);
    }
}

function zoomOut(button) {
    var mediaContainer = button.parentNode.parentNode;
    var mediaElement = mediaContainer.querySelector('img');
    var currentZoomLevel = getCurrentZoomLevel(mediaElement);

    if (currentZoomLevel > 1) {
        var newZoomLevel = currentZoomLevel - 0.5;
        applyZoom(mediaElement, newZoomLevel);
        enableImageDragging(mediaContainer);
    }
}

function getCurrentZoomLevel(mediaElement) {
    var currentZoom = mediaElement.dataset.zoom || 1;
    return parseFloat(currentZoom);
}

function applyZoom(mediaElement, zoomLevel) {
    mediaElement.style.transform = 'scale(' + zoomLevel + ')';
    mediaElement.dataset.zoom = zoomLevel;
}

function enableImageDragging(mediaContainer) {
    var mediaElement = mediaContainer.querySelector('img, video');
    var isDragging = false;
    var startX;
    var startY;
    var offsetX = 0;
    var offsetY = 0;

    mediaContainer.addEventListener('mousedown', startDragging);
    mediaContainer.addEventListener('mousemove', dragImage);
    mediaContainer.addEventListener('mouseup', stopDragging);
    mediaContainer.addEventListener('mouseleave', stopDragging);

    function startDragging(event) {
        isDragging = true;
        startX = event.clientX;
        startY = event.clientY;
    }

    function dragImage(event) {
        if (!isDragging) return;

        event.preventDefault();

        var deltaX = event.clientX - startX;
        var deltaY = event.clientY - startY;
        startX = event.clientX;
        startY = event.clientY;

        offsetX += deltaX;
        offsetY += deltaY;

        mediaElement.style.transform = 'scale(' + getCurrentZoomLevel(mediaElement) + ') translate(' + offsetX + 'px, ' + offsetY + 'px)';
    }

    function stopDragging() {
        isDragging = false;
    }
}