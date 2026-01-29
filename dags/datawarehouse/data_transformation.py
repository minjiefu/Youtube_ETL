from datetime import timedelta, datetime


def parse_duration(duration_str):

    duration_str = duration_str.replace("P", "").replace("T", "")

    components = ["D", "H", "M", "S"]
    values = {"D": 0, "H": 0, "M": 0, "S": 0}

    for component in components:
        if component in duration_str:
            value, duration_str = duration_str.split(component)
            values[component] = int(value)

    total_duration = timedelta(
        days=values["D"], hours=values["H"], minutes=values["M"], seconds=values["S"]
    )

    return total_duration


def transform_data(row):

    duration_td = parse_duration(row["Duration"])
    # eg: PT5M33S --> timedelta(minutes=5, seconds=33)

    row["Duration"] = (datetime.min + duration_td).time()
    # eg: timedelta(minutes=5, seconds=33) --> 00:05:33
    # .time() is used to extract time part from datetime object
    # datetime.min is 0001-01-01 00:00:00

    row["Video_Type"] = "Shorts" if duration_td.total_seconds() <= 60 else "Normal"
    # .total_seconds() is methods of timedelta object to get total seconds
    return row