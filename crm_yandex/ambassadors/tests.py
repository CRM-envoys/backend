from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import (Activity, Ambassador, AmbassadorActivity,
                     AmbassadorPreference, Content, Merch, MerchOnShipping,
                     MerchShipment, Preference, Venue)
from .validators import POSTAL_CODE_VALIDATOR, TELEGRAM_USERNAME_VALIDATOR


class AmbassadorTests(TestCase):

    def setUp(self):
        self.activity = Activity.objects.create(name="Test_activity")
        self.preference = Preference.objects.create(name="Test_preference")
        self.ambassador = Ambassador.objects.create(
            fio="Тест Тестов Тестович",
            sex="М",
            course="analyst",
            country="test_country",
            city="test_city",
            address="test_address",
            postal_code="123456",
            email="testuser@yandex.ru",
            telegram="@test_telegram",
            phone_number="+75555555555",
            education="Test",
            job="test_job",
            goal="test_goal",
            blog_link="https://www.example.com",
            clothing_size="xs",
            foot_size="40",
            comment="test_comment",
            registration_date="2024-01-01",
            promocode="test_promo",
            status="active",
            guide_one=False,
            guide_two=False,
            onboarding=False,
        )
        self.merch = Merch.objects.create(
            merch_type="test",
            cost="25.00",
        )
        self.merch_shipment = MerchShipment.objects.create(
            curator="Test Test",
            ambassador=self.ambassador,
            date="2024-01-01",
            comment="test_comment"
        )
        self.venue = Venue.objects.create(name="test_venue")
        self.content = Content.objects.create(
            ambassador=self.ambassador,
            link="https://www.example.com",
            venue=self.venue,
            date="2024-01-01",
            guide_followed=False
        )
        self.ambassador_activity = AmbassadorActivity.objects.create(
            ambassador=self.ambassador,
            activity=self.activity
        )
        self.ambassador_preference = AmbassadorPreference.objects.create(
            ambassador=self.ambassador,
            preference=self.preference
        )
        self.merch_on_shipping = MerchOnShipping.objects.create(
            shipping=self.merch_shipment,
            merch=self.merch
        )

    def test_activity_listing(self):
        self.assertEqual(self.activity.name, "Test_activity")

    def test_preference_listing(self):
        self.assertEqual(self.preference.name, "Test_preference")

    def test_ambassador_listing(self):
        self.assertEqual(self.ambassador.fio, "Тест Тестов Тестович")
        self.assertEqual(self.ambassador.sex, "М")
        self.assertEqual(self.ambassador.course, "analyst")
        self.assertEqual(self.ambassador.country, "test_country")
        self.assertEqual(self.ambassador.city, "test_city")
        self.assertEqual(self.ambassador.address, "test_address")
        self.assertEqual(self.ambassador.postal_code, "123456")
        self.assertEqual(self.ambassador.email, "testuser@yandex.ru")
        self.assertEqual(self.ambassador.phone_number, "+75555555555")
        self.assertEqual(self.ambassador.telegram, "@test_telegram")
        self.assertEqual(self.ambassador.education, "Test")
        self.assertEqual(self.ambassador.job, "test_job")
        self.assertEqual(self.ambassador.goal, "test_goal")
        self.assertEqual(self.ambassador.blog_link, "https://www.example.com")
        self.assertEqual(self.ambassador.clothing_size, "xs")
        self.assertEqual(self.ambassador.foot_size, "40")
        self.assertEqual(self.ambassador.comment, "test_comment")
        self.assertEqual(self.ambassador.registration_date, "2024-01-01")
        self.assertEqual(self.ambassador.promocode, "test_promo")
        self.assertEqual(self.ambassador.status, "active")
        self.assertEqual(self.ambassador.guide_one, False)
        self.assertEqual(self.ambassador.guide_two, False)
        self.assertEqual(self.ambassador.onboarding, False)

    def test_merch_listing(self):
        self.assertEqual(self.merch.merch_type, "test")
        self.assertEqual(self.merch.cost, "25.00")

    def test_merch_shipment_listing(self):
        self.assertEqual(self.merch_shipment.curator, "Test Test")
        self.assertEqual(
            self.merch_shipment.ambassador.fio,
            "Тест Тестов Тестович"
        )
        self.assertEqual(self.merch_shipment.date, "2024-01-01")
        self.assertEqual(self.merch_shipment.comment, "test_comment")

    def test_models_have_correct_object_names(self):
        model_str = {
            self.activity: self.activity.name,
            self.preference: self.preference.name,
            self.ambassador: self.ambassador.fio,
            self.merch: f"{self.merch.merch_type} - {self.merch.cost}",
            self.merch_shipment: (
                f"Ambassador ID: {self.merch_shipment.ambassador.id} - "
                f"{self.merch_shipment.date}"
            ),
            self.venue: self.venue.name,
            self.content: (
                f"Амбассадор: {self.content.ambassador.fio} "
                f"{self.content.link}"
            )
        }
        for model, expected_value in model_str.items():
            with self.subTest(model=model):
                self.assertEqual(expected_value, str(model))

    def test_relationships(self):
        self.assertEqual(self.ambassador_activity.ambassador, self.ambassador)
        self.assertEqual(self.ambassador_activity.activity, self.activity)
        self.assertEqual(
            self.ambassador_preference.ambassador, self.ambassador
        )
        self.assertEqual(
            self.ambassador_preference.preference, self.preference
        )
        self.assertEqual(self.merch_on_shipping.shipping, self.merch_shipment)
        self.assertEqual(self.merch_on_shipping.merch, self.merch)
        self.assertEqual(self.merch_shipment.ambassador, self.ambassador)
        self.assertEqual(self.content.venue, self.venue)
        self.assertEqual(self.content.ambassador, self.ambassador)


class ModelValidatorTests(TestCase):

    def test_postal_code_validator(self):
        invalid_postal_code = "1234567"
        with self.assertRaises(ValidationError):
            POSTAL_CODE_VALIDATOR(invalid_postal_code)

    def test_telegram_username_validator(self):
        invalid_telegram_username = "test_username"
        with self.assertRaises(ValidationError):
            TELEGRAM_USERNAME_VALIDATOR(invalid_telegram_username)
