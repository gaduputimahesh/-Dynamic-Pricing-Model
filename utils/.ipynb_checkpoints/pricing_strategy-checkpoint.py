def calculate_reward(sales, price, competitor_price):
    # Reward based on profit
    profit_margin = sales * (price - competitor_price)
    return profit_margin

def adjust_price(current_price, competitor_price, demand_factor):
    
    if demand_factor > 1:
        return current_price * 1.05
    else:
        return current_price * 0.95
