
#from utils import add_years_to_date
from Cars.Batteries.Battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_service_date):
        self.current_service_date = current_service_date
        self.last_service_date = last_service_date

    def needs_service(self):

        return self.current_service_date > (self.last_service_date.replace(year=self.last_service_date.year + 3))
