import unittest
from datetime import datetime
import pytz
from QuaterlyCycles import QuarterlyCycles  # assuming the class is saved in quarterly_cycles.py

class TestQuarterlyCycles(unittest.TestCase):
    
    def setUp(self):
        self.local_timezone = 'Europe/Zurich'
        self.target_timezone = 'America/New_York'
        self.tz = pytz.timezone(self.target_timezone)

    # Test Weekly Quarters
    def test_weekly_quarter_q1(self):
        # Sunday 7pm (Q1)
        dt = self.tz.localize(datetime(2024, 6, 9, 19, 0))
        qt = QuarterlyCycles(dt, local_timezone=self.local_timezone, target_timezone=self.target_timezone)
        quarter, (start, end) = qt.get_weekly_quarter()
        self.assertEqual(quarter, "Q1")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 9, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 10, 18, 0)))
    
    def test_weekly_quarter_q2(self):
        # Monday 7pm (Q2)
        dt = self.tz.localize(datetime(2024, 6, 10, 19, 0))
        qt = QuarterlyCycles(dt, local_timezone=self.local_timezone, target_timezone=self.target_timezone)
        quarter, (start, end) = qt.get_weekly_quarter()
        self.assertEqual(quarter, "Q2")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 10, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 11, 18, 0)))
    
    def test_weekly_quarter_q3(self):
        # Tuesday 7pm (Q3)
        dt = self.tz.localize(datetime(2024, 6, 11, 19, 0))
        qt = QuarterlyCycles(dt, local_timezone=self.local_timezone, target_timezone=self.target_timezone)
        quarter, (start, end) = qt.get_weekly_quarter()
        self.assertEqual(quarter, "Q3")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 11, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 12, 18, 0)))
    
    def test_weekly_quarter_q4(self):
        # Wednesday 7pm (Q4)
        dt = self.tz.localize(datetime(2024, 6, 12, 19, 0))
        qt = QuarterlyCycles(dt, local_timezone=self.local_timezone, target_timezone=self.target_timezone)
        quarter, (start, end) = qt.get_weekly_quarter()
        self.assertEqual(quarter, "Q4")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 12, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 13, 18, 0)))
    
    def test_weekly_quarter_qx(self):
        # Thursday 7pm (Qx)
        dt = self.tz.localize(datetime(2024, 6, 13, 19, 0))
        qt = QuarterlyCycles(dt, local_timezone=self.local_timezone, target_timezone=self.target_timezone)
        quarter, (start, end) = qt.get_weekly_quarter()
        self.assertEqual(quarter, "Qx")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 13, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 14, 16, 0)))

    def test_weekly_quarter_friday(self):
        # Friday 10am (Outside defined quarters)
        dt = self.tz.localize(datetime(2024, 6, 14, 10, 0))
        qt = QuarterlyCycles(dt, local_timezone=self.local_timezone, target_timezone=self.target_timezone)
        quarter, (start, end) = qt.get_weekly_quarter()
        self.assertEqual(quarter, "Qx")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 13, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 14, 16, 0)))

    # Test Previous weekly quarter
    def test_weekly_previous_quarter_q1(self):
        # Sunday 7pm (Q1)
        dt = self.tz.localize(datetime(2024, 6, 9, 19, 0))
        qt = QuarterlyCycles(dt, local_timezone=self.local_timezone, target_timezone=self.target_timezone)
        quarter, (start, end) = qt.get_previous_weekly_quarter()
        self.assertEqual(quarter, "Qx")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 6, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 7, 16, 0)))
    
    def test_weekly_previous_quarter_q2(self):
        # Monday 7pm (Q2)
        dt = self.tz.localize(datetime(2024, 6, 10, 19, 0))
        qt = QuarterlyCycles(dt, local_timezone=self.local_timezone, target_timezone=self.target_timezone)
        quarter, (start, end) = qt.get_previous_weekly_quarter()
        self.assertEqual(quarter, "Q1")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 9, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 10, 18, 0)))

    def test_weekly_previous_quarter_qx(self):
        # Fri 10 am (Qx)
        dt = self.tz.localize(datetime(2024, 6, 7, 10, 0))
        qt = QuarterlyCycles(dt, local_timezone=self.local_timezone, target_timezone=self.target_timezone)
        quarter, (start, end) = qt.get_previous_weekly_quarter()
        self.assertEqual(quarter, "Q4")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 5, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 6, 18, 0)))
    
    def test_weekly_previous_quarter_q3(self):
        # Wed 10 am (Q3)
        dt = self.tz.localize(datetime(2024, 6, 12, 10, 0))
        qt = QuarterlyCycles(dt, local_timezone=self.local_timezone, target_timezone=self.target_timezone)
        quarter, (start, end) = qt.get_previous_weekly_quarter()
        self.assertEqual(quarter, "Q2")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 10, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 11, 18, 0)))

    # Test daily quarter
    def test_daily_quarter_q1(self):
        dt = self.tz.localize(datetime(2024, 7, 9, 19, 0))
        qt = QuarterlyCycles(dt, local_timezone=self.local_timezone, target_timezone=self.target_timezone)
        quarter, (start, end) = qt.get_daily_quarter()
        self.assertEqual(quarter, "Q1")
        self.assertEqual(start, self.tz.localize(datetime(2024, 7, 9, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 7, 10, 0, 0)))

    def test_daily_quarter_q2(self):
        dt = self.tz.localize(datetime(2024, 7, 10, 5, 0))
        qt = QuarterlyCycles(dt, local_timezone=self.local_timezone, target_timezone=self.target_timezone)
        quarter, (start, end) = qt.get_daily_quarter()
        self.assertEqual(quarter, "Q2")
        self.assertEqual(start, self.tz.localize(datetime(2024, 7, 10, 0, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 7, 10, 6, 0)))

    def test_daily_quarter_q3(self):
        dt = self.tz.localize(datetime(2024, 7, 10, 8, 0))
        qt = QuarterlyCycles(dt, local_timezone=self.local_timezone, target_timezone=self.target_timezone)
        quarter, (start, end) = qt.get_daily_quarter()
        self.assertEqual(quarter, "Q3")
        self.assertEqual(start, self.tz.localize(datetime(2024, 7, 10, 6, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 7, 10, 12, 0)))

    def test_daily_quarter_q4(self):
        dt = self.tz.localize(datetime(2024, 7, 10, 15, 0))
        qt = QuarterlyCycles(dt, local_timezone=self.local_timezone, target_timezone=self.target_timezone)
        quarter, (start, end) = qt.get_daily_quarter()
        self.assertEqual(quarter, "Q4")
        self.assertEqual(start, self.tz.localize(datetime(2024, 7, 10, 12, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 7, 10, 18, 0)))

    # Test 90m quarter
    def test_90_minute_quarter_asia(self):
        # Test each quarter in the Asia session
        quarters = [
            (datetime(2024, 6, 9, 18, 0), "Asia Q1", datetime(2024, 6, 9, 19, 30)),
            (datetime(2024, 6, 9, 19, 30), "Asia Q2", datetime(2024, 6, 9, 21, 0)),
            (datetime(2024, 6, 9, 21, 0), "Asia Q3", datetime(2024, 6, 9, 22, 30)),
            (datetime(2024, 6, 9, 22, 30), "Asia Q4", datetime(2024, 6, 9, 23, 59)),
        ]
        for start, expected_quarter, end in quarters:
            dt = self.tz.localize(start)
            qt = QuarterlyCycles(dt, local_timezone=self.local_timezone, target_timezone=self.target_timezone)
            quarter, (start_time, end_time) = qt.get_90_minute_quarter()
            self.assertEqual(quarter, expected_quarter)
            self.assertEqual(start_time, self.tz.localize(start))
            self.assertEqual(end_time, self.tz.localize(end))

    def test_90_minute_quarter_london(self):
        # Test each quarter in the London session
        quarters = [
            (datetime(2024, 6, 9, 0, 0), "London Q1", datetime(2024, 6, 9, 1, 30)),
            (datetime(2024, 6, 9, 1, 30), "London Q2", datetime(2024, 6, 9, 3, 0)),
            (datetime(2024, 6, 9, 3, 0), "London Q3", datetime(2024, 6, 9, 4, 30)),
            (datetime(2024, 6, 9, 4, 30), "London Q4", datetime(2024, 6, 9, 6, 0)),
        ]
        for start, expected_quarter, end in quarters:
            dt = self.tz.localize(start)
            qt = QuarterlyCycles(dt, local_timezone=self.local_timezone, target_timezone=self.target_timezone)
            quarter, (start_time, end_time) = qt.get_90_minute_quarter()
            self.assertEqual(quarter, expected_quarter)
            self.assertEqual(start_time, self.tz.localize(start))
            self.assertEqual(end_time, self.tz.localize(end))

    def test_90_minute_quarter_new_york(self):
        # Test each quarter in the New York session
        quarters = [
            (datetime(2024, 6, 9, 6, 0), "New York Q1", datetime(2024, 6, 9, 7, 30)),
            (datetime(2024, 6, 9, 7, 30), "New York Q2", datetime(2024, 6, 9, 9, 0)),
            (datetime(2024, 6, 9, 9, 0), "New York Q3", datetime(2024, 6, 9, 10, 30)),
            (datetime(2024, 6, 9, 10, 30), "New York Q4", datetime(2024, 6, 9, 12, 0)),
        ]
        for start, expected_quarter, end in quarters:
            dt = self.tz.localize(start)
            qt = QuarterlyCycles(dt, local_timezone=self.local_timezone, target_timezone=self.target_timezone)
            quarter, (start_time, end_time) = qt.get_90_minute_quarter()
            self.assertEqual(quarter, expected_quarter)
            self.assertEqual(start_time, self.tz.localize(start))
            self.assertEqual(end_time, self.tz.localize(end))

    def test_90_minute_quarter_afternoon(self):
        # Test each quarter in the Afternoon session
        quarters = [
            (datetime(2024, 6, 9, 12, 0), "Afternoon Q1", datetime(2024, 6, 9, 13, 30)),
            (datetime(2024, 6, 9, 13, 30), "Afternoon Q2", datetime(2024, 6, 9, 15, 0)),
            (datetime(2024, 6, 9, 15, 0), "Afternoon Q3", datetime(2024, 6, 9, 16, 30)),
            (datetime(2024, 6, 9, 16, 30), "Afternoon Q4", datetime(2024, 6, 9, 18, 0)),
        ]
        for start, expected_quarter, end in quarters:
            dt = self.tz.localize(start)
            qt = QuarterlyCycles(dt, local_timezone=self.local_timezone, target_timezone=self.target_timezone)
            quarter, (start_time, end_time) = qt.get_90_minute_quarter()
            self.assertEqual(quarter, expected_quarter)
            self.assertEqual(start_time, self.tz.localize(start))
            self.assertEqual(end_time, self.tz.localize(end))


if __name__ == '__main__':
    unittest.main()
