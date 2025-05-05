py manage.py shell
from django.contrib.auth.models import User
users=User.objects.all()
users
exit()
