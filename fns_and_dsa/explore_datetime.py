from datetime import datetime, timedelta

def display_current_datetime():
    current_datetime = datetime.now()
    print("Current Date and Time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
    return current_datetime
    
def calculate_future_date(current_datetime):
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_datetime + timedelta(days=number_of_days)
    print("Future Date:", future_date.strftime("%Y-%m-%d"))
    
if __name__ == "__main__":
    current_datetime = display_current_datetime()
    calculate_future_date(current_datetime)