# DB router for app1

class App1DBRouter(object):
    """
    A router to control app1 db operations
    """

    @staticmethod
    def db_for_read(model, **hints):
        "Point all operations on app1 models to 'db_app1'"
        from django.conf import settings
        if not settings.DATABASES['db_app1']:
            return None
        if model._meta.app_label == 'product':
            return 'db_app1'
        return None

    @staticmethod
    def db_for_write(model, **hints):
        "Point all operations on app1 models to 'db_app1'"
        from django.conf import settings
        if not settings.DATABASES['db_app1']:
            return None
        if model._meta.app_label == 'product':
            return 'db_app1'
        return None

    @staticmethod
    def allow_relation(obj1, obj2, **hints):
        "Allow any relation if a model in app1 is involved"
        from django.conf import settings
        if not settings.DATABASES['db_app1']:
            return None
        if obj1._meta.app_label == 'product' or obj2._meta.app_label == 'product':
            return True
        return None

    @staticmethod
    def allow_syncdb(db, model):
        "Make sure the app1 app only appears on the 'app1' db"
        from django.conf import settings
        if not settings.DATABASES['db_app1']:
            return None
        if db == 'db_app1':
            return model._meta.app_label == 'product'
        elif model._meta.app_label == 'product':
            return False
        return None
