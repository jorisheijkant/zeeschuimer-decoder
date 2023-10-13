# The parsing function for Tiktok content

def parse_tiktok(item, index):
    parsed_item = {}
    parsed_item['index'] = index
    parsed_item['id'] = item['item_id']

    # Here set up the full video string
    username_for_string = item['data']['author']['uniqueId']
    parsed_item['url'] = f"https://www.tiktok.com/@{username_for_string}/video/{item['item_id']}"

    parsed_item['description'] = item['data']['desc']
    parsed_item['author'] = item['data']['author']['nickname']
    parsed_item['author_followers'] = item['data']['authorStats']['followerCount']
    parsed_item['digg_count'] = item['data']['stats']['diggCount']
    parsed_item['share_count'] = item['data']['stats']['shareCount']
    parsed_item['comment_count'] = item['data']['stats']['commentCount']
    parsed_item['play_count'] = item['data']['stats']['playCount']
    parsed_item['search_url'] = item['source_platform_url']


    return parsed_item