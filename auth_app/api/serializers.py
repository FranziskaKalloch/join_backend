from rest_framework import serializers

from ..models import User

# im Frontend wird name (full_name) angenommen

class SignUpSerializer(serializers.ModelSerializer):
    """Validates registration data and creates a new user."""
    password = serializers.CharField(write_only=True, trim_whitespace=False, min_length=6)
    confirm_password = serializers.CharField(write_only=True, trim_whitespace=False, min_length=6)
    full_name = serializers.CharField(max_length=255, write_only=True)
    privacy_policy = serializers.BooleanField(required=True, write_only=True)
    class Meta:
        model = User
        fields = ('full_name', 'email', 'password', 'confirm_password', 'privacy_policy')
        
    
    def validate(self, data):
        ''' Checks that the password and confirmation match and returns the validated data. '''
        if data['confirm_password']!= data['password']:
            raise serializers.ValidationError("Die Passwörter stimmen nicht überein")
        
        if len(data['full_name'].split()) < 2:
             raise serializers.ValidationError({"full_name": "Bitte gib Vor- und Nachnamen ein"})
        
        first_name, last_name = data["full_name"].split(maxsplit=1) # maxsplit=1 - höchstens einmal aufteilen
        if len(first_name) > 150:
            raise serializers.ValidationError({
                "first_name": "Der Vorname darf maximal 150 Zeichen haben"
            })
        
        if len(last_name) > 150:
            raise serializers.ValidationError({
                "last_name": "Der Nachname darf maximal 150 Zeichen haben"
                })
        
        privacy_policy = data['privacy_policy']
        if privacy_policy != True:
            raise serializers.ValidationError({
                "privacy_policy": "Privacy Policy muss ausgewählt werden"
                })
        
        return data
    
    def create(self, data):
        ''' Creates user with validated data '''
        full_name = data['full_name']
        first_name, last_name = full_name.split(maxsplit=1) # Splits the full name at the first whitespace and assigns the two parts to first_name and last_name.
        
        user = User.objects.create_user(
            email=data['email'],
            password=data['password'],
            first_name= first_name,
            last_name= last_name,
        )
        return user