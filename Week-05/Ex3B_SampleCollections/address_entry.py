# Create dictionary
contact_info = {
    "name": "Nahom Asheber",
    "address": "123 Snellville Rd",
    "city": "Gwinnett",
    "state": "GA",
    "zip": "28000"
}

# Print formatted address
print(f"""
{contact_info["name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}
""")

# Remove the name key:value pair
contact_info.pop("name")

# Create new dictionary for full name
full_name = {
    "first name": "Nahom",
    "last name": "Asheber"
}

# Add honorific using update()
full_name.update({"honorific": "Mr."})

# Add full_name to contact_info
contact_info.update({"full_name": full_name})

# Print updated formatted address
print(f"""
{contact_info["full_name"]["honorific"]} {contact_info["full_name"]["first name"]} {contact_info["full_name"]["last name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}
""")