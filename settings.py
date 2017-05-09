from django.conf import settings as django_settings


SU_ADMIN_NAME = "Django Admin"

SU_ADMIN_MENU = [
]


class Settings(object):
    """Settings for internal use."""
    def __getattr__(self, name):
        if not hasattr(django_settings, name) and name not in globals():
            raise ValueError('{} is not found in settings'.format(name))
        s = getattr(django_settings, name, globals()[name])
        return s


settings = Settings()
