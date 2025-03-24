import urllib.request
import json
import datetime
import argparse
from urllib.error import HTTPError, URLError

def get_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        response = urllib.request.urlopen(url)
        data = json.load(response)
    except HTTPError as e:
        print(f"There has been an HTTP error {e.code} - {e.reason}")
    except URLError as e:
        print(f"There has been an URL error {e.reason}")
    except Exception as e:
        print(f"An error has occured {str(e)}")
    today = datetime.datetime.now(datetime.timezone.utc).date()
    start_of_week = today - datetime.timedelta(days=today.weekday())
    commits = 0
    creates = 0
    for push in data:
        event_date = datetime.datetime.strptime(push["created_at"], "%Y-%m-%dT%H:%M:%SZ").date()
        if push["type"] == "PushEvent":
            if start_of_week <= event_date <= today:
                commits +=1
        elif push["type"] == "CreateEvent":
            if start_of_week <= event_date <= today:
                creates +=1 
    commits_word = "commit" if commits == 1 else "commits"
    creates_word = "repo" if creates == 1 else "repos"
    print(f"There {'is' if commits == 1 else 'are'} {commits} {commits_word} this week")
    print(f"There {'has' if creates == 1 else 'have'} been {creates} {creates_word} created this week")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Github activity tracker")
    subparsers = parser.add_subparsers(dest="command")

    get_activity_parser = subparsers.add_parser("get-activity", help="Retreive users activity")
    get_activity_parser.add_argument("username", help="Username of user to fetch activity")
    args = parser.parse_args()
    if args.command == "get-activity":
        get_activity(args.username)
