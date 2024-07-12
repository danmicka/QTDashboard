# Example Usage
from QuaterlyCycles import QuarterlyCycles
from datetime import datetime 

if __name__ == "__main__":

    local_timezone = 'Europe/Zurich'
    target_timezone = 'America/New_York'

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
    #qt = QuarterlyCycles(datetime(2024, 6, 9, 19, 00), timezone='America/New_York')
    # Fri 10am
    #qt = QuarterlyCycles(datetime(2024, 6, 14, 10, 00), timezone='America/New_York')
    # THu 7pm
    #qt = QuarterlyCycles(datetime(2024, 6, 13, 19, 00), timezone='America/New_York')
    # Yearly
    #qt = QuarterlyCycles(datetime(2024, 11, 15, 10, 0), local_timezone=local_timezone, target_timezone=target_timezone)
    # Monthly
    qt =  QuarterlyCycles(datetime(2024, 5, 3, 10, 0), local_timezone=local_timezone, target_timezone=target_timezone)

    """
    # Now
    dt = datetime.now()
    print (dt)
    qt = QuarterlyCycles(dt, local_timezone=local_timezone, target_timezone=target_timezone)
  
    # Print the day, hour, and minute in the target timezone
    print(f"Day: {qt.day}, Hour: {qt.hour}, Minute: {qt.minute}")

    quarter = qt.get_90_minute_quarter()
    if quarter:
        quarter_name, (start, end) = quarter
        print(f"Quarter: {quarter_name}, Start: {start}, End: {end}")
    else:
        print("No 90-minute quarter found.")
    """
    print('current quaters:')
    print(qt.get_current_quarter())
    print('previous quaters:')
    print(qt.get_previous_quarter())
    print('test:')
    #qtw = QuarterlyCycles(datetime(2024, 6, 19, 18, 30), timezone='America/New_York')
    #print(qt.get_weekly_quarter())
    #
    