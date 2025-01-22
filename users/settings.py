# User app specific settings

# Custom User Model
AUTH_USER_MODEL = 'users.CustomUser'

# Djoser Configuration
DJOSER = {
    'USER_ID_FIELD': 'email',  # Use email as the unique identifier
    'LOGIN_FIELD': 'email',  # Specify email as the login field
    'SET_PASSWORD_RETYPE': True,  # Requires re_new_password for confirmation
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,  # Sends confirmation email after password change
    'USER_CREATE_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_URL': 'http://192.168.1.105:5173/password/reset/confirm/{uid}/{token}',
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    "EMAIL": {
        #"password_reset": "djoser.email.PasswordResetEmail",
        "password_reset": "users.emails.CustomPasswordResetEmail",
        "activation": "users.emails.CustomAccountActivationEmail",
    },
    'SERIALIZERS': {
        'user_create': 'users.serializers.CustomUserCreateSerializer',
        'user': 'users.serializers.CustomUserSerializer',
        'set_password': 'djoser.serializers.SetPasswordSerializer',
    },
}

# DRF and JWT settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
}
