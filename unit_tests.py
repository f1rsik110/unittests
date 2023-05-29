import unittest
from start import surname, name, father_name, master_class, master


class TestSite(unittest.TestCase):

    def test_surname(self):
        self.assertEqual(surname("Фирс"), "Фирс")
        self.assertEqual(surname(1.2), "Введено не корректно")
        self.assertEqual(surname(" "), "Введено не корректно")

    def test_name(self):
        self.assertEqual(name("Данил"), "Данил")
        self.assertEqual(name(1.2), "Введено не корректно")
        self.assertEqual(name(" "), "Введено не корректно")

    def test_father_name(self):
        self.assertEqual(father_name("Анатольевич"), "Анатольевич")
        self.assertEqual(father_name(1.2), "Введено не корректно")
        self.assertEqual(father_name(" "), " ")

    def test_master_class(self):
        self.assertEqual(master_class("K-pop"), "K-pop")
        self.assertEqual(master_class("G-pop"), "Введено не корректно")

    def test_master(self):
        self.assertEqual(master("Фирсик"), "Фирсик")
        self.assertEqual(master(1.2), "Введено не корректно")
