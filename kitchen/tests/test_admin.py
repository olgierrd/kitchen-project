from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="testadmin",
            password="testadminpass",
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="testcook",
            password="testcookpass",
            first_name="Test",
            last_name="Cook",
            years_of_experience=5,
        )

    def test_cook_experience_listed(self) -> None:
        """
        Test that cook experience is listed
        in admin user list
        :return:
        """
        url = reverse("admin:kitchen_cook_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_detail_experience_listed(self) -> None:
        """
        Test that cook detail page displays experience
        :return:
        """
        url = reverse("admin:kitchen_cook_change", args=[self.cook.id])
        res = self.client.get(url)
