
def calculate_fare(distance, base_fare, per_km):
    fare = base_fare + (distance * per_km)
    return fare

def get_traffic_multiplier(traffic):
    if traffic == "low":
        return 1.0
    elif traffic == "medium":
        return 1.2
    else:
        return 1.5