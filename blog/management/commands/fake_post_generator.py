import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Category, Post


class Command(BaseCommand):
    help = "Generates random test data for YourModel"
    STATUS = ["published", "pending", "archive", "trash"]

    def handle(self, *args, **options):
        fake = Faker()
        # Create a user
        username = fake.user_name()
        password = fake.password()  # Should not be used in production
        user = User.objects.create_user(
            username=username,
            password=password,
        )

        def generate_unique_slug() -> str:
            # Generate a unique slug by appending a random number to the slug
            base_slug = fake.slug()
            slug = base_slug
            num = 2
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            return slug

        def generate_unique_category():
            while True:
                name = fake.word()
                category, created = Category.objects.get_or_create(name=name)
                if created:
                    return category

        def generate_random_data(user):
            # Create a post
            post = Post(
                title=fake.sentence(),
                content=fake.text(max_nb_chars=10000),
                published_at=fake.date_time_this_decade(),
                slug=generate_unique_slug(),
                author=user,
                category=generate_unique_category(),
                status=random.choice(self.STATUS),
            )
            post.save()

        # Generate 10 random posts
        for _ in range(100):
            generate_random_data(user)

        self.stdout.write(
            self.style.SUCCESS("Successfully generated random Post."),
        )
