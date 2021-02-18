from datetime import datetime
from datetime import timedelta
from datetime import timezone
import requests


def github_caching_check(checker):
    try:
        critical_time = datetime.now(timezone.utc) - timedelta(minutes=5)
        response = requests.get(f"{checker.repo.api}/commits",
                                params={
                                    "page": 0,
                                    "per_page": 1,
                                    "path": checker.readme.filename,
                                    "since": critical_time.strftime("%Y-%m-%dT%H:%M:%SZ")
                                })
        if len(response.json()) > 0:
            print(f"Warning: Your {checker.readme.filename} was updated " +
                  "less than 5 minutes ago. The effects of this update " +
                  "are not visible yet in the calculated compliance.")
        return
    except ValueError:
        return
