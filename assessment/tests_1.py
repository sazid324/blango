from rest_framework.test import APIClient, APITestCase


class Question1TestCase(APITestCase):
    def test_client_attributes(self):
        q1tc = self
        self.assertIsInstance(q1tc.client, APIClient)
        self.assertTrue(
            hasattr(q1tc, "client"), "APITestCase should provide a 'client' attribute"
        )


class Question2TestCase(APITestCase):
    def test_client_methods_available(self):
        self.assertTrue(
            hasattr(self.client, "get"), "Client should have a 'get' method"
        )
        self.assertTrue(
            hasattr(self.client, "post"), "Client should have a 'post' method"
        )
        self.assertTrue(
            hasattr(self.client, "put"), "Client should have a 'put' method"
        )
        self.assertTrue(
            hasattr(self.client, "patch"), "Client should have a 'patch' method"
        )
        self.assertTrue(
            hasattr(self.client, "delete"), "Client should have a 'delete' method"
        )
