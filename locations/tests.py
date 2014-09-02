from django.test import TestCase

from locations.models import Vehicle

class VehicleMethodTests(TestCase):

    def test_was_reported_recently_with_future_report(self):
        """
        was_reported_recently() should return False for vehicles whose
        seconds_since_report is negative (non-sensical / in the future)
        """
        future_report = Vehicle(
            run_id='201_38_01',
            vehicle_id='7184',
            route_id='201',
            seconds_since_report=-1,
            latitude=34.07349,
            longitude=-118.288185,
            heading=255,
            predictable=True
        )
        self.assertEqual(future_report.was_reported_recently(), False)

    def test_was_reported_recently_with_old_report(self):
        """
        was_reported_recently() should return False for vehicles whose
        seconds_since_report is older than 30 seconds
        """
        future_report = Vehicle(
            run_id='201_38_01',
            vehicle_id='7184',
            route_id='201',
            seconds_since_report=31,
            latitude=34.07349,
            longitude=-118.288185,
            heading=255,
            predictable=True
        )
        self.assertEqual(future_report.was_reported_recently(), False)

    def test_was_reported_recently_with_recent_report(self):
        """
        was_reported_recently() should return False for vehicles whose
        seconds_since_report is less than or equal to 30
        """
        future_report = Vehicle(
            run_id='201_38_01',
            vehicle_id='7184',
            route_id='201',
            seconds_since_report=29,
            latitude=34.07349,
            longitude=-118.288185,
            heading=255,
            predictable=True
        )
        self.assertEqual(future_report.was_reported_recently(), True)        