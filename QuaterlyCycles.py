from datetime import datetime, timedelta
import pytz

class QuarterlyCycles:
    def __init__(self, dt: datetime, timezone: str = 'UTC'):
        self.timezone = pytz.timezone(timezone)
        self.dt = self.timezone.localize(dt)
        self.year = self.dt.year
        self.month = self.dt.month
        self.day = self.dt.day
        self.hour = self.dt.hour
        self.minute = self.dt.minute

    def format_datetime(self, dt: datetime):
        return dt.strftime("%d/%m/%Y %H:%M")

    def get_first_full_week_start(self):
        first_day_of_month = datetime(self.year, self.month, 1)
        first_day_of_month = self.timezone.localize(first_day_of_month)
        first_sunday_6pm = first_day_of_month + timedelta(days=(6 - first_day_of_month.weekday() + 1) % 7, hours=18 - first_day_of_month.hour)
        if first_sunday_6pm.day > 1:
            first_sunday_6pm = first_sunday_6pm + timedelta(days=7)
        return first_sunday_6pm

    def first_monday_of_month(self):
        first_day = datetime(self.year, self.month, 1)
        first_monday = first_day + timedelta(days=(7 - first_day.weekday()) % 7)
        return first_monday

    def get_yearly_quarter(self):
        quarters = [(1, 3), (4, 6), (7, 9), (10, 12)]
        for i, (start, end) in enumerate(quarters, 1):
            if start <= self.month <= end:
                start_dt = self.timezone.localize(datetime(self.year, start, 1))
                end_dt = self.timezone.localize(datetime(self.year, end, 1) + timedelta(days=-1))
                return f"Q{i}", (start_dt, end_dt)
        return None

    def get_monthly_quarter_old(self):
        first_week_start = self.get_first_full_week_start()
        q1_start = first_week_start
        q1_end = q1_start + timedelta(days=7)
        q2_start = q1_end
        q2_end = q2_start + timedelta(days=7)
        q3_start = q2_end
        q3_end = q3_start + timedelta(days=7)
        q4_start = q3_end
        q4_end = q4_start + timedelta(days=7)

        if q1_start <= self.dt < q1_end:
            return "Q1", (q1_start, q1_end)
        elif q2_start <= self.dt < q2_end:
            return "Q2", (q2_start, q2_end)
        elif q3_start <= self.dt < q3_end:
            return "Q3", (q3_start, q3_end)
        elif q4_start <= self.dt < q4_end:
            return "Q4", (q4_start, q4_end)
        elif self.dt.weekday() == 4 and self.hour >= 18:
            friday_start = self.timezone.localize(datetime(self.year, self.month, self.day, 18, 0))
            friday_end = friday_start + timedelta(days=2, hours=18)
            return "Qx", (friday_start, friday_end)
        return None

    def get_monthly_quarter(self):
        first_monday = self.first_monday_of_month()
        
        q1_start = self.timezone.localize(first_monday - timedelta(days=1) + timedelta(hours=18))

        q1_end = q1_start + timedelta(days=7)
        q2_start = q1_end
        q2_end = q2_start + timedelta(days=7)
        q3_start = q2_end
        q3_end = q3_start + timedelta(days=7)
        q4_start = q3_end
        q4_end = q4_start + timedelta(days=7)

        if q1_start <= self.dt < q1_end:
            current_quarter = 'Q1'
            start_datetime = q1_start
            end_datetime = q1_end
        elif q2_start <= self.dt < q2_end:
            current_quarter = 'Q2'
            start_datetime = q2_start
            end_datetime = q2_end
        elif q3_start <= self.dt < q3_end:
            current_quarter = 'Q3'
            start_datetime = q3_start
            end_datetime = q3_end
        else:
            current_quarter = 'Q4'
            start_datetime = q4_start
            end_datetime = q4_end

        return current_quarter, (start_datetime, end_datetime)

    def get_weekly_quarter(self):
        quarters = {
            "Q1": (0, 0),
            "Q2": (1, 1),
            "Q3": (2, 2),
            "Q4": (3, 3),
        }
        day_of_week = self.dt.weekday()
        for q, (start, end) in quarters.items():
            if start <= day_of_week <= end:
                start_dt = self.dt - timedelta(days=(day_of_week - start))
                end_dt = start_dt + timedelta(days=1)
                return q, (start_dt, end_dt)
        return None

    def get_daily_quarter(self):
        quarters = [(18, 0), (0, 6), (6, 12), (12, 18)]
        for i, (start, end) in enumerate(quarters, 1):
            if start <= self.hour < end or (start == 18 and self.hour < end):
                start_dt = self.timezone.localize(datetime(self.year, self.month, self.day, start, 0))
                end_dt = start_dt + timedelta(hours=6)
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
        quarters = [timedelta(minutes=22.5*i) for i in range(4)]
        for i, start_delta in enumerate(quarters, 1):
            end_delta = start_delta + timedelta(minutes=22.5)
            if start_time + start_delta <= self.dt < start_time + end_delta:
                return f"Q{i}", (start_time + start_delta, start_time + end_delta)
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

# Example Usage
#qt = QuarterlyTheory(datetime(2024, 6, 9, 10, 30), timezone='America/New_York')
#print(qt.get_current_quarter())
