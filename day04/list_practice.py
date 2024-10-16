fruits = ["Apple", "Banana", "Mango", "Cherry", "Pear"]
states_of_india = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
    "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
    "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand",
    "West Bengal"
]
print(len(states_of_india))
print(len(fruits))
fruits[0] = "AP"
print(fruits)
fruits.append("Coconut")
print(fruits)
fruits.extend(["Black Berry", "Watermelon"])
print(fruits)
