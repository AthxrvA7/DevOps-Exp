import unittest
from app import hello_world, welcome_message

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_message(self):
        self.assertEqual(hello_world(), "Hello, DevOps!")

    def test_hello_world_returns_string(self):
        self.assertIsInstance(hello_world(), str)

    def test_welcome_message_atharva(self):
        self.assertEqual(welcome_message("Atharva"), "Welcome to DevOps, Atharva!")

    def test_welcome_message_riya(self):
        self.assertEqual(welcome_message("Riya"), "Welcome to DevOps, Riya!")

if __name__ == "__main__":
    unittest.main()