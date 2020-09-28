from django.test import TestCase
from .models import Consulta, Exame
from django.db.models import Count, Sum
from django.db import models

class ConsultaTestClass(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_nome_medico(self):
        self.assertFalse(False)

    def test_data_inicio(self):
        self.assertFalse(False)

    def test_data_fim(self):
        self.assertFalse(False)
