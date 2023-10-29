from collections.abc import Iterator

from faker import Faker

from apps.contacts.models import Contact

faker = Faker()


def generate_contact() -> Contact:
    return Contact(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        phone_number=faker.phone_number(),
    )


def generate_contacts(amount: int) -> Iterator[Contact]:
    for _ in range(amount):
        yield generate_contact()
