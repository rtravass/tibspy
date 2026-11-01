import csv
import json

input_file = "reviews.csv"
output_file = "review_analysis.json"

positive_words = {
    "excellent","amazing","good","great","liked","love"
}

negative_words = {
    "bad","poor","slow","disappointing","worst"
}

results = []

try:
    with open(input_file,"r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            customer = row["Customer"]
            review = row["Review"]
            words = review.lower().replace(",","").split()
            
            positive_matches = set(words).intersection(positive_words)
            negative_matches = set(words).intersection(negative_words)

            if len(positive_matches) > len(negative_matches):
                sentiment = "Positive"
            elif len(negative_matches) > len(positive_matches):
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            result = {
                "customer":customer,
                "review":review,
                "sentiment":sentiment
            }

            results.append(result)

except FileNotFoundError:
    print("reviews.csv file was not found")
    exit()

# Display results
print("\n=========== AI Product review analysis ============= ")

for result in results:
    print(
       f"{result['customer']} => "
       f"{result['sentiment']}"
    )

# Save result
with open(output_file,"w") as file:
    json.dump(results, file, indent=4)

print("\nAnalysis completed.")
print(f"Results saved to : {output_file}")