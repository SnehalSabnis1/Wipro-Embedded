class TrafficData:
    @staticmethod
    def get_traffic_info(user_location, destination):
        # Pseudo code to fetch real-time traffic data
        # This could be an API call to a traffic data provider
        traffic_info = f"Traffic information from {user_location} to {destination}"
        return traffic_info

    @staticmethod
    def get_alternative_routes(user_location, destination):
        # Pseudo code to fetch alternative routes
        alternative_routes = [
            f"Route 1 from {user_location} to {destination}",
            f"Route 2 from {user_location} to {destination}"
        ]
        return alternative_routes

class UserPreference:
    def __init__(self, user_location, destination):
        self.user_location = user_location
        self.destination = destination

    def save(self):
        # Pseudo code to save user preferences
        pass
