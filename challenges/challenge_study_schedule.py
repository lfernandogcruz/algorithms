def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    users = 0
    for login, logout in permanence_period:
        if type(login) is not int or type(logout) is not int:
            return None

        if login <= target_time <= logout:
            users += 1

    return users
