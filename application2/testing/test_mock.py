from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application2.app import animals, animalsnoises
from application2 import app


class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_football(self):
        with patch('requests.get') as g:
            g.return_value.text = "Dog"

            response = self.client.get(url_for('animalsnoises'))
            self.assertIn(b'Dog Woof', response.data)
