#   GitHub Profile CLI - Show GitHub profile details on terminal.
#   Copyright (C) 2022  Kerem Biçen

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import re
import requests
from requests.exceptions import HTTPError

def main():
	username = input("username> ")
	if not re.match("^\w+$", username):
		print("Specified username is invalid.")
		return
	try:
		info = requests.get(f"https://api.github.com/users/{username}")
		info.raise_for_status()
		info = info.json()
		repos = requests.get(info["repos_url"]).json()
		print("\nName: {}\nNickname: {}\nRepos:\n\t{}".format(info["name"], info["login"], "\n\t".join([repo["name"] for repo in repos])))
	except HTTPError as e:
		if e.response.status_code == 404:
			print(f"'{username}' not found.")

if __name__ == "__main__":
	main()
