
function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 37.7749, lng: -122.4194}, // Example coordinates (San Francisco)
        zoom: 12
    });

    // Example transit data
    var transitData = [
        {id: 1, position: {lat: 37.7749, lng: -122.4194}, status: 'On time'},
        {id: 2, position: {lat: 37.7849, lng: -122.4294}, status: 'Delayed'},
        // Add more transit data as needed
    ];

    // Add markers to the map
    transitData.forEach(function(transit) {
        var marker = new google.maps.Marker({
            position: transit.position,
            map: map,
            title: `Transit ID: ${transit.id}, Status: ${transit.status}`
        });

        marker.addListener('click', function() {
            showTransitDetails(transit);
        });
    });
}

function showTransitDetails(transit) {
    var modalBody = document.querySelector('#transitModal .modal-body');
    modalBody.innerHTML = `<p>Transit ID: ${transit.id}</p>
                           <p>Status: ${transit.status}</p>
                           <p>Position: (${transit.position.lat}, ${transit.position.lng})</p>`;
    $('#transitModal').modal('show');
}


