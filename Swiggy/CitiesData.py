import json
import re

# Load the JSON data from your file
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# unique cities
all_cities_and_subregions = set()
unique_cities = set()

# Delhi
delhi_subregion_restaurant_counts = {}

# city costs
city_costs = {}

# Regular expression pattern to extract numeric part of cost value
cost_pattern = re.compile(r'\d+')

# Iterate to extract cities and subregions
for city_name, city_data in data.items():
    all_cities_and_subregions.add(city_name)

    if 'restaurants' in city_data:
        unique_cities.add(city_name)

        if city_name == 'Delhi' and 'subregion' in city_data:
            subregion = city_data['subregion']
            if subregion in delhi_subregion_restaurant_counts:
                delhi_subregion_restaurant_counts[subregion] += len(
                    city_data['restaurants'])
            else:
                delhi_subregion_restaurant_counts[subregion] = len(
                    city_data['restaurants'])

        for restaurant_id, restaurant_info in city_data['restaurants'].items():
            cost = restaurant_info.get('cost')
            if cost:
                # Extract numeric part of cost value and convert to float
                cost_match = cost_pattern.search(cost)
                if cost_match:
                    cost_numeric = float(cost_match.group())
                    city_costs.setdefault(city_name, []).append(cost_numeric)

# Count the total number of cities and subregions
total_cities_and_subregions = len(all_cities_and_subregions)

# Count the number of unique cities
num_unique_cities = len(unique_cities)

#

# else:
#     print("No data available for subregions of Delhi.")

# Calculate and display the top 5 most expensive cities
top_expensive_cities = sorted(city_costs.keys(), key=lambda city: sum(
    city_costs[city])/len(city_costs[city]), reverse=True)[:5]
print("Top 5 Most Expensive Cities:")
for i, city in enumerate(top_expensive_cities, start=1):
    average_cost = sum(city_costs[city]) / len(city_costs[city])
    print(f"{i}. {city} (Average Cost: ₹{average_cost:.2f})")

print('\n')

print(
    f"Total number of cities and subregions where Swiggy is listed: {total_cities_and_subregions}")

print(
    f"Number of cities (excluding subregions) where Swiggy is listed: {num_unique_cities}")
