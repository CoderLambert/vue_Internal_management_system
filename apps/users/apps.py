from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = "用户管理"
    def ready(self):
        import users.signals
    # 加了密码就会错，无法登陆,如果是后端直接创建的话

    # 通过 create user 方法 需要自己加密一下

