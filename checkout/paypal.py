import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AVsUUMIQu3-izfmZtJNnRWiimZZAlAs5gZFy48oljIgy_ZUUZRx8ZEBcIaSt2elyk9pTtu0xKNV07l9a"
        self.client_secret = "EI0EyRDRaY6WCeVQ3usQzmrlkFnZ57XdgP2edD7GHSez2FocttDcYtjfFumrzYgOsda2ukaUZiUaMqGm"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)