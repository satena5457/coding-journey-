def apply_discount(price, discount):
    """
    Calculates the discounted price.
    
    Args:
        price (int/float): Original price
        discount (int/float): Discount percentage (0-100)
    
    Returns:
        float: Discounted price, or error message string
    """
    # Validate price
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    
    # Validate discount
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
    
    # Validate price range
    if price <= 0:
        return "The price should be greater than 0"
    
    # Validate discount range
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    
    # Calculate and return discounted price
    discounted_price = price - (price * discount / 100)
    return discounted_price
