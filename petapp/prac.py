import json
# json_string = "[{\"model\": \"petapp.cart\", \"pk\": 87, \"fields\": {\"user_id\": 3, \"pet_id\": 3, \"name\": \"Bulldog\", \"line\": \"The Bulldog is a British breed of dog of mastiff type\", \"img1\": \"https://cdn.britannica.com/07/234207-050-0037B589/English-bulldog-dog.jpg\", \"date\": \"2024-01-14\"}}, {\"model\": \"petapp.cart\", \"pk\": 92, \"fields\": {\"user_id\": 7, \"pet_id\": 36, \"name\": \"Sheep\", \"line\": \"Sheep or domestic sheep are a domesticated, ruminant mammal typically kept as livestock.\", \"img1\": \"https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQiY6a7mjKS9Dz_zLCviJ4d2yUKU1IK7j7R-MNze-N5FHDVYxAsEji4gPSoHZ15gavM\", \"date\": \"2024-01-14\"}}, {\"model\": \"petapp.cart\", \"pk\": 93, \"fields\": {\"user_id\": 7, \"pet_id\": 8, \"name\": \"The Leghorn\", \"line\": \"The breed was introduced to Britain from the United States in 1870\", \"img1\": \"https://cs-tf.com/wp-content/uploads/2020/02/rooster.jpg\", \"date\": \"2024-01-15\"}}, {\"model\": \"petapp.cart\", \"pk\": 94, \"fields\": {\"user_id\": 7, \"pet_id\": 7, \"name\": \"Peacock\", \"line\": \"A Beautiful species in the world\", \"img1\": \"https://thedarjeelingchronicle.com/wp-content/uploads/2020/02/Peacock-777x437.jpg\", \"date\": \"2024-01-17\"}}, {\"model\": \"petapp.cart\", \"pk\": 95, \"fields\": {\"user_id\": 7, \"pet_id\": 34, \"name\": \"Leopard gecko\", \"line\": \"The leopard gecko or common leopard gecko is a ground-dwelling lizard\", \"img1\": \"https://t3.gstatic.com/licensed-image?q=tbn:ANd9GcTNq4EINrEUVndfv-ssjSZ1Bwk6sJHY6GOaj7FnHXDJmF6fYpZBqibmAEz6jj6aelNJ\", \"date\": \"2024-01-17\"}}, {\"model\": \"petapp.cart\", \"pk\": 97, \"fields\": {\"user_id\": 3, \"pet_id\": 9, \"name\": \"Gir\", \"line\": \"the Gir forest region of Gujarat\", \"img1\": \"https://hetha.in/cdn/shop/products/ScreenShot2021-07-16at10.57.58AM_737x.png?v=1631170331\", \"date\": \"2024-02-20\"}}, {\"model\": \"petapp.cart\", \"pk\": 98, \"fields\": {\"user_id\": 3, \"pet_id\": 6, \"name\": \"King cobra\", \"line\": \"it is not taxonomically a true cobra\", \"img1\": \"https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/12_-_The_Mystical_King_Cobra_and_Coffee_Forests.jpg/800px-12_-_The_Mystical_King_Cobra_and_Coffee_Forests.jpg\", \"date\": \"2024-02-21\"}}]"
# json_string="static/json/jdata.json"
with open("static/json/jdata.json") as file:
    json_string=json.load(file)
# Parse the JSON string into Python data structures (lists and dictionaries)
data = json.loads(json_string)


# Convert the data to a clean JSON string
clean_json_string = json.dumps(data, indent=4)

# Write the clean JSON string to a file
with open('clean_data.json', 'w') as json_file:
    json_file.write(clean_json_string)