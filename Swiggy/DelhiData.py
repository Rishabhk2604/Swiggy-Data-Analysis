import json

# Load
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# least expensive restaurant and maximum restaurant count
min_cost = float('inf')  # Set to positive infinity initially
least_expensive_subregion = None

max_restaurant_count = 0
max_subregion = None

# Iterate through tHe SubRegions
if 'Delhi' in data:
    delhi_data = data['Delhi']
    for subregion, subregion_data in delhi_data.items():
        if 'restaurants' in subregion_data:
            # least expensive restaurant
            for restaurant_info in subregion_data['restaurants'].values():
                cost = restaurant_info.get('cost')
                if cost and cost != 'NA':
                    try:
                        # Extract numeric part of cost value
                        cost_numeric = float(cost.split('₹')[-1])
                        if cost_numeric < min_cost:
                            min_cost = cost_numeric
                            least_expensive_subregion = subregion
                    except ValueError:
                        pass  # Ignore invalid cost values

            # Find maxim restaurant count
            restaurant_count = len(subregion_data['restaurants'])
            if restaurant_count > max_restaurant_count:
                max_restaurant_count = restaurant_count
                max_subregion = subregion

# Display Subregion with least expensive restaurant
if least_expensive_subregion:
    print(
        f"SubRegion in Delhi with the least expensive restaurant: {least_expensive_subregion} (Cost: ₹{min_cost:.2f})")
else:
    print("No restaurant data available for Delhi.")

# Display Subregion with maximum number of restaurants
if max_subregion:
    print(
        f"SubRegion of Delhi with the maximum number of restaurants: {max_subregion} ({max_restaurant_count} restaurants)")
else:
    print("No restaurant data available for Delhi.")
