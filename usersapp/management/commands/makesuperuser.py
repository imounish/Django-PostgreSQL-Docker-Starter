import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

User = get_user_model()


# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         username = "admin"
#         email = "admin@admin.com"
#         try:
#             u = None
#             if (
#                 not User.objects.filter(username=username).exists()
#                 and not User.objects.filter(is_superuser=True).exists()
#             ):
#                 print("admin user not found, creating one")

#                 new_password = get_random_string(10)

#                 u = User.objects.create_superuser(username, email, new_password)
#                 print(f"===================================")
#                 print(
#                     f"A superuser '{username}' was created with email '{email}' and password '{new_password}'"
#                 )
#                 print(f"===================================")
#             else:
#                 print("admin user found. Skipping super user creation")
#                 print(u)
#         except Exception as e:
#             print(f"There was an error: {e}")


class Command(BaseCommand):
    def handle(self, *args, **options):
        username = os.environ.get("SUPERUSER_NAME", "admin")
        email = os.environ.get("SUPERUSER_EMAIL", "admin@example.com")

        try:
            u = None
            if (
                not User.objects.filter(username=username).exists()
                and not User.objects.filter(is_superuser=True).exists()
            ):
                print("admin user not found, creating one")

                new_password = get_random_string(10)
                password = os.environ.get("SUPERUSER_PASS", new_password)

                u = User.objects.create_superuser(username, email, password)

                print(f"===================================")
                print(
                    f"A superuser '{username}' was created with email '{email}' and password '{password}'"
                )
                print(f"===================================")
            else:
                print("admin user found. Skipping super user creation")
                print(u)
        except Exception as e:
            print(f"There was an error: {e}")
