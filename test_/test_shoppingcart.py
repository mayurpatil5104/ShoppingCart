import pytest

from POM.shopping_cart import ShoppingCart
from Data import reading_objects
zip_list = reading_objects.zip_code


class TestShoppingCart:

    @pytest.mark.parametrize("zip_",zip_list)
    def test_shopping_cart(self, _driver,zip_):
        sc = ShoppingCart(_driver)
        sc.click_shopping_cart()
        sc.select_and_update()
        sc.discount_code()
        sc.gift_card()
        sc.select_country()
        sc.zip_postal_code(zip_)
        sc.estimate_shipping_details()
        sc.terms_of_services()
        sc.checkout()

