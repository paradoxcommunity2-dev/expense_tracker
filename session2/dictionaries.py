Dict = {
    "name": "kevin",
    "age": 18
}

# Update name
Dict["name"] = "tom"

# Add email
Dict["email"] = "eg@mail.com"


# Remove Key
del Dict['email']


# Print all key-value pairs
for key, value in Dict.items():
    print(f"{key} : {value}")