def send_alert(total_cost):
    threshold = 10

    if total_cost > threshold:
        print(f"Alert: Total cost exceeding over ${total_cost} ")
    else:
        print(f"Total cost of ${total_cost} is within the threshold.")