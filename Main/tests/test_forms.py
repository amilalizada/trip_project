from django.test import TestCase
from Main.forms import ContactForm

class ContactFormTestCase(TestCase):

    def setUp(self):
        self.valid_data = {
            'name': 'Aqil',
            'email': 'agil.mahmud@mail.ru',
            'subject': 'Sayt islemir',
            'message': 'Veziyyet pisdi'
        }

        self.invalid_data = {
            'name': 'AqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqil',
            'email': 'agil.mahmud',
            'subject': 'Sayt islemir',
            'message': 'Veziyyet pisdi'
        }
        self.invalid_data2 = {
            'name': 'AqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqilAqil',
            'email': 'agil.mahmud',

        }

    def test_valid_data(self):
        form = ContactForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = ContactForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertIn('name',form.errors.keys())
        self.assertIn('Bu dəyərin ən çox 40 simvol olduğuna əmin olun (80 var)',form.errors['name'])

    def test_invalid_data2(self):
        form = ContactForm(data=self.invalid_data2)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)