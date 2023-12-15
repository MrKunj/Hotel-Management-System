from odoo import api, models, fields
from datetime import date
from datetime import datetime
from odoo.exceptions import UserError


# This file been used by the waiter
class CustomerSection(models.Model):
    _name = "customer.section"
    _description = "To get and add all the details of customer and take the order as per requirement"
    # Enter the rec name which will directly fetct and show the name on the top of the form view
    _rec_name = "customer_name"

    # Manual Data entry by the waiter, when he reaches the table
    customer_name = fields.Char(string="Customer Name: ")
    customer_gender = fields.Char(string="Customer Gender: ")
    customer_phoneNumber = fields.Char(string="Contact Number: ")
    customer_member = fields.Char(string="Total Member: ")
    customer_occation = fields.Char(string="Customer Occation: ")
    customer_refference = fields.Char(string="Customer Refference: ")

    # All Below fields are computed fields
    # Automatic and calculated Data entry. Date, Time, Day, Generate Customer ID,
    # This will be generated on saving the details of the customer
    rand_id = fields.Char(string="", readonly=True, store=True)
    time = fields.Char(string="Time: ", readonly=True, store=True)
    day = fields.Char(string="Day: ", readonly=True, store=True)
    # Date at which the customer enters the restaurent
    date = fields.Char(string="Date: ", readonly=True, store=True)


    def customerSeatID(self):
        import random
        import string
        num_seats = 50
        prefix = "SEAT --> "
        suffix = ''.join(random.choices(string.digits, k=3))
        seat_number = prefix + suffix
        self.rand_id = seat_number

    def currentTime(self):
        import datetime
        import pytz
        indian_timezone = pytz.timezone('Asia/Kolkata')
        current_time = datetime.datetime.now(indian_timezone)
        time_string = current_time.strftime('%I:%M:%S %p')
        self.time = time_string

    def currentDay(self):
        import datetime
        today1 = datetime.date.today()
        day_index = today1.weekday()
        days_of_week = ['Monday', 'Tuesday', 'Wednesday',
                        'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_name = days_of_week[day_index]
        self.day = str(day_name)

    def currentDate(self):
        import datetime
        today2 = datetime.date.today()
        day = today2.strftime("%d")
        if day.endswith("1") and day != "11":
            suffix = "st"
        elif day.endswith("2") and day != "12":
            suffix = "nd"
        elif day.endswith("3") and day != "13":
            suffix = "rd"
        else:
            suffix = "th"
        month = today2.strftime("%B")
        checker = f"{day}{suffix} {month}"
        self.date = checker

    def currentAll(self):
        self.customerSeatID()
        self.currentTime()
        self.currentDay()
        self.currentDate()
        # raise UserError(f"Hello, Sir {self.customer_name}")

