import sys

import paypalrestsdk

class PayPalClient:
    def __init__(self):
        paypalrestsdk.configure({
            "mode": "sandbox",  # Change to "live" in production
            "client_id": "AVsUUMIQu3-izfmZtJNnRWiimZZAlAs5gZFy48oljIgy_ZUUZRx8ZEBcIaSt2elyk9pTtu0xKNV07l9a",
            "client_secret": "EI0EyRDRaY6WCeVQ3usQzmrlkFnZ57XdgP2edD7GHSez2FocttDcYtjfFumrzYgOsda2ukaUZiUaMqGm"
        })

    def get_payment(self, payment_id):
        return paypalrestsdk.Payment.find(payment_id)