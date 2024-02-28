import random

from django.core.management.base import BaseCommand
from faker import Faker

from shop.models import Product, ProductCategory


class Command(BaseCommand):
    help = "Generates random product"
    STATUS = ["published", "pending", "archive", "trash"]

    def handle(self, *args, **options):
        fake = Faker()

        def generate_unique_slug() -> str:
            # Generate a unique slug by appending a random number to the slug
            base_slug = fake.slug()
            slug = base_slug
            num = 2
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            return slug

        def genrate_category():
            cats = [
                "Infant toys",
                "Jigsaw puzzles",
                "Movement toys",
                "Musical toys",
                "Play Vehicles",
                "Building toys",
                "Children books",
                "Dolls",
                "Games",
            ]
            for cat in cats:
                ProductCategory.objects.create(name=cat)

        def get_random_category():
            category_objects = ProductCategory.objects.all()
            return random.choice(category_objects)

        def generate_random_data():
            # Create a Product
            post = Product(
                title=fake.word(),
                slug=generate_unique_slug(),
                description=fake.text(max_nb_chars=10000),
                category=get_random_category(),
                status=random.choice(self.STATUS),
            )
            post.save()

        genrate_category()
        # Generate 100 random posts
        for _ in range(100):
            generate_random_data()

        self.stdout.write(
            self.style.SUCCESS("Successfully generated random Product."),
        )
