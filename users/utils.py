from users.models import User


def generate_random_password():
    return User.objects.make_random_password()
