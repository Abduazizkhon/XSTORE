from django.contrib.auth.models import BaseUserManager


class Manager(BaseUserManager):
    def create_user(self, email, password, **extra_fields): #** means not to write all fields of the user it accepts all fields
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password) # to hash the pass we need to use set_password
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        return self.create_user(email, password, **extra_fields)
        

