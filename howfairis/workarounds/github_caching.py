from datetime import datetime
from datetime import timedelta
import requests
from dateutil import tz


def github_caching_check(checker):
    try:
        date_critical_utc = datetime.now().replace(second=0).astimezone(tz.tzutc()) - timedelta(minutes=5)
        date_critical_utc_string = date_critical_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
        response = requests.get(f"{checker.repo.api}/commits?page=0&per_page=1&" +
                                "path={checker.readme.filename}&since=" + date_critical_utc_string)
        if len(response.json()) > 0:
            print(f"Warning: Your {checker.readme.filename} was updated " +
                  "less than 5 minutes ago. The effects of this update " +
                  "are not visible yet in the calculated compliance.")
        return
    except ValueError:
        return
