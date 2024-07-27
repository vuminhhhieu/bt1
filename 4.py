from datetime import datetime

class DateHandler:
   
    def format_date(date):
        
        return date.strftime("%d/%m/%Y")
    
    
    def get_days_between(date1, date2):
        
        delta = abs((date2 - date1).days)
        return delta


date1 = datetime(2024, 7, 27)
date2 = datetime(2024, 8, 15)
    
print("Formatted Date1:", DateHandler.format_date(date1))  
print("Formatted Date2:", DateHandler.format_date(date2))  
print("Days between Date1 and Date2:", DateHandler.get_days_between(date1, date2))  