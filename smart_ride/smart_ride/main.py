
from utils.ride import calculate_fare, get_traffic_multiplier

print("\n==========================================")
print("      SMART RIDE ADVISOR        ")
print("\n==========================================")

distance = float(input("Enter the distance in kms: "))
traffic = input("Enter traffic (low/medium/high): ").lower()
ride_type = input("Enter ride type (economy/comfort/premium)").lower()

if ride_type == "economy":
    base_fare = 50
    per_km = 12
elif ride_type == "comfort":
    base_fare = 80
    per_km = 18
elif ride_type == "premium":
    base_fare = 120
    per_km = 25
else:
    print("Invalid ride type")
    exit()    

basic_fare = calculate_fare(distance, base_fare,per_km)
multiplier = get_traffic_multiplier(traffic)
final_fare = basic_fare * multiplier

if traffic == "high" and distance > 10:
    recommendation = "Heavy traffic expected. Consider starting early."
elif traffic == "medium":
    recommendation = "Moderate traffic expected."
else:
    recommendation = "Traffic looks good"
print("\n==================================")
print("          TRIP SUMMARY              ")
print("\n==================================")
print("Distance:\t",distance,"km")
print("Traffic:\t",traffic)
print("Ride Type:\t",ride_type)
print("Basic Fare: Rs", round(basic_fare,2))
print("Traffic Factor: ", multiplier)
print("Estimated Fare: Rs", round(final_fare,2))
print("\nRecommendation:")
print(recommendation)
print("\n==================================")
