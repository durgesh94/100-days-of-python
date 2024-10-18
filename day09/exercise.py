fruit_colors = {
    "Apple": "Red",
    "Mango": "Orange",
    "Banana": "Yellow"
}

print(fruit_colors['Apple'])

print(fruit_colors)

fruit_colors['Mango'] = "Orange-Yellow-Green"
print(fruit_colors)

# fruit_colors = {}
# print(fruit_colors)

# Loop through dictionary
for key in fruit_colors:
    print(key)
    print(fruit_colors[key])