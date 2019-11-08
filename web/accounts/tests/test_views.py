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

class SponsorshipViewTest(TestCase):
    def test_sponsorship_page_view_by_status_code(self):
        response = self.client.get('/sponsorship')
        self.assertEquals(response.status_code, 200)

    def test_sponsorship_page_view_by_name(self):
        response= self.client.get(reverse('donate'))
        self.assertEquals(response.status_code, 200)

    def test_index_page_view_template(self):
        response= self.client.get(reverse('donate'))
        self.assertTemplateUsed(response, "accounts/sponsorship.html")


class ThanksViewTest(TestCase):
    def test_thanks_page_view_by_status_code(self):
        response = self.client.get('/thank-you')
        self.assertEquals(response.status_code, 200)

    def test_sponsorship_page_view_by_name(self):
        response= self.client.get(reverse('thanks'))
        self.assertEquals(response.status_code, 200)

    def test_index_page_view_template(self):
        response= self.client.get(reverse('thanks'))
        self.assertTemplateUsed(response, "accounts/sponsor-thanks.html")



class TicketPayCorporateViewTest(TestCase):
    def test_ticket_pay_corp_page_view_by_status_code(self):
        response = self.client.get('/ticket-pay-corp')
        self.assertEquals(response.status_code, 200)

    def test_ticket_pay_corp_page_view_by_name(self):
        response= self.client.get(reverse('ticket_pay_corporate'))
        self.assertEquals(response.status_code, 200)

    def test_ticket_pay_corp_page_view_template(self):
        response= self.client.get(reverse('ticket_pay_corporate'))
        self.assertTemplateUsed(response, "accounts/ticket_pay_corporate.html")


class TicketPayIndividualViewTest(TestCase):
    def test_ticket_pay_indeividual_page_view_by_status_code(self):
        response = self.client.get('/ticket-pay-indiv')
        self.assertEquals(response.status_code, 200)

    def test_ticket_pay_indeividual_page_view_by_name(self):
        response= self.client.get(reverse('ticket_pay_individual'))
        self.assertEquals(response.status_code, 200)

    def test_ticket_pay_indeividual_page_view_template(self):
        response= self.client.get(reverse('ticket_pay_individual'))
        self.assertTemplateUsed(response, "accounts/ticket_pay_individual.html")


class TicketPayStudentsViewTest(TestCase):

    def test_ticket_pay_student_page_view_by_status_code(self):
        response = self.client.get('/ticket-pay-stud')
        self.assertEquals(response.status_code, 200)

    def test_ticket_pay_student_page_view_by_name(self):
        response= self.client.get(reverse('ticket_pay_students'))
        self.assertEquals(response.status_code, 200)

    def test_ticket_pay_student_page_view_template(self):
        response= self.client.get(reverse('ticket_pay_students'))
        self.assertTemplateUsed(response, "accounts/ticket_pay_students.html")
