from django.conf import settings as django_settings


SU_ADMIN_NAME = "Django Admin"

SU_ADMIN_MENU = [
]


class Settings(object):
    """Settings for internal use."""
    def __getattr__(self, name):
        print('getting setting {}'.format(name))
        if not hasattr(django_settings, name) and name not in globals():
            print('not found setting {}'.format(name))
            raise ValueError('{} is not found in settings'.format(name))
        s = getattr(django_settings, name, globals()[name])
        print('found setting {}'.format(name))
        return s


settings = Settings()
