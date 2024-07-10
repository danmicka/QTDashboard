import unittest
from datetime import datetime
import pytz
from QuaterlyCycles import QuarterlyCycles  # assuming the class is saved in quarterly_cycles.py

class TestQuarterlyCycles(unittest.TestCase):
    
    def setUp(self):
        self.timezone = 'America/New_York'
        self.tz = pytz.timezone(self.timezone)

    # Test Weekly Quarters
    def test_weekly_quarter_q1(self):
        # Sunday 7pm (Q1)
        dt = self.tz.localize(datetime(2024, 6, 9, 19, 0))
        qt = QuarterlyCycles(dt, timezone=self.timezone)
        quarter, (start, end) = qt.get_weekly_quarter()
        self.assertEqual(quarter, "Q1")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 9, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 10, 18, 0)))
    
    def test_weekly_quarter_q2(self):
        # Monday 7pm (Q2)
        dt = self.tz.localize(datetime(2024, 6, 10, 19, 0))
        qt = QuarterlyCycles(dt, timezone=self.timezone)
        quarter, (start, end) = qt.get_weekly_quarter()
        self.assertEqual(quarter, "Q2")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 10, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 11, 18, 0)))
    
    def test_weekly_quarter_q3(self):
        # Tuesday 7pm (Q3)
        dt = self.tz.localize(datetime(2024, 6, 11, 19, 0))
        qt = QuarterlyCycles(dt, timezone=self.timezone)
        quarter, (start, end) = qt.get_weekly_quarter()
        self.assertEqual(quarter, "Q3")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 11, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 12, 18, 0)))
    
    def test_weekly_quarter_q4(self):
        # Wednesday 7pm (Q4)
        dt = self.tz.localize(datetime(2024, 6, 12, 19, 0))
        qt = QuarterlyCycles(dt, timezone=self.timezone)
        quarter, (start, end) = qt.get_weekly_quarter()
        self.assertEqual(quarter, "Q4")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 12, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 13, 18, 0)))
    
    def test_weekly_quarter_qx(self):
        # Thursday 7pm (Qx)
        dt = self.tz.localize(datetime(2024, 6, 13, 19, 0))
        qt = QuarterlyCycles(dt, timezone=self.timezone)
        quarter, (start, end) = qt.get_weekly_quarter()
        self.assertEqual(quarter, "Qx")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 13, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 14, 16, 0)))

    def test_weekly_quarter_friday(self):
        # Friday 10am (Outside defined quarters)
        dt = self.tz.localize(datetime(2024, 6, 14, 10, 0))
        qt = QuarterlyCycles(dt, timezone=self.timezone)
        quarter, (start, end) = qt.get_weekly_quarter()
        self.assertEqual(quarter, "Qx")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 13, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 14, 16, 0)))

    # Test Previous weekly quarter
    def test_weekly_previous_quarter_q1(self):
        # Sunday 7pm (Q1)
        dt = self.tz.localize(datetime(2024, 6, 9, 19, 0))
        qt = QuarterlyCycles(dt, timezone=self.timezone)
        quarter, (start, end) = qt.get_previous_weekly_quarter()
        self.assertEqual(quarter, "Qx")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 6, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 7, 16, 0)))
    
    def test_weekly_previous_quarter_q2(self):
        # Monday 7pm (Q2)
        dt = self.tz.localize(datetime(2024, 6, 10, 19, 0))
        qt = QuarterlyCycles(dt, timezone=self.timezone)
        quarter, (start, end) = qt.get_previous_weekly_quarter()
        self.assertEqual(quarter, "Q1")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 9, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 10, 18, 0)))

    def test_weekly_previous_quarter_qx(self):
        # Fri 10 am (Qx)
        dt = self.tz.localize(datetime(2024, 6, 7, 10, 0))
        qt = QuarterlyCycles(dt, timezone=self.timezone)
        quarter, (start, end) = qt.get_previous_weekly_quarter()
        self.assertEqual(quarter, "Q4")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 5, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 6, 18, 0)))
    
    def test_weekly_previous_quarter_q3(self):
        # Wed 10 am (Q3)
        dt = self.tz.localize(datetime(2024, 6, 12, 10, 0))
        qt = QuarterlyCycles(dt, timezone=self.timezone)
        quarter, (start, end) = qt.get_previous_weekly_quarter()
        self.assertEqual(quarter, "Q2")
        self.assertEqual(start, self.tz.localize(datetime(2024, 6, 10, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 6, 11, 18, 0)))

    # Test daily quarter
    def test_daily_quarter_q1(self):
        dt = self.tz.localize(datetime(2024, 7, 9, 19, 0))
        qt = QuarterlyCycles(dt, timezone=self.timezone)
        quarter, (start, end) = qt.get_daily_quarter()
        self.assertEqual(quarter, "Q1")
        self.assertEqual(start, self.tz.localize(datetime(2024, 7, 9, 18, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 7, 10, 0, 0)))

    def test_daily_quarter_q2(self):
        dt = self.tz.localize(datetime(2024, 7, 10, 5, 0))
        qt = QuarterlyCycles(dt, timezone=self.timezone)
        quarter, (start, end) = qt.get_daily_quarter()
        self.assertEqual(quarter, "Q2")
        self.assertEqual(start, self.tz.localize(datetime(2024, 7, 10, 0, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 7, 10, 6, 0)))

    def test_daily_quarter_q3(self):
        dt = self.tz.localize(datetime(2024, 7, 10, 8, 0))
        qt = QuarterlyCycles(dt, timezone=self.timezone)
        quarter, (start, end) = qt.get_daily_quarter()
        self.assertEqual(quarter, "Q3")
        self.assertEqual(start, self.tz.localize(datetime(2024, 7, 10, 6, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 7, 10, 12, 0)))

    def test_daily_quarter_q4(self):
        dt = self.tz.localize(datetime(2024, 7, 10, 15, 0))
        qt = QuarterlyCycles(dt, timezone=self.timezone)
        quarter, (start, end) = qt.get_daily_quarter()
        self.assertEqual(quarter, "Q4")
        self.assertEqual(start, self.tz.localize(datetime(2024, 7, 10, 12, 0)))
        self.assertEqual(end, self.tz.localize(datetime(2024, 7, 10, 18, 0)))

if __name__ == '__main__':
    unittest.main()
