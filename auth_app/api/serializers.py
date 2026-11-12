from rest_framework import serializers

from ..models import User

# im Frontend wird name (full_name) angenommen

class SignUpSerializer(serializers.ModelSerializer):
    """Validates registration data and creates a new user."""
    password = serializers.CharField(write_only=True, trim_whitespace=False, min_length=6)
    confirm_password = serializers.CharField(write_only=True, trim_whitespace=False, min_length=6)
    full_name = serializers.CharField(max_length=255, write_only=True)
    class Meta:
        model = User
        fields = ('full_name', 'email', 'password', 'confirm_password')
        
    
    def validate(self, data):
        ''' Checks that the password and confirmation match and returns the validated data. '''
        if data['confirm_password']!= data['password']:
            raise serializers.ValidationError("Die Passwörter stimmen nicht überein")
        
        if len(data['full_name'].split()) < 2:
             raise serializers.ValidationError({"full_name": "Bitte gib Vor- und Nachnamen ein"})
        
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