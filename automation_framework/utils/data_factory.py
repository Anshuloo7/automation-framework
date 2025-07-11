from faker import Faker

faker = Faker()

def generate_user():
    return {
        "name": faker.first_name(),
        "email": faker.email(),
        "phone": faker.phone_number(),
        "id": faker.uuid4()
    }