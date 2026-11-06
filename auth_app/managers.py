from django.contrib.auth.base_user import BaseUserManager # Provides the base functionality for a custom user manager


class UserManager(BaseUserManager):
    """Creates, validates, and saves a user with a hashed password, then returns the user."""
    def create_user(self, email, password=None, **extra_fields): # **extra fields collects additional informations in a dictonary for example {"first_name": "Solo", "last_name": "Ka"}
        if not email:
            raise ValueError("Die E-Mail Adresse ist erforderlich")
        
        email = self.normalize_email(email) # Normalizes the email address by converting the domain part (after @) to lowercase
        user = self.model(email=email, **extra_fields) # creates a user object
        user.set_password(password) # creates a hashed password
        user.full_clean() # Validates the user data and raises a ValidationError if any model rules are violated
        user.save(using=self._db) # Saves the user to the database selected by this manager # using=self._db -> which database will be chosen
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Der superuser muss 'is_staff=True' haben")
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Der superuser muss 'is_superuser=True' haben")
        
        return self.create_user(email, password, **extra_fields)