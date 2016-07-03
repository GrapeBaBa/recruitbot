import json
import os

import github
from github import Github

# First create a Github instance:

g = Github("grapebaba", "heatonn1",per_page=1000)


def main():
    '''
    Use small data for this application
    :return:
    '''
    with open(os.path.join(os.path.expanduser("~"),'recruitbot_data.txt'),'w') as f:
        for user in g.search_users("type:user")[0:10000]:
            user_dict = {}
            user_dict['username'] = user.login
            user_dict['id'] = user.id
            user_dict['profile_url'] = user.html_url
            user_dict['location'] = user.location
            user_dict['followers'] = user.followers
            user_dict['private_gists'] = user.private_gists
            user_dict['public_gists'] = user.public_gists
            user_dict['name'] = user.name
            user_dict['company'] = user.company
            user_dict['blog_url'] = user.blog
            user_dict['email'] = user.email
            user_dict['id'] = user.id
            user_dict['contributions']={}
            for repo in user.get_watched():
                try:
                    repo_total = 0
                    for _ in repo.get_commits():
                        repo_total = repo_total + 1
                    if repo.get_stats_contributors() is not None:
                        for contributor in repo.get_stats_contributors():
                            if contributor is not None and contributor.author.id == user_dict['id']:
                                user_dict['contributions'][repo.name]={}
                                user_dict['contributions'][repo.name]['contributor_commits']=contributor.total
                                user_dict['contributions'][repo.name]['repo_commits']=repo_total
                                user_dict['contributions'][repo.name]['language']=repo.language
                                user_dict['contributions'][repo.name]['stars']=repo.stargazers_count
                                print user_dict
                                break
                except github.GithubException as e:
                    print e

            f.write(json.dumps(user_dict)+"\n")

if __name__ == '__main__':
    main()
