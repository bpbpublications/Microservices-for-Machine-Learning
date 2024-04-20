
if user_activity_today > avg_user_activity * 1.5:
    alert("Spike in user activity!")
elif user_activity_today < avg_user_activity * 0.5:
    alert("Drop in user activity!")
