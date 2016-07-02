import json

from github import Github

# First create a Github instance:

g = Github("grapebaba", "heatonn1",per_page=500)


def main():
    '''
    Use small data for this application
    :return:
    '''
    for user in g.search_users("type:user language:java")[0:1]:
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

        print json.dumps(user_dict)


def _filter(contributor, id):
    if contributor.author is not None:
        return contributor.author.id == id
    else:
        return False


if __name__ == '__main__':
    main()
