from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Category, Post


class Command(BaseCommand):
    help = "Generates random test data for YourModel"

    def handle(self, *args, **options):
        fake = Faker()
        Faker.seed(0)  # For repeatable results

        def generate_unique_slug() -> str:
            # Generate a unique slug by appending a random number to the slug
            base_slug = fake.slug()
            slug = base_slug
            num = 2
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            return slug

        def generate_random_data():
            # Create a user
            username = fake.user_name()
            password = fake.password()  # Should not be used in production
            user = User.objects.create_user(
                username=username,
                password=password,
            )

            # Create a category
            category = Category.objects.create(name=fake.word())

            # Create a post
            post = Post(
                title=fake.sentence(),
                content=fake.text(),
                published_at=fake.date_time_this_decade(),
                slug=generate_unique_slug(),
                author=user,
                category=category,
            )
            post.save()

        # Generate 10 random posts
        for _ in range(10):
            generate_random_data()

        self.stdout.write(
            self.style.SUCCESS("Successfully generated random Post."),
        )
