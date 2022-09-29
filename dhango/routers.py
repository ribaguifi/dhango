class FlaskRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'dhango'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to flask_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'flask_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to flask_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'flask_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the dhango app is involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the dhango app only appear in the 'flask_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'flask_db'
        return None
