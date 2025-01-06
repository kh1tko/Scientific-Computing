def add_time(start, duration, starting_day=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Split start time for hours, minutes and AM/PM
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Translation start time  on 24-hour format
    if period == "PM":
        start_hour += 12

    # Divide the time period into hours and minutes
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Add the time period to the initial one
    total_minutes = start_minute + duration_minute
    total_hours = start_hour + duration_hour + (total_minutes // 60)
    total_minutes %= 60

    # Calculate the total number of days
    total_days = total_hours // 24
    end_hour = total_hours % 24

    # Convert the result to a 12-hour format
    end_period = "AM" if end_hour < 12 else "PM"
    end_hour = end_hour % 12
    end_hour = 12 if end_hour == 0 else end_hour

    # Shaping the result
    new_time = f"{end_hour}:{total_minutes:02} {end_period}"

    # Add the day of the week if it is specified
    if starting_day:
        starting_day_index = days_of_week.index(starting_day.capitalize())
        end_day_index = (starting_day_index + total_days) % 7
        new_day = days_of_week[end_day_index]
        new_time += f", {new_day}"

    # Add information about the number of days
    if total_days == 1:
        new_time += " (next day)"
    elif total_days > 1:
        new_time += f" ({total_days} days later)"

    return new_time