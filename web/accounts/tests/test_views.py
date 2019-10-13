from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

class IndexPageViewTest(TestCase):
    def test_index_page_view_by_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_index_page_view_by_name(self):
        response= self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    def test_index_page_view_template(self):
        response= self.client.get(reverse('index'))
        self.assertTemplateUsed(response, "accounts/index.html")


# class DashboardPageViewTest(TestCase):
#     def test_index_page_view_by_status_code(self):
#         response = self.client.get('/')
#         self.assertEquals(response.status_code, 200)

#     def test_index_page_view_by_name(self):
#         response= self.client.get(reverse('index'))
#         self.assertEquals(response.status_code, 200)

#     def test_index_page_view_template(self):
#         response= self.client.get(reverse('index'))
#         self.assertTemplateUsed(response, "accounts/index.html")
#         print(response)



class SignInTest(TestCase):
    def setUp(self):
        self.user =  get_user_model().objects.create_user(username='testuser',password="testpassword")
        self.user.save()


    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user =authenticate(username="testuser", password="testpassword")
        self.assertTrue((user is not None) and user.is_authenticated)
    
    def test_wrong_username(self):
        user = authenticate(username='wrong', password='testpassword')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)


class ProfilePageViewTest(TestCase):
    pass


class TicketPricingPageViewTest(TestCase):
    pass