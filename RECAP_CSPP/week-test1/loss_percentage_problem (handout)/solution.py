cost_price = float(input())
selling_price = float(input())
def calculate_loss_per(cost_price, selling_price):
    if selling_price >= cost_price:
        return 0.0
    Loss_percent = ((cost_price - selling_price)/cost_price) * 100
    return round(Loss_percent,2)
    if Loss_percent == 0:
        return 0.0
    
print(calculate_loss_per(cost_price, selling_price))