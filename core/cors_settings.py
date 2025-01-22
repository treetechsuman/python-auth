from corsheaders.defaults import default_headers

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://192.168.1.105:5173",  # Replace with your React app's URL
    "http://localhost:5173",
    "https://react-stater.vercel.app"
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    'X-CSRFTOKEN',  # Explicitly allow this header
]

# CSRF settings
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://192.168.1.105:5173",
    "https://react-stater.vercel.app/",
]
