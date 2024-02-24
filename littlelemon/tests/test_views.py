from django.test import TestCase

from restaurant.models import Menu
from restaurant.views import MenuItemsView


class MenuViewTest(TestCase):

    def setUp(self) -> None:
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)

    def test_get_all(self):
        items = Menu.objects.all()
        self.assertListEqual([str(i) for i in items], ["IceCream : 80.00"])
