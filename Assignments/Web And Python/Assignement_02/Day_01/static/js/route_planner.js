function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 16.728, lng: 79.958},
        zoom: 7
    });

    var directionsService = new google.maps.DirectionsService();
    var directionsRenderer = new google.maps.DirectionsRenderer();
    directionsRenderer.setMap(map);

    document.getElementById('routeForm').addEventListener('submit', function(event) {
        event.preventDefault();
        calculateAndDisplayRoute(directionsService, directionsRenderer);
    });

    // Automatically calculate the route when the page loads
    calculateAndDisplayRoute(directionsService, directionsRenderer);
}

function calculateAndDisplayRoute(directionsService, directionsRenderer) {
    var start = document.getElementById('start').value;
    var end = document.getElementById('end').value;

    directionsService.route({
        origin: start,
        destination: end,
        travelMode: 'DRIVING'
    }, function(response, status) {
        if (status === 'OK') {
            directionsRenderer.setDirections(response);
        } else {
            window.alert('Directions request failed due to ' + status);
        }
    });
}


