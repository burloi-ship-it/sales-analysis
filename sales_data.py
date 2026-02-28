# sales_data.py

sales_data = [230, 200, 310, 290, 400, 150, 180]
print(f"Sales data for week: {sales_data}.)

def total_sales(data):
    total = 0
    for i in data:
        total += i
    return total
    
def average_sales(data):
    average = sum(data) / len(data)
    return average
    
result_total_sales = total_sales(sales_data)
print(f"Total sales is: {result_total_sales}."}

result_average_sales = average_sales(sales_data)
print(f"Average sales is: {result_total_sales}.")
