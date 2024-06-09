from datetime import datetime, timedelta

class QuarterlyCycles:
    def __init__(self, dt: datetime):
        self.dt = dt
        self.year = dt.year
        self.month = dt.month
        self.day = dt.day
        self.hour = dt.hour
        self.minute = dt.minute

    def format_datetime(self, dt: datetime):
        return dt.strftime("%d/%m/%Y %H:%M")

    def get_yearly_quarter(self):
        quarters = [(1, 3), (4, 6), (7, 9), (10, 12)]
        for i, (start, end) in enumerate(quarters, 1):
            if start <= self.month <= end:
                start_dt = datetime(self.year, start, 1)
                end_dt = datetime(self.year, end, 1) + timedelta(days=-1)
                return f"Q{i}", (start_dt, end_dt)
        return None

    def get_monthly_quarter(self):
        first_monday = self.dt - timedelta(days=self.dt.weekday())
        q1_start = first_monday
        q1_end = first_monday + timedelta(weeks=1)
        q2_start = q1_end
        q2_end = q2_start + timedelta(weeks=1)
        q3_start = q2_end
        q3_end = q3_start + timedelta(weeks=1)
        q4_start = q3_end
        q4_end = q4_start + timedelta(weeks=1)

        if q1_start <= self.dt < q1_end:
            return "Q1", (q1_start, q1_end)
        elif q2_start <= self.dt < q2_end:
            return "Q2", (q2_start, q2_end)
        elif q3_start <= self.dt < q3_end:
            return "Q3", (q3_start, q3_end)
        elif q4_start <= self.dt < q4_end:
            return "Q4", (q4_start, q4_end)
        return None

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
                start_dt = datetime(self.year, self.month, self.day, start, 0)
                end_dt = start_dt + timedelta(hours=6)
                return f"Q{i}", (start_dt, end_dt)
        return None

    def get_90_minute_quarter(self):
        start_time = datetime(self.year, self.month, self.day, 18, 0)
        quarters = [timedelta(minutes=90*i) for i in range(4)]
        for i, start_delta in enumerate(quarters, 1):
            end_delta = start_delta + timedelta(minutes=90)
            if start_time + start_delta <= self.dt < start_time + end_delta:
                return f"Q{i}", (start_time + start_delta, start_time + end_delta)
        return None

    def get_micro_quarter(self):
        start_time = datetime(self.year, self.month, self.day, 18, 0)
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
qt = QuarterlyCycles(datetime(2024, 6, 9, 10, 30))
print(qt.get_current_quarter())

#qt = QuarterlyCycles(datetime(2024, 6, 9, 10, 30))
#print(qt.get_current_quarter())