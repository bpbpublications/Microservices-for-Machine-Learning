
# Install faker: pip install faker
from faker import Faker

fake = Faker()

def mask_user_data(user_data):
    user_data['name'] = fake.name()
    user_data['address'] = fake.address()
    user_data['email'] = fake.email()
    return user_data

# INPUT
user = {
    "name": "Alice",
    "address": "1234 Real St, Imaginary City, IL 12345",
    "email": "alice@email.com"
}

# PROCESS
masked_user = mask_user_data(user)

# OUTPUT
print(masked_user)
