# Example Usage
from QuaterlyCycles import QuarterlyCycles
from datetime import datetime 

if __name__ == "__main__":
    #qt = QuarterlyCycles(datetime(2024, 6, 6, 10, 30), timezone='America/New_York')
    qt = QuarterlyCycles(datetime(2024, 6, 20, 10, 30), timezone='America/New_York')
    print(qt.get_current_quarter())