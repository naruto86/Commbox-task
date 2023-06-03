from faker import Faker


def generate_mock_data(num_identities):
    fake = Faker()
    data = []
    for _ in range(num_identities):
        email = fake.email()
        firstname = fake.first_name()
        lastname = fake.last_name()
        city = fake.city()
        country = fake.country()
        personal_id = fake.random_number(digits=9)
        data.append(f"{email}, {firstname}, {lastname}, {city}, {country}, {personal_id}")
    return data


num_identities = int(input("Enter the number of identities to create: "))
mock_data = generate_mock_data(num_identities)
for data in mock_data:
    print(data)
