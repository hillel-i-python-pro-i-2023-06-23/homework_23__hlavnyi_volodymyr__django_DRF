import logging

from django.core.management.base import BaseCommand

from apps.contacts import models
from apps.contacts.services.generate_contacts import generate_contacts


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        logger = logging.getLogger("django")

        # Contacts
        # Contacts (10 pcs)
        logger.info("---------Start filling the database with the 3rd step")
        init_first_contacts(amount=10)
        logger.info("---------Finish filling the database with the 3rd step")


# Contacts (20 pcs)
def init_first_contacts(amount: int = 10) -> None:
    logger = logging.getLogger("django")

    queryset = models.Contact.objects.all()

    logger.info(f"Current amount of Contacts before: {queryset.count()}")

    if queryset.count() == 0:
        for contact in generate_contacts(amount=amount):
            contact.save()
        logger.info(f"Create new Contacts (amount is {amount})")
    else:
        logger.info(f"Contacts already exists (current amount is {queryset.count()}). Skip creating new Contacts!")
