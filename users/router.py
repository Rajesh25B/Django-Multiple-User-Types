class AuthRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'users',}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'users' # return users db
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write to our user model.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'users'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        As cross-db relationships dont support in django, this makes sure
        that relations happen to my model are happening in this context of this
        route_app_label which includes my users app. Only models in my users 
        app gonna be allow to have a relationships btwn them.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure that users app only appear in the
        'users' database. when migrate, that migrations gonna go to users db
        """
        if app_label in self.route_app_labels:
            return db == 'users'
        return None
