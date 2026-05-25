def calculate_cost(services):
    total = 0

    for service in services:
        usage = service.usage
        price = service.price
        total += usage * price

    return round(total, 2)