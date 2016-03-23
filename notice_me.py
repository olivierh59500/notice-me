import requests
import json


class attention_whore:

    def __init__(self, username, password):
        self.gh_username = username
        self.gh_access = password

    def get_users(self, min_followers, max_num=-1):
        user_count = 0
        page = 1

        user_list = []

        while user_count < max_num or max_num == -1:

            search_request = requests.get(
                "https://api.github.com/search/users?q=followers:%3E" +
                str(min_followers) + "&per_page=300&page=" + str(page),
                auth=(self.gh_username, self.gh_access))

            search_results = json.loads(search_request.text)

            if max_num == -1 and page == 1:
                max_num = search_results["total_count"]

            for user in search_results["items"]:
                user_list.append(user["login"])
                user_count += 1

            page += 1

        return user_list

    def touch_collaborator(self, project, username):

        request_string = ("https://api.github.com/repos/" + self.gh_username + "/" +
                          project + "/collaborators/" + username)

        add_request = requests.put(request_string, auth=(
            self.gh_username, self.gh_access))

        remove_request = requests.delete(
            request_string, auth=(self.gh_username, self.gh_access))

if __name__ == "__main__":
    print("notice-me.py is a library. try example.py")
