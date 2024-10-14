import json
from typing import List, Tuple
from collections import defaultdict
from datetime import datetime

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    date_user_activity = defaultdict(lambda: defaultdict(int))

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            date_str = tweet['date'].split("T")[0]  # Extract the date part
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
            user = tweet['user']['username']
            
            date_user_activity[date_obj][user] += 1

    top_10_dates = sorted(date_user_activity.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]
    result = [(date, max(users.items(), key=lambda u: u[1])[0]) for date, users in top_10_dates]

    return result


