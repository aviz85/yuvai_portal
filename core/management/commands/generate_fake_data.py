from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import AITool, Creation, Comment
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Generates fake data for the application'

    def handle(self, *args, **kwargs):
        self.stdout.write('Generating fake data...')

        # Create users
        users = []
        for _ in range(10):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'
            )
            users.append(user)

        # Create AI tools
        ai_tools = []
        for _ in range(5):
            tool = AITool.objects.create(
                name=fake.company(),
                description=fake.text(),
                website=fake.url()
            )
            ai_tools.append(tool)

        # Create creations
        creation_types = ['APP', 'IMG', 'VID', 'AUD', 'OTH']
        for _ in range(20):
            creation = Creation.objects.create(
                title=fake.catch_phrase(),
                description=fake.paragraph(),
                creation_type=random.choice(creation_types),
                content=fake.file_name(),
                creator=random.choice(users)
            )
            creation.tools_used.set(random.sample(ai_tools, random.randint(1, 3)))

            # Add comments to each creation
            for _ in range(random.randint(0, 5)):
                Comment.objects.create(
                    creation=creation,
                    author=random.choice(users),
                    content=fake.paragraph()
                )

        self.stdout.write(self.style.SUCCESS('Fake data generated successfully!'))