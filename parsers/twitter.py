# The parsing function for Twitter content

def parse_twitter(item, index):
    parsed_item = {}
    parsed_item['index'] = index
    parsed_item['id'] = item['item_id']

    user = item['data']['core']['user_results']['result']

    # Here set up the full video string
    parsed_item['url'] = ""
    if(user):
        print(user)
        username_for_string = user['legacy']['screen_name']
        parsed_item['url'] = f"https://www.twitter.com/@{username_for_string}/status/{item['item_id']}"

    parsed_item['tweet'] = item['data']['legacy']['full_text']
    parsed_item['is_retweet'] = item['data']['legacy']['retweeted']
    parsed_item['author'] = ""
    if(user):
        parsed_item['author'] = user['legacy']['name']
    parsed_item['author_followers'] = ""
    if(user):
        parsed_item['author_followers'] = user['legacy']['followers_count']
    parsed_item['view_count'] = item['data']['views']['count']
    parsed_item['heart_count'] = item['data']['legacy']['favorite_count']
    parsed_item['retweet_count'] = item['data']['legacy']['retweet_count']
    parsed_item['reply_count'] = item['data']['legacy']['reply_count']
    parsed_item['search_url'] = item['source_platform_url']


    return parsed_item