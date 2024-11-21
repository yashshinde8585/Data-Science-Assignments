# 4) Write a Python program to get the number of followers of any twitter account.

from TwitterAPI import TwitterAPI


CONSUMER_KEY = "wLRyiaWuBENS0c8FTBcuwZSLI"
CONSUMER_SECRET = "kPvx3M54gvw59PfUyUn1EpbKvPUCbUoSkXXdBTJPnZnltcYF8R"
ACCESS_TOKEN_KEY = "1849864773829361664-vF32L1mSWKS7Iyain0tPQ3KKFmm7jk"
ACCESS_TOKEN_SECRET = "l197njYzbuaP4emQHUgbO6rfnCShNRrinsa0WauFGjAl6"


api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

screen_name = 'elonmusk'  

try:
    
    response = api.request('users/show', {'screen_name': screen_name})

    if response.status_code == 200:
        user_data = response.json()
        follower_count = user_data['followers_count']
        print(f"Total followers for @{screen_name}: {follower_count}")
    else:
        print(f"Failed to get user data: {response.status_code} - {response.text}")

except Exception as e:
    print(f"An error occurred: {e}")
