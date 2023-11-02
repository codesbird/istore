from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User

@receiver(user_logged_in)
def change_password(sender, request, user, **kwargs):
    new_password = User.objects.make_random_password()
    user.set_password(new_password)
    user.save()
    print(f"Sysytem detected that's A new user ({user}) login in the system")
    send_mail(
        'Password Changed',
        f'Your new password is {new_password}. Please keep it safe.',
        'hak997327@gmail.com',
        [user.email],
        fail_silently=False,
    )
