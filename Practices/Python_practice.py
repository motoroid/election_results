print("Hello World")
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1]== 'Denver':
    print (counties[1])
if counties[1] !="Jefferson":
    print(counties[2])

temperature = int(input("what is the temp outside?"))
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the window")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Araphoe or El Paso is in the list")
else:
    print("Araphoe or El Paso is not in the list")

for county in counties:
    print(county)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

for county in counties_dict.keys():
    print(county)
    