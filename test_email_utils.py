import unittest
from email_utils import is_valid, get_domain, local_part, masked_email

class TestEmailUtils(unittest.TestCase):
    def test_is_valid(self):
        self.assertTrue(is_valid("john.doe@example.com"))
        self.assertTrue(is_valid("user+tag@sub.domain.co.uk"))
        self.assertFalse(is_valid("not-an-email"))
        self.assertFalse(is_valid(123))
        self.assertFalse(is_valid(None))
        self.assertFalse(is_valid("foo@bar"))

    def test_get_domain(self):
        self.assertEqual(get_domain("john.doe@example.com"), "example.com")
        self.assertEqual(get_domain("a@b.co"), "b.co")
        self.assertEqual(get_domain("noatsign"), "")
        self.assertEqual(get_domain(123), "")

    def test_local_part(self):
        self.assertEqual(local_part("john.doe@example.com"), "john.doe")
        self.assertEqual(local_part("a@b.co"), "a")
        self.assertEqual(local_part("noatsign"), "")
        self.assertEqual(local_part(123), "")

    def test_masked_email(self):
        self.assertEqual(masked_email("john.doe@example.com", show=2), "jo******@example.com")
        self.assertEqual(masked_email("ab@example.com", show=2), "ab@example.com")
        self.assertEqual(masked_email("a@example.com", show=2), "a@example.com")
        self.assertEqual(masked_email("john.doe@example.com", show=0), "********@example.com")
        self.assertEqual(masked_email("not-an-email", show=2), "not-an-email")
        self.assertEqual(masked_email(123), 123)

if __name__ == "__main__":
    unittest.main()
