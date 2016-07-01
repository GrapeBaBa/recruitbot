from github import Github

# First create a Github instance:

g = Github("grapebaba", "heatonn1")


def main():
    '''
    Use small data for this application
    :return:
    '''
    print g.search_users("type:user language:java").totalCount
    for user in g.search_users("type:user language:java")[0:1]:
        username=user.login
        id=user.id
        profile_url=user.html_url
        location=user.location
        followers=user.followers
        private_gists=user.private_gists
        public_gists=user.public_gists
        name=user.name
        company=user.company
        blog_url=user.blog
        email=user.email
        print email
        print blog_url
        print company
        print name
        print username
        print id
        print location
        print followers
        print profile_url
        print private_gists
        print public_gists
        reposs=user.get_repos()
        for repo in reposs:
            print repo.name



if __name__ == '__main__':
    main()
