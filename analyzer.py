file = open("C:\\Users\\bjaya\\Desktop\\Python\\readme.txt", "r")

categories = {
    "noun": ["lorem", "ipsum", "dummy"],
    "preposition": ["but", "with", "only"]
}

output = {}
densities = {}
result = {}

data = file.read()
total = len(data.split())

for category in categories:
    list = categories[category]
    
    for word in list:
        count = data.lower().count(word.lower())
        output.setdefault(category, {})[word] = count
        densities.setdefault(category, {})[word] = (count * 100) / total

for category in densities:
    group = densities[category]
    count = 0

    for density in group.values():
        count += density

    result[category] = count / len(group)

# print(output)
# print(densities)
print(result)

