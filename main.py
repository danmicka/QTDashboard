# Example Usage
from QuaterlyCycles import QuarterlyCycles
from datetime import datetime 

if __name__ == "__main__":
    #qt = QuarterlyCycles(datetime(2024, 6, 6, 10, 30), timezone='America/New_York')
    #qt = QuarterlyCycles(datetime(2024, 6, 20, 10, 30), timezone='America/New_York')
    #qt = QuarterlyCycles(datetime(2024, 6, 24, 6, 00), timezone='America/New_York')
    #qt = QuarterlyCycles(datetime(2024, 6, 9, 19, 00), timezone='America/New_York')
    #qt = QuarterlyCycles(datetime(2024, 6, 10, 19, 00), timezone='America/New_York')
    # tues 5am
    #qt = QuarterlyCycles(datetime(2024, 6, 11, 5, 00), timezone='America/New_York')
    # tues 5am
    #qt = QuarterlyCycles(datetime(2024, 6, 11, 19, 00), timezone='America/New_York')
    # fri 5am
    #qt = QuarterlyCycles(datetime(2024, 6, 14, 5, 00), timezone='America/New_York')
    # sun 7pm
    #qt = QuarterlyCycles(datetime(2024, 6, 9, 19, 00), timezone='America/New_York')
    # mon 7pm
    #qt = QuarterlyCycles(datetime(2024, 6, 10, 19, 00), timezone='America/New_York')
    # Sun 7pm
    #qt = QuarterlyCycles(datetime(2024, 7, 1, 19, 00), timezone='America/New_York')
    qt = QuarterlyCycles(datetime(2024, 6, 9, 19, 00), timezone='America/New_York')

    print('current quaters:')
    print(qt.get_current_quarter())
    print('previous quaters:')
    print(qt.get_previous_quarter())
    print('test:')
    #qtw = QuarterlyCycles(datetime(2024, 6, 19, 18, 30), timezone='America/New_York')
    #print(qt.get_weekly_quarter())