def calculate_stop_limit_prices(purchase_price, spread, percentage):
    """
    Calculate stop-limit prices based on the purchase price, spread, and percentage increment.

    :param purchase_price: float, the price at which the asset was purchased
    :param spread: float, the spread to be subtracted from the stop price to set the limit price
    :param percentage: float, percentage increment for calculating stop prices
    :return: tuple, containing the stop price and corresponding limit price
    """
    limit_price = purchase_price * (1+(percentage / 100))
    stop_price = limit_price + spread
    return round(stop_price, 2), round(limit_price, 2)

def main():
    purchase_price = float(input("Enter the purchase price: "))
    spread = float(input("Enter the spread: "))
    percentage = float(input("Enter the percentage increment: "))

    stop_price, limit_price = calculate_stop_limit_prices(purchase_price, spread, percentage)

    print("\nStop-Limit Prices:")
    print(f"{percentage}% Increment \n Stop Price: ${stop_price} \n Limit Price: ${limit_price}")

if __name__ == "__main__":
    main()
