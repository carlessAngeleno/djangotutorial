from django.test import TestCase
from django.core.urlresolvers import reverse

from locations.models import Vehicle

class VehicleMethodTests(TestCase):

    def test_was_reported_recently_with_future_vehicle(self):
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

    def test_was_reported_recently_with_old_vehicle(self):
        """
        was_reported_recently() should return False for vehicles whose
        seconds_since_report is older than 30 seconds
        """
        old_report = Vehicle(
            run_id='201_38_01',
            vehicle_id='7184',
            route_id='201',
            seconds_since_report=31,
            latitude=34.07349,
            longitude=-118.288185,
            heading=255,
            predictable=True
        )
        self.assertEqual(old_report.was_reported_recently(), False)

    def test_was_reported_recently_with_recent_vehicle(self):
        """
        was_reported_recently() should return False for vehicles whose
        seconds_since_report is less than or equal to 30
        """
        recent_report = Vehicle(
            run_id='201_38_01',
            vehicle_id='7184',
            route_id='201',
            seconds_since_report=29,
            latitude=34.07349,
            longitude=-118.288185,
            heading=255,
            predictable=True
        )
        self.assertEqual(recent_report.was_reported_recently(), True)


def create_vehicle(run_id, vehicle_id, route_id, seconds_since_report,
                    latitude, longitude, heading, predictable):
    return Vehicle.objects.create(
            run_id=run_id,
            vehicle_id=vehicle_id,
            route_id=route_id,
            seconds_since_report=seconds_since_report,
            latitude=latitude,
            longitude=longitude,
            heading=heading,
            predictable=predictable
        )


class VehicleViewTests(TestCase):
    def test_index_view_with_no_vehicles(self):
        """
        If no vehicles exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('locations:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No vehicles are available.")
        self.assertQuerysetEqual(
            response.context['latest_vehicle_list'],
            []
        )

    def test_index_view_with_a_past_vehicle(self):
        """
        Vehicles with a positive seconds_since_report lte 30 should be
        displayed on the index page.
        """
        create_vehicle(
            run_id='201_38_01',
            vehicle_id='7184',
            route_id='201',
            seconds_since_report=29,
            latitude=34.07349,
            longitude=-118.288185,
            heading=255,
            predictable=True            
        )
        response = self.client.get(reverse('locations:index'))
        self.assertQuerysetEqual(
            response.context['latest_vehicle_list'],
            ['<Vehicle: 7184>']
        )

    def test_detail_view_with_a_future_vehicle(self):
        """
        Details page for vehicles with negative seconds_since_report should
        not be accessible.
        """
        future_vehicle = create_vehicle(
            run_id='201_38_01',
            vehicle_id='7184',
            route_id='201',
            seconds_since_report=-9,
            latitude=34.07349,
            longitude=-118.288185,
            heading=255,
            predictable=True            
        )
        response = self.client.get(reverse('locations:detail', args=(future_vehicle.id,)))
        self.assertEqual(response.status_code, 404)