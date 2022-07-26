import unittest
from unittest.mock import patch

from main import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, remove_doc_from_shelf, \
    get_doc_shelf, show_all_docs_info, add_new_doc, delete_doc, append_doc_to_shelf, add_new_shelf


class TestSecretaryProgram(unittest.TestCase):

    @patch('builtins.input', lambda *args: '10')
    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name(), None)

    def test_get_all_doc_owners_names(self):
        self.assertIsNotNone(get_all_doc_owners_names())
        self.assertNotEqual(get_all_doc_owners_names(), None)

    def test_show_all_docs_info(self):
        self.assertIsNone(show_all_docs_info())

    @patch('builtins.input', lambda *args: '10006')
    def test_get_doc_shelf(self):
        self.assertEqual(get_doc_shelf(), '2')

    def test_add_new_doc(self):
        user_input = ['2-656', 'passport', 'Ульяна Копейкина', '3']
        with patch('builtins.input', side_effect=user_input):
            add_doc_result = add_new_doc()
        self.assertEqual(add_doc_result, '3')

    @patch('builtins.input', lambda *args: '2-656')
    def test_delete_doc(self):
        self.assertEqual(delete_doc(), ('2-656', True))

    def test_remove_doc_from_shelf(self):
        self.assertTrue(remove_doc_from_shelf('10006'))
        self.assertFalse(remove_doc_from_shelf('0111'))

    def test_doc_to_shelf(self):
        self.assertTrue(append_doc_to_shelf('1', '3'))

    def test_add_new_shelf(self):
        self.assertEqual(add_new_shelf('4'), ('4', True))
        self.assertEqual(add_new_shelf('3'), ('3', False))

    def test_check_document_existance(self):
        self.assertEqual(check_document_existance('11-2'), True)










