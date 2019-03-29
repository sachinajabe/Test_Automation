import datetime
class DateGet():

    def start_day(self):
        a = datetime.datetime.today()
        a1= a + datetime.timedelta(days=1)
        ate_1 = datetime.date.strftime(a1, "%m/%d/%Y")
        return ate_1

    def return_day(self):
        a = datetime.datetime.today()
        a2= a + datetime.timedelta(days=22)
        ate_2 = datetime.date.strftime(a2, "%m/%d/%Y")
        return ate_2
                # r_date.send_keys(ate_1)
                # time.sleep(5)