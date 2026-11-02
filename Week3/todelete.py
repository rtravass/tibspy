#==================== Tuple unpacking ===================================

transcation = ("tx101","c501",2500.00,"inr")
transcation_id, customer_id, amount, currency = transcation

print(transcation_id)
print(currency)

# op:
# tx101
# inr


#==================== csv operations ===================================

import csv

with open("customers.csv","r",newline="") as input_file:
    reader = csv.DictReader(input_file)

    with open("processed_customers.csv","w",newline="") as output_file:
        fieldnames = ["name","city","updated_spend"]
        writer = csv.DictWriter(output_file,fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            spend = float(row["spend"])
            updated_spend = spend * 1.10
            writer.writerow(
                {
                    "name": row["name"],
                    "city": row["city"],
                    "updated_spend": updated_spend
                }
            )


#==================== json operations ===================================

import json

json_text = '{"name": "Ryan","city": "Mumbai"}'

customer = json.loads(json_text)   # string to Python object
print(customer["name"])

#=========================  read json file ===============================================

import json

with open("customer.json","r") as file:
    customer = json.load(file)

print(customer["name"])
print(customer["city"])

#===========================

import json

customer = {
        "customer_id": 101,
        "name": "Ryan",
        "city": "Mumbai"
    }

with open("new_customer.json","w") as file:
    json.dump(customer, file)