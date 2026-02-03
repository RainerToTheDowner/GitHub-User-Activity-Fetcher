import requests

userinput = ""
while userinput != "exit":
    userinput = input("Enter a username (or exit): ")
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
                    totalPushesPerRepo[repo] = totalPushesPerRepo.get(repo, 0) + 1
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
                elif activity["type"] == "ForkEvent":
                    fork = activity["payload"]["forkee"]["full_name"]
                    print("Forked " + repo + " to create " + fork)
            for repo in totalPushesPerRepo:
                print("Pushed " + str(totalPushesPerRepo[repo]) + " commits to " + repo)
    else:
        print("Invalid username")