#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv  # Import the csv module
from github import Github

ACCESS_TOKEN = '' # Replace with your GitHub access token
g = Github(ACCESS_TOKEN)


def search_github(keywords):
    query = '+'.join(keywords) + '+ in:readme stars:50..59'
    result = g.search_repositories(query, 'stars', 'desc')
    print(f'Found {result.totalCount} repo(s)')
    return result


if __name__ == '__main__':
    keywords = ['deep neural network']
    repo = search_github(keywords)

    filtered_repo = []
    c = []

    for r in repo:
        c.append(r.clone_url)

    aa = []

    for cc in c:
        aa.append(cc.split('https://github.com/')[1].split('.git')[0])

    count = 0

    for cc in aa:
        try:
            reponame = cc
            repos = g.get_repo(reponame)
            releases = repos.get_releases()
            count += 1
            print(count)
            if releases.totalCount > 1:
                filtered_repo.append(cc)
        except Exception:
            pass
    # print(filtered_repo)
    # Save filtered_repo data to a CSV file
    with open('50..59.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Repository'])
        csv_writer.writerows([[repo] for repo in filtered_repo])

    print("Filtered data saved to '50..59.csv'")
                                                                                                                                                                                                                                             