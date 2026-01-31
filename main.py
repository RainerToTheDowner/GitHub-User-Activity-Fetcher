import requests

userinput = ""
while userinput != "exit":
    userinput = input()
    if userinput == "exit":
        break

    userdata = (requests.get(f"https://api.github.com/users/{userinput}/events")).json()
    totalPushesPerRepo = {}
    if "message" not in userdata:
        if len(userdata) == 0:
            print("No recent activity")
        else: 
            for activity in userdata:
                repo = activity["repo"]["name"]
                if activity["type"] == "PushEvent":
                    try:
                        totalPushesPerRepo[repo] += 1
                    except:
                        totalPushesPerRepo[repo] = 1
                elif activity["type"] == "WatchEvent":
                    print("Starred " + repo)
                elif activity["type"] == "IssuesEvent":
                    action = activity["payload"]["action"]
                    if action == "opened":
                        print("Opened a new issue in " + repo)
                    else:
                        print(action.capitalize() + " an issue in " + repo)
                elif activity["type"] == "IssueCommentEvent":
                    comment = activity["payload"]["comment"]["body"]
                    print("Commented '" + comment + "' on " + repo)
            for repo in list(totalPushesPerRepo.keys()):
                print("Pushed " + str(totalPushesPerRepo[repo]) + " commits to " + repo)
    else:
        print("Invalid username")