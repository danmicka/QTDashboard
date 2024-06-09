# Example Usage
from QuaterlyCycles import QuarterlyCycles
from datetime import datetime 

if __name__ == "__main__":
    qt = QuarterlyCycles(datetime(2024, 6, 9, 10, 30))
    print(qt.get_current_quarter())