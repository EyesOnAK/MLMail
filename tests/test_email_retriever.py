# tests/test_email_retriever.py

import unittest
from unittest.mock import MagicMock, Mock
from email.message import EmailMessage
from email_retriever import fetch_emails

class TestEmailRetriever(unittest.TestCase):

    def test_fetch_emails(self):
        # Create a mock mail object
        mock_mail = MagicMock()
        
        # Mock the behavior of the mail object methods
        mock_mail.select.return_value = ('OK', ['1'])
        mock_mail.search.return_value = ('OK', [b'1'])
        
        # Create a mock email message
        mock_email = EmailMessage()
        mock_email["Subject"] = "Test Subject"
        mock_email["From"] = "test@example.com"
        mock_email.set_payload("This is a test email.")

        # Mock the fetch method to return a properly formatted email
        mock_mail.fetch.return_value = ('OK', [(b'1', mock_email.as_bytes())])

        # Call fetch_emails with the mock mail object
        result = fetch_emails(mock_mail)

        # Add assertions based on your function's expected behavior
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
