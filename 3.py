from datetime import datetime

class CustomDate:
    def __init__(self):
        self.current_datetime = datetime.now()
    
    def get_date(self):
        return self.current_datetime.strftime("%d-%m-%Y")
    
    def get_time(self):
        return self.current_datetime.strftime("%H:%M:%S")


current_datetime = CustomDate()
    
print("Date:", current_datetime.get_date())  
print("Time:", current_datetime.get_time())  