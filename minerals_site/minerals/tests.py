from django.utils import timezone
from django.urls import reverse
from django.test import TestCase

from .models import Mineral


class MineralModelTests(TestCase):
    def setUp(self):
        self.mineral1 = Mineral.objects.create(name="A Cool Name")
        self.mineral2 = Mineral.objects.create(name="A Different Name")

    def test_mineral_creation(self):
        now = timezone.now()
        self.assertLess(self.mineral1.created_at, now)

    def test_slug_generation(self):
        self.assertTrue(self.mineral1.slug == "a-cool-name")


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral1 = Mineral.objects.create(name="A Cool Name")
        self.mineral2 = Mineral.objects.create(name="A Different Name")

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral1, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail', kwargs={'slug': self.mineral1.slug}))
        self.assertEqual(resp.status_code, 200)
