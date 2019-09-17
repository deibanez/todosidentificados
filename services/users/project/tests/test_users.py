# services/users/project/tests/test_users.py
import json
import unittest

from project.tests.base import BaseTestCase
from project.tests.utils import add_user


class TestUserService(BaseTestCase):
    """Tests for the Users Service."""

    def test_users(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get("/users/ping")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("pong!", data["message"])
        self.assertIn("success", data["status"])

    def test_add_user(self):
        """Ensure a new user can be added to the database."""
        with self.client as client:
            response = client.post(
                "/users",
                data=json.dumps(
                    {
                        "username": "zippy",
                        "email": "zippy@fakemail.org",
                        "password": "greaterthaneight",
                    }
                ),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn("zippy@fakemail.org was added!", data["message"])
            self.assertIn("success", data["status"])

    def test_add_user_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty."""
        with self.client as client:
            response = client.post(
                "/users", data=json.dumps({}), content_type="application/json"
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid payload.", data["message"])
            self.assertIn("fail", data["status"])

    def test_add_user_invalid_json_keys(self):
        """Ensure error is thrown if the JSON object does not have a username key."""  # noqa: E501
        with self.client as client:
            response = client.post(
                "/users",
                data=json.dumps(
                    {
                        "email": "zippy@fakemail.org",
                        "password": "greaterthaneight",
                    }
                ),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid payload.", data["message"])
            self.assertIn("fail", data["status"])

    def test_add_user_duplicate_email(self):
        """Ensure error is thrown if the email already exists."""
        with self.client as client:
            client.post(
                "/users",
                data=json.dumps(
                    {
                        "username": "zippy",
                        "email": "zippy@fakemail.org",
                        "password": "greaterthaneight",
                    }
                ),
                content_type="application/json",
            )
            response = self.client.post(
                "/users",
                data=json.dumps(
                    {
                        "username": "zippy",
                        "email": "zippy@fakemail.org",
                        "password": "greaterthaneight",
                    }
                ),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("Sorry. That email already exists.", data["message"])
            self.assertIn("fail", data["status"])

    def test_single_user(self):
        """Ensure get single user behaves correctly."""
        user = add_user("zippy", "zippy@fakemail.org", "greaterthaneight")
        with self.client as client:
            response = client.get(f"/users/{user.id}")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn("zippy", data["data"]["username"])
            self.assertIn("zippy@fakemail.org", data["data"]["email"])
            self.assertIn("success", data["status"])

    def test_single_user_no_id(self):
        """Ensure error is thrown if an id is not provided."""
        with self.client as client:
            response = client.get("/users/blah")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn("User does not exist", data["message"])
            self.assertIn("fail", data["status"])

    def test_single_user_incorrect_id(self):
        """Ensure error is thrown if the id does not exist."""
        with self.client as client:
            response = client.get("/users/999")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn("User does not exist", data["message"])
            self.assertIn("fail", data["status"])

    def test_all_users(self):
        """Ensure get all users behaves correctly."""
        add_user("zippy", "zippy@fakemail.org", "greaterthaneight")
        add_user("sconf", "sconf@notreal.com", "greaterthaneight")
        with self.client as client:
            response = client.get("/users")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data["data"]["users"]), 2)
            self.assertIn("zippy", data["data"]["users"][0]["username"])
            self.assertIn(
                "zippy@fakemail.org", data["data"]["users"][0]["email"]
            )
            self.assertIn("sconf", data["data"]["users"][1]["username"])
            self.assertIn(
                "sconf@notreal.com", data["data"]["users"][1]["email"]
            )
            self.assertIn("success", data["status"])

    def test_main_no_users(self):
        """Ensure the main route behaves correctly when no users have been
        added to the database."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"All Users", response.data)
        self.assertIn(b"<p>No users!</p>", response.data)

    def test_main_with_users(self):
        """Ensure the main route behaves correctly when users have been
        added to the database."""
        add_user("zippy", "zippy@fakemail.org", "greaterthaneight")
        add_user("sconf", "sconf@notreal.com", "greaterthaneight")
        with self.client as client:
            response = client.get("/")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"All Users", response.data)
            self.assertNotIn(b"<p>No users!</p>", response.data)
            self.assertIn(b"zippy", response.data)
            self.assertIn(b"sconf", response.data)

    def test_main_add_user(self):
        """Ensure a new user can be added to the database via a POST request."""  # noqa: E501
        with self.client as client:
            response = client.post(
                "/",
                data=dict(
                    username="zippy",
                    email="zippy@sonotreal.com",
                    password="greaterthaneight",
                ),
                follow_redirects=True,
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"All Users", response.data)
            self.assertNotIn(b"<p>No users!</p>", response.data)
            self.assertIn(b"zippy", response.data)

    def test_add_user_invalid_json_keys_no_password(self):
        """Ensure error is thrown if the JSON object does not have a password key."""  # noqa: E501
        with self.client:
            response = self.client.post(
                "/users",
                data=json.dumps(
                    dict(username="zippy", email="zippy@reallynotreal.com")
                ),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid payload.", data["message"])
            self.assertIn("fail", data["status"])


if __name__ == "__main__":
    unittest.main()
