from drivers.models import Driver

MAX_RANGE = 5


def get_nearest_driver(latitude, longitude):
    """
    Function to get the nearest driver for given location
    """
    def _get_min_max_point(direction, distance):
        return direction-distance, direction+distance

    for distance in range(1, MAX_RANGE+1):
        min_latitude, max_latitude = _get_min_max_point(latitude, distance)
        min_longitude, max_longitude = _get_min_max_point(longitude, distance)
        driver = Driver.objects.filter(
            latitude__lte=max_latitude, latitude__gte=min_latitude,
            longitude__lte=max_longitude, longitude__gte=min_longitude,
            current_ride__isnull=True
        )
        if driver.exists():
            return driver.first()
    return None
