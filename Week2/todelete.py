products = [
    ("laptop",80000),
    ("phone",20000),
    ("tab",30000)
]

for product, price in products:
    if price > 50000:
        print(f"{product}: Premium")
    else:
        print(f"{product}: Standard")

#=============================

for attempt in range(3):
    print(f"Processing {attempt}")

#============changing global variable=================

count = 0

def increment():
    global count
    count += 1

increment()
print(count)


#==================lambda===========

double = lambda x: x*2
print(double(10))

addtwo = lambda x : x + 2
print(addtwo(3))


#==================lambda sort ===========

products = [
    ("laptop",80000),
    ("phone",20000),
    ("tab",30000)
]

sorted_products = sorted(products,key = lambda item : item [1])
print(sorted_products)


#==================lambda filter ===========

score = [10, 30, 20, 5]
high_score = list(filter(lambda score : score > 20, score))
print(high_score)

#==================lambda map ===========

prices = [100, 200, 300]
new_price = list(map(lambda x: x * 1.1, prices))
print(new_price)
