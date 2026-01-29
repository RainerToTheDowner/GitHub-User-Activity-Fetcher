import requests

userinput = ""
while userinput != "exit":
    userinput = input()
    if userinput == "exit":
        break

    userdata = (requests.get(f"https://api.github.com/users/{userinput}/events")).json()
    totalPushesPerRepo = {}
    for activity in userdata:
        fullrepolink = activity["repo"]["url"]
        repo = fullrepolink.split("/")[-2:]
        repo = "/".join(repo)
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
    for repo in list(totalPushesPerRepo.keys()):
        print("Pushed " + str(totalPushesPerRepo[repo]) + " commits to " + repo)