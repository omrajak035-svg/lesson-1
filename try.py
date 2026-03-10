"""
Freemium SaaS Business Metrics Calculator
----------------------------------------
A professional command-line tool to project monthly revenue, calculate net profit,
and evaluate business health for a freemium SaaS model.
"""

def format_inr(amount: float) -> str:
    """Formats a number as Indian Rupees (INR).

    Args:
        amount: The financial amount to format.

    Returns:
        A formatted string with the ₹ symbol and proper comma placement (e.g., ₹1,50,000.00).
    """
    is_negative = amount < 0
    amount = abs(amount)
    integer_part = int(amount)
    decimal_part = f"{amount:.2f}".split(".")[1]
    
    integer_str = str(integer_part)
    if len(integer_str) > 3:
        last_three = integer_str[-3:]
        remaining = integer_str[:-3]
        
        # Group by 2s for Indian Numbering System
        groups = []
        while remaining:
            groups.append(remaining[-2:])
            remaining = remaining[:-2]
        
        groups.reverse()
        formatted_integer = ",".join(groups) + "," + last_three
    else:
        formatted_integer = integer_str
        
    result = f"₹{formatted_integer}.{decimal_part}"
    return f"-{result}" if is_negative else result

def get_numeric_input(prompt: str) -> float:
    """Prompts the user for a numeric input and robustly handles invalid entries.

    Args:
        prompt: The message to display to the user.

    Returns:
        The valid numeric value entered by the user.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            value = float(user_input)
            return value
        except ValueError:
            print("\n  [!] Error: Invalid input. Please enter a valid number (e.g., 1000).")
            print("  " + "-" * 56)

def calculate_pro_revenue(free_users: float, conversion_rate: float, pro_price: float) -> float:
    """Calculates the gross revenue from Pro subscriptions based on a conversion rate.

    Args:
        free_users: The initial number of free tier users.
        conversion_rate: The percentage of free users that convert to Pro (0-100).
        pro_price: The price of a Pro subscription.

    Returns:
        The calculated gross revenue.
    """
    pro_users = (free_users * conversion_rate) / 100.0
    return pro_users * pro_price

def calculate_net_profit(revenue: float, server_bill: float) -> float:
    """Calculates the net profit after deducting expenses.

    Args:
        revenue: The gross revenue calculated.
        server_bill: Monthly server expense.

    Returns:
        The calculated net profit.
    """
    return revenue - server_bill

def evaluate_business_health(net_profit: float) -> str:
    """Evaluates the general business health based on the monthly net profit.

    Args:
        net_profit: The calculated monthly net profit.

    Returns:
        A string message indicating the business health tier.
    """
    if net_profit > 100000:
        return "Excellent (High Profitability) - You are rich!"
    elif net_profit > 50000:
        return "Steady (Moderate Profitability) - You are middle class!"
    elif net_profit > 0:
        return "Surviving (Low Profitability) - You are surviving."
    else:
        return "Critical (Operating at a Loss) - You are poor."

def main() -> None:
    """Main execution guard that orchestrates the CLI SaaS projection tool."""
    print("=" * 60)
    print(f"{'🚀 SAAS FREEMIUM PROJECTION TOOL 🚀':^60}")
    print("=" * 60)
    print("\nPlease enter your business metrics below:\n")
    
    pro_price = 1000.0
    
    free_users = get_numeric_input("  ▶ How many free users are there? : ")
    conversion_rate = get_numeric_input("  ▶ What is the conversion percentage to Pro? (%) : ")
    server_bill = get_numeric_input("  ▶ How much is your server bill this month? (₹) : ")
    
    print("\n" + "-" * 60)
    print(f"{'📊 GENERATING FINANCIAL REPORT 📊':^60}")
    print("-" * 60 + "\n")
    
    revenue = calculate_pro_revenue(free_users, conversion_rate, pro_price)
    net_profit = calculate_net_profit(revenue, server_bill)
    health_status = evaluate_business_health(net_profit)
    
    pro_users_count = int((free_users * conversion_rate) / 100)
    
    print(f"  • Pro Subscription Price : {format_inr(pro_price)}")
    print(f"  • Projected Pro Users    : {pro_users_count}")
    print(f"  • Gross Monthly Revenue  : {format_inr(revenue)}")
    print(f"  • Monthly Server Expense : {format_inr(server_bill)}")
    print("\n" + "." * 60 + "\n")
    
    print(f"  💰 NET PROFIT           : {format_inr(net_profit)}")
    print(f"  🏥 BUSINESS HEALTH      : {health_status}")
    
    print("\n" + "=" * 60)
    print(f"{'✨ END OF REPORT ✨':^60}")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()