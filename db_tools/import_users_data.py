from users.models import UserProfile
from db_tools.data.users_data import row_data
for user in row_data:
    UserProfile.objects.create_superuser(username=user['username'],email=user['email'],password=user['password'])