
from flask import Flask
from flask import render_template
import requests


app = Flask(__name__)


@app.route("/")
def index():
    user_data = requests.get('https://api.github.com/users/janeenscott') # api for main github data
    translated = user_data.json() # translated is a dictionary (call it with brackets)
    # translated is a dictionary

    repo_content = requests.get('https://api.github.com/users/janeenscott/repos') # api for repo data
    translated_repo = repo_content.json() # translated_repo is a list of dictionaries. 'repos' in
                                          # context below contains a list of dictionaries now. So I can
                                          # call dictionary items from the list through dot notation
                                          # in my index.html file
    context = {
        'name': translated['name'],
        'username': translated['login'],
        'bio': translated['bio'],
        'location': translated['location'],
        'email': translated['email'],
        'bio_image': translated['avatar_url'],
        'repos_url': translated['repos_url'],
        'repos': translated_repo
    }
    # this is saying, 'name' is now a variable that is pulling from a key value pair in the dictionary, translated
    # so translated['name'] pulls the value from the key 'name' in the dictionary translated, and puts it in a
    # new variable, 'name'. Now 'name' will be populated with API data from translated.

    return render_template('index.html', **context)
                                            # had repos=translated_repos below when I thought I could
                                            # have two functions under one app route. So I put it in the
                                            # context so it can be accessed and put through index file


@app.route('/followers/')
def followers():

    user_data = requests.get('https://api.github.com/users/janeenscott')
    translated = user_data.json()

    follower_content = requests.get(translated['followers_url'])
    # same as follower_content = requests.get(https://api.github.com/users/janeenscott/followers)
    translated_followers = follower_content.json()
    #translated followers is a list of dictionaries

    follower_data = []

    for follower in translated_followers:           # the variable follower is a dictionary containing the info for an
        follower_url = follower['url']              # individual follower. I need to extract the url
        print(follower_url)
        # follower_url is the specific url for the follower api
        # which was called from the follower dictionary by follower['url']
        # now, each time it loops over the list of translated_followers, it will populate
        # the variable follower_url with that specific api request address

    follower_api = requests.get(follower_url)

        # this should populate follower_api with the specific follower api request

        # follower_data = follower_data.append(follower_api)

    print(follower_api)


    context = {
        'name': translated['name'],
        'username': translated['login'],
        'bio': translated['bio'],
        'location': translated['location'],
        'email': translated['email'],
        'bio_image': translated['avatar_url'],
        'repos_url': translated['repos_url'],
        'followers': follower_api
    }

    return render_template('followers.html', **context)
