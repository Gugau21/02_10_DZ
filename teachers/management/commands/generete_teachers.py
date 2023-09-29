import faker

from django.core.management.base import BaseCommand
from teachers.models import Teacher

fake = faker.Faker()

class Command(BaseCommand):
    help = "Add the specified number of teachers to the database"

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, default=100)

    def handle(self, *args, **options):
        number = options["number"]
        if number < 1:
            self.stdout.write(
                self.style.ERROR("Number is less then 1")
            )
        for i in range (options["number"]):
            t = Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                birth_date=fake.date()
            )
            self.stdout.write(
                self.style.SUCCESS('Successfully added teacher "%s"' % t.id)
            )