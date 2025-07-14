from datetime import datetime, timedelta

def display_current_datetime():
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)
    return formatted_date 
    
def calculate_future_date(current_datetime_str):
    current_datetime = datetime.strptime(current_datetime_str, "%Y-%m-%d %H:%M:%S")
    number_of_days = int(input("Enter the number of days to add: "))
    future_date = current_datetime + timedelta(days=number_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future Date:", formatted_future_date)
    return formatted_future_date  
    
if __name__ == "__main__":
    current_datetime_str = display_current_datetime()
    calculate_future_date(current_datetime_str)
