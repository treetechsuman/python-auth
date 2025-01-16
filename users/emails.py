from djoser.email import PasswordResetEmail
from djoser.email import ActivationEmail
import os
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")

class CustomPasswordResetEmail(PasswordResetEmail):
    template_name = "users/password_reset.html"
    plain_text_template_name = "users/password_reset.txt"  # Path to your plain text template

    def get_context_data(self):
        context = super().get_context_data()
        # Use the frontend URL instead of the backend URL
        context["url"] = f"{FRONTEND_URL}/password-reset/confirm/{context['uid']}/{context['token']}"
        print("Email context:", context)  # Log context for debugging
        return context

    def get_subject(self):
        # Define your custom subject
        print("Custom subject is being used!")
        return "Reset Your Password - My Application"


class CustomAccountActivationEmail(ActivationEmail):
    template_name = "users/account_activation.html"
    plain_text_template_name = "users/account_activation.txt"  # Path to your plain text template

    def get_context_data(self):
        context = super().get_context_data()
        # Use the frontend URL to direct users to the activation page
        context["url"] = f"{FRONTEND_URL}/activate/{context['uid']}/{context['token']}"
        print("Activation email context:", context)  # Log context for debugging
        return context

    def get_subject(self):
        # Define your custom subject
        print("Custom activation email subject is being used!")
        return "Activate Your Account - My Application"