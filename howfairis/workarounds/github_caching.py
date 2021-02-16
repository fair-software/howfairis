from datetime import datetime
from datetime import timedelta
import requests
from dateutil import tz


def github_caching_check(checker):
    try:
        response = requests.get(checker.repo.api)
        date_created_string = response.json().get("created_at")
        date_created_utc = datetime.strptime(date_created_string, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=tz.tzutc())
        date_created_local = date_created_utc.astimezone(tz.tzlocal())
        date_now_local = datetime.now().astimezone(tz.tzlocal())
        time_delta = date_now_local - date_created_local
        if time_delta < timedelta(minutes=5):
            print(f"Warning: Your {checker.readme.filename} was updated " +
                  "less than 5 minutes ago. The effects of this update " +
                  "are not visible yet in the calculated compliance.")
        return
    except TypeError:
        return
