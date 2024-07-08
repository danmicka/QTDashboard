from datetime import datetime, timedelta
import pytz

class QuarterlyCycles:
    def __init__(self, dt: datetime, timezone: str = 'UTC'):
        self.timezone = pytz.timezone(timezone)
        if dt.tzinfo is None:
            self.dt = self.timezone.localize(dt)
        else:
            self.dt = dt.astimezone(self.timezone)
        self.year = self.dt.year
        self.month = self.dt.month
        self.day = self.dt.day
        self.hour = self.dt.hour
        self.minute = self.dt.minute

    def format_datetime(self, dt: datetime):
        return dt.strftime("%d/%m/%Y %H:%M")

    def get_start_of_first_full_week(self):
        first_day_of_month = self.timezone.localize(datetime(self.year, self.month, 1))
        first_sunday_6pm = first_day_of_month + timedelta(days=(6 - first_day_of_month.weekday() + 1) % 7, hours=18 - first_day_of_month.hour)
        if first_sunday_6pm.day > 1:
            first_sunday_6pm += timedelta(days=7)
        return first_sunday_6pm

    def get_first_monday(self):
        first_day = datetime(self.year, self.month, 1)
        first_monday = first_day + timedelta(days=(7 - first_day.weekday()) % 7)
        return self.timezone.localize(first_monday)

    def get_yearly_quarter(self):
        quarters = [(1, 3), (4, 6), (7, 9), (10, 12)]
        for i, (start, end) in enumerate(quarters, 1):
            if start <= self.month <= end:
                start_dt = self.timezone.localize(datetime(self.year, start, 1))
                end_dt = self.timezone.localize(datetime(self.year, end + 1, 1)) - timedelta(days=1)
                return f"Q{i}", (start_dt, end_dt)
        return None

    def get_monthly_quarter(self):
        first_monday = self.get_first_monday()
        quarters = [(first_monday - timedelta(days=1) + timedelta(hours=18))]
        for i in range(1, 4):
            quarters.append(quarters[-1] + timedelta(days=7))

        for i, (start_time) in enumerate(quarters, 1):
            end_time = start_time + timedelta(days=7)
            if start_time <= self.dt < end_time:
                return f"Q{i}", (start_time, end_time)
        
        # Handle extra period if not within any quarter
        start_time = (self.dt - timedelta(days=self.dt.weekday() + 1)).replace(hour=18, minute=0)
        days_until_friday = (4 - self.dt.weekday()) % 7
        end_time = (self.dt + timedelta(days=days_until_friday)).replace(hour=16, minute=0)
        return "Qx", (start_time, end_time)

    """
    def get_weekly_quarter(self):
        day_of_week = self.dt.weekday()
        hour = self.dt.hour

        sessions = [
            ("Q1", [6, 18, 0, 0, 18, 0]),
            ("Q2", [0, 18, 0, 1, 18, 0]),
            ("Q3", [1, 18, 0, 2, 18, 0]),
            ("Q4", [2, 18, 0, 3, 18, 0]),
            ("Qx", [3, 18, 0, 4, 16, 0]),
        ]
        for i, (session_name, quarters) in enumerate(sessions):
             start_d, start_h, start_m, end_d, end_h, end_m = quarters
             if day_of_week in [start_d, end_d]:                 
                if day_of_week == end_d and self.hour >= end_h and self.minute > end_m:           
                    start_time = self.timezone.localize(datetime(self.year, self.month, self.day, end_h, end_m))
                    end_time = self.timezone.localize(datetime(self.year, self.month, self.day+1, end_h, end_m))
                    Q=sessions[i+1][0]
                else:
                    start_time = self.timezone.localize(datetime(self.year, self.month, self.day-1, start_h, start_m))
                    end_time = self.timezone.localize(datetime(self.year, self.month, self.day, end_h, end_m))
                    Q=sessions[i][0]
    
                return f"{Q}", (start_time, end_time)
        return None
    """
    """
    def get_weekly_quarter(self):
        day_of_week = self.dt.weekday()
        hour = self.dt.hour

        #get the Sunday
        days_since_sunday = (day_of_week + 1) % 7 + 7
        previous_sunday = (self.dt - timedelta(days=days_since_sunday)).replace(hour=18, minute=0)
        print(previous_sunday)

        #get the monday
        days_since_monday = (day_of_week + 7) % 7
        previous_monday = (self.dt - timedelta(days=days_since_monday)).replace(hour=18, minute=0)
        print(previous_monday)

        #get the Tuesday
        days_since_tuesday = 2 - day_of_week
        previous_tuesday = (self.dt - timedelta(days=days_since_tuesday)).replace(hour=18, minute=0)
        print(previous_tuesday)

        #get the Wednesday
        days_since_wednesday = (2 - day_of_week + 7) % 7
        previous_wednesday = (self.dt - timedelta(days=days_since_wednesday)).replace(hour=18, minute=0)
        print(previous_wednesday)

        #get the Thursday
        days_since_thursday = (3 - day_of_week + 7) % 7
        previous_thursday = (self.dt - timedelta(days=days_since_thursday)).replace(hour=18, minute=0)
        print(previous_thursday)

        #get the friday
        days_since_friday = (4 - day_of_week + 7) % 7
        previous_friday = (self.dt - timedelta(days=days_since_friday)).replace(hour=18, minute=0)
        print(previous_friday)
        print('test')
    """

    def get_weekly_quarter(self):
        day_of_week = self.dt.weekday()
        hour = self.dt.hour

        qts = ["Q1", "Q2", "Q3", "Q4", "Qx"]

        if hour > 18:
            if day_of_week == 6:
                qt=qts[0]  
            else:              
                qt = qts[day_of_week+1]
            start_dt = self.timezone.localize(datetime(self.year, self.month, self.day, 18, 00))
            end_dt = (self.dt + timedelta(days=1)).replace(hour=18, minute=0)
        else:
            qt = qts[day_of_week]
            start_dt = (self.dt - timedelta(days=1)).replace(hour=18, minute=0)
            if day_of_week == 4:
                end_dt = self.timezone.localize(datetime(self.year, self.month, self.day, 16, 00))
            else:
                end_dt = self.timezone.localize(datetime(self.year, self.month, self.day, 18, 00))

        return f"{qt}", (start_dt, end_dt)

    def get_daily_quarter(self):
        quarters = [(18, 24), (0, 6), (6, 12), (12, 18)]
        for i, (start, end) in enumerate(quarters, 1):
            start_dt = self.timezone.localize(datetime(self.year, self.month, self.day, start, 0))
            end_dt = start_dt + timedelta(hours=6)
            if start_dt <= self.dt < end_dt:
                return f"Q{i}", (start_dt, end_dt)
        return None

    def get_90_minute_quarter(self):
        sessions = [
            ("Asia", 18, [(18, 0, 19, 30), (19, 30, 21, 0), (21, 0, 22, 30), (22, 30, 23, 59)]),
            ("London", 0, [(0, 0, 1, 30), (1, 30, 3, 0), (3, 0, 4, 30), (4, 30, 6, 0)]),
            ("New York", 6, [(6, 0, 7, 30), (7, 30, 9, 0), (9, 0, 10, 30), (10, 30, 12, 0)]),
            ("Afternoon", 12, [(12, 0, 13, 30), (13, 30, 15, 0), (15, 0, 16, 30), (16, 30, 18, 0)])
        ]
        for session_name, start_hour, quarters in sessions:
            for i, (start_h, start_m, end_h, end_m) in enumerate(quarters, 1):
                start_time = self.timezone.localize(datetime(self.year, self.month, self.day, start_h, start_m))
                end_time = self.timezone.localize(datetime(self.year, self.month, self.day, end_h, end_m))
                if start_time <= self.dt < end_time:
                    return f"{session_name} Q{i}", (start_time, end_time)
        return None

    def get_micro_quarter(self):
        start_time = self.timezone.localize(datetime(self.year, self.month, self.day, 18, 0))
        for i in range(4):
            start_delta = timedelta(minutes=22.5 * i)
            end_delta = start_delta + timedelta(minutes=22.5)
            if start_time + start_delta <= self.dt < start_time + end_delta:
                return f"Q{i + 1}", (start_time + start_delta, start_time + end_delta)
        return None

    def get_current_quarter(self):
        results = {
            "yearly": self.get_yearly_quarter(),
            "monthly": self.get_monthly_quarter(),
            "weekly": self.get_weekly_quarter(),
            "daily": self.get_daily_quarter(),
            "90_minute": self.get_90_minute_quarter(),
            "micro": self.get_micro_quarter(),
        }
        result_str = ""
        for cycle, result in results.items():
            if result:
                quarter, (start, end) = result
                result_str += f"{cycle.capitalize()}:\n"
                result_str += f"  Quarter: {quarter}\n"
                result_str += f"  Start: {self.format_datetime(start)}\n"
                result_str += f"  End: {self.format_datetime(end)}\n\n"
            else:
                result_str += f"{cycle.capitalize()}:\n"
                result_str += f"  Quarter: Not found\n"
                result_str += f"  Start: N/A\n"
                result_str += f"  End: N/A\n\n"
        return result_str

    def get_previous_yearly_quarter(self):
        previous_dt = self.dt - timedelta(weeks=13)
        prev_quarters = QuarterlyCycles(previous_dt, self.timezone.zone)
        return prev_quarters.get_yearly_quarter()

    def get_previous_monthly_quarter(self):
        previous_dt = self.dt - timedelta(days=7)
        prev_quarters = QuarterlyCycles(previous_dt, self.timezone.zone)
        return prev_quarters.get_monthly_quarter()

    def get_previous_weekly_quarter(self):
        # if Monday
        if self.dt.weekday() == 0:
            # force to time = 12:00 to prevent any timing issue
            previous_dt = (self.dt - timedelta(days=3)).replace(hour=12, minute=0, second=0)
        elif self.dt.weekday() == 6: 
            previous_dt = (self.dt - timedelta(days=2)).replace(hour=12, minute=0, second=0)
        else: 
            previous_dt = self.dt - timedelta(days=1)
        
        prev_quarters = QuarterlyCycles(previous_dt, self.timezone.zone)
        return prev_quarters.get_weekly_quarter()

    def get_previous_daily_quarter(self):
        previous_dt = self.dt - timedelta(hours=6)
        prev_quarters = QuarterlyCycles(previous_dt, self.timezone.zone)
        return prev_quarters.get_daily_quarter()

    def get_previous_90_minute_quarter(self):
        previous_dt = self.dt - timedelta(minutes=90)
        prev_quarters = QuarterlyCycles(previous_dt, self.timezone.zone)
        return prev_quarters.get_90_minute_quarter()

    def get_previous_micro_quarter(self):
        previous_dt = self.dt - timedelta(minutes=22.5)
        prev_quarters = QuarterlyCycles(previous_dt, self.timezone.zone)
        return prev_quarters.get_micro_quarter()

    def get_previous_quarter(self):
        results = {
            "yearly": self.get_previous_yearly_quarter(),
            "monthly": self.get_previous_monthly_quarter(),
            "weekly": self.get_previous_weekly_quarter(),
            "daily": self.get_previous_daily_quarter(),
            "90_minute": self.get_previous_90_minute_quarter(),
            "micro": self.get_previous_micro_quarter(),
        }
        result_str = ""
        for cycle, result in results.items():
            if result:
                quarter, (start, end) = result
                result_str += f"{cycle.capitalize()}:\n"
                result_str += f"  Quarter: {quarter}\n"
                result_str += f"  Start: {self.format_datetime(start)}\n"
                result_str += f"  End: {self.format_datetime(end)}\n\n"
            else:
                result_str += f"{cycle.capitalize()}:\n"
                result_str += f"  Quarter: Not found\n"
                result_str += f"  Start: N/A\n"
                result_str += f"  End: N/A\n\n"
        return result_str

