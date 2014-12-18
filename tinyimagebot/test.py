import unittest2
from models import SimpleTweet
import image_processor

class TestTweetModel(unittest2.TestCase):

    def setUp(self):
        # no hashtag
        self.dm_no_hashtag = {u'direct_message': {u'created_at': u'Thu Dec 18 17:15:40 +0000 2014', u'recipient_id_str': u'2929029785', u'sender': {u'follow_request_sent': False, u'profile_use_background_image': True, u'default_profile_image': False, u'id': 11194772, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme9/bg.gif', u'verified': False, u'profile_location': None, u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/474958498023755777/ab-d_9F1_normal.jpeg', u'profile_sidebar_fill_color': u'252429', u'profile_text_color': u'666666', u'followers_count': 171, u'profile_sidebar_border_color': u'181A1E', u'id_str': u'11194772', u'profile_background_color': u'1A1B1F', u'listed_count': 9, u'is_translation_enabled': False, u'utc_offset': -28800, u'statuses_count': 92, u'description': u'As it is in the Void, so it is under my skin.', u'friends_count': 154, u'location': u'Los Angeles, CA', u'profile_link_color': u'2FC2EF', u'profile_image_url': u'http://pbs.twimg.com/profile_images/474958498023755777/ab-d_9F1_normal.jpeg', u'following': False, u'geo_enabled': False, u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme9/bg.gif', u'name': u'Jim Fingal', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 92, u'screen_name': u'jimfingal', u'notifications': False, u'url': u'http://jimfingal.com', u'created_at': u'Sat Dec 15 13:04:23 +0000 2007', u'contributors_enabled': False, u'time_zone': u'Pacific Time (US & Canada)', u'protected': False, u'default_profile': False, u'is_translator': False}, u'sender_id_str': u'11194772', u'text': u'dm no hashtag', u'sender_screen_name': u'jimfingal', u'sender_id': 11194772, u'entities': {u'symbols': [], u'user_mentions': [], u'hashtags': [], u'urls': []}, u'recipient_id': 2929029785, u'id_str': u'545628473616646144', u'recipient_screen_name': u'tinyimagebot', u'recipient': {u'follow_request_sent': False, u'profile_use_background_image': True, u'default_profile_image': True, u'id': 2929029785, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme1/bg.png', u'verified': False, u'profile_location': None, u'profile_image_url_https': u'https://abs.twimg.com/sticky/default_profile_images/default_profile_3_normal.png', u'profile_sidebar_fill_color': u'DDEEF6', u'profile_text_color': u'333333', u'followers_count': 0, u'profile_sidebar_border_color': u'C0DEED', u'id_str': u'2929029785', u'profile_background_color': u'C0DEED', u'listed_count': 0, u'is_translation_enabled': False, u'utc_offset': None, u'statuses_count': 0, u'description': None, u'friends_count': 1, u'location': None, u'profile_link_color': u'0084B4', u'profile_image_url': u'http://abs.twimg.com/sticky/default_profile_images/default_profile_3_normal.png', u'following': False, u'geo_enabled': False, u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme1/bg.png', u'name': u'Tiny Image Bot', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 0, u'screen_name': u'tinyimagebot', u'notifications': False, u'url': None, u'created_at': u'Thu Dec 18 05:24:06 +0000 2014', u'contributors_enabled': False, u'time_zone': None, u'protected': False, u'default_profile': True, u'is_translator': False}, u'id': 545628473616646144}}

        # has #hashtag hashtag
        self.dm_hashtag = {u'direct_message': {u'created_at': u'Thu Dec 18 17:16:21 +0000 2014', u'recipient_id_str': u'2929029785', u'sender': {u'follow_request_sent': False, u'profile_use_background_image': True, u'default_profile_image': False, u'id': 11194772, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme9/bg.gif', u'verified': False, u'profile_location': None, u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/474958498023755777/ab-d_9F1_normal.jpeg', u'profile_sidebar_fill_color': u'252429', u'profile_text_color': u'666666', u'followers_count': 171, u'profile_sidebar_border_color': u'181A1E', u'id_str': u'11194772', u'profile_background_color': u'1A1B1F', u'listed_count': 9, u'is_translation_enabled': False, u'utc_offset': -28800, u'statuses_count': 92, u'description': u'As it is in the Void, so it is under my skin.', u'friends_count': 154, u'location': u'Los Angeles, CA', u'profile_link_color': u'2FC2EF', u'profile_image_url': u'http://pbs.twimg.com/profile_images/474958498023755777/ab-d_9F1_normal.jpeg', u'following': False, u'geo_enabled': False, u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme9/bg.gif', u'name': u'Jim Fingal', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 92, u'screen_name': u'jimfingal', u'notifications': False, u'url': u'http://jimfingal.com', u'created_at': u'Sat Dec 15 13:04:23 +0000 2007', u'contributors_enabled': False, u'time_zone': u'Pacific Time (US & Canada)', u'protected': False, u'default_profile': False, u'is_translator': False}, u'sender_id_str': u'11194772', u'text': u'dm #hashtag', u'sender_screen_name': u'jimfingal', u'sender_id': 11194772, u'entities': {u'symbols': [], u'user_mentions': [], u'hashtags': [{u'indices': [3, 11], u'text': u'hashtag'}], u'urls': []}, u'recipient_id': 2929029785, u'id_str': u'545628648082923520', u'recipient_screen_name': u'tinyimagebot', u'recipient': {u'follow_request_sent': False, u'profile_use_background_image': True, u'default_profile_image': True, u'id': 2929029785, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme1/bg.png', u'verified': False, u'profile_location': None, u'profile_image_url_https': u'https://abs.twimg.com/sticky/default_profile_images/default_profile_3_normal.png', u'profile_sidebar_fill_color': u'DDEEF6', u'profile_text_color': u'333333', u'followers_count': 0, u'profile_sidebar_border_color': u'C0DEED', u'id_str': u'2929029785', u'profile_background_color': u'C0DEED', u'listed_count': 0, u'is_translation_enabled': False, u'utc_offset': None, u'statuses_count': 0, u'description': None, u'friends_count': 1, u'location': None, u'profile_link_color': u'0084B4', u'profile_image_url': u'http://abs.twimg.com/sticky/default_profile_images/default_profile_3_normal.png', u'following': False, u'geo_enabled': False, u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme1/bg.png', u'name': u'Tiny Image Bot', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 0, u'screen_name': u'tinyimagebot', u'notifications': False, u'url': None, u'created_at': u'Thu Dec 18 05:24:06 +0000 2014', u'contributors_enabled': False, u'time_zone': None, u'protected': False, u'default_profile': True, u'is_translator': False}, u'id': 545628648082923520}}

        # DM with image and hashtag
        self.dm_image = {u'direct_message': {u'created_at': u'Thu Dec 18 17:18:14 +0000 2014', u'recipient_id_str': u'2929029785', u'sender': {u'follow_request_sent': False, u'profile_use_background_image': True, u'default_profile_image': False, u'id': 11194772, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme9/bg.gif', u'verified': False, u'profile_location': None, u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/474958498023755777/ab-d_9F1_normal.jpeg', u'profile_sidebar_fill_color': u'252429', u'profile_text_color': u'666666', u'followers_count': 171, u'profile_sidebar_border_color': u'181A1E', u'id_str': u'11194772', u'profile_background_color': u'1A1B1F', u'listed_count': 9, u'is_translation_enabled': False, u'utc_offset': -28800, u'statuses_count': 92, u'description': u'As it is in the Void, so it is under my skin.', u'friends_count': 154, u'location': u'Los Angeles, CA', u'profile_link_color': u'2FC2EF', u'profile_image_url': u'http://pbs.twimg.com/profile_images/474958498023755777/ab-d_9F1_normal.jpeg', u'following': False, u'geo_enabled': False, u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme9/bg.gif', u'name': u'Jim Fingal', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 92, u'screen_name': u'jimfingal', u'notifications': False, u'url': u'http://jimfingal.com', u'created_at': u'Sat Dec 15 13:04:23 +0000 2007', u'contributors_enabled': False, u'time_zone': u'Pacific Time (US & Canada)', u'protected': False, u'default_profile': False, u'is_translator': False}, u'sender_id_str': u'11194772', u'text': u'dm image #hashtag https://t.co/mnk3H4jo6O', u'sender_screen_name': u'jimfingal', u'sender_id': 11194772, u'entities': {u'symbols': [], u'user_mentions': [], u'hashtags': [{u'indices': [9, 17], u'text': u'hashtag'}], u'urls': [{u'url': u'https://t.co/mnk3H4jo6O', u'indices': [18, 41], u'expanded_url': u'https://twitter.com/messages/media/545629119480733698', u'display_url': u'pic.twitter.com/mnk3H4jo6O'}], u'media': [{u'expanded_url': u'https://twitter.com/messages/media/545629119480733698', u'display_url': u'pic.twitter.com/mnk3H4jo6O', u'url': u'https://t.co/mnk3H4jo6O', u'media_url_https': u'https://ton.twitter.com/1.1/ton/data/dm/545629119480733698/545629119493320704/I6D0P1CX.png', u'id_str': u'545629119493320704', u'sizes': {u'large': {u'h': 8, u'resize': u'fit', u'w': 8}, u'small': {u'h': 8, u'resize': u'fit', u'w': 8}, u'medium': {u'h': 8, u'resize': u'fit', u'w': 8}, u'thumb': {u'h': 8, u'resize': u'crop', u'w': 8}}, u'indices': [18, 41], u'type': u'photo', u'id': 545629119493320704, u'media_url': u'https://ton.twitter.com/1.1/ton/data/dm/545629119480733698/545629119493320704/I6D0P1CX.png'}]}, u'recipient_id': 2929029785, u'id_str': u'545629119480733698', u'recipient_screen_name': u'tinyimagebot', u'recipient': {u'follow_request_sent': False, u'profile_use_background_image': True, u'default_profile_image': True, u'id': 2929029785, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme1/bg.png', u'verified': False, u'profile_location': None, u'profile_image_url_https': u'https://abs.twimg.com/sticky/default_profile_images/default_profile_3_normal.png', u'profile_sidebar_fill_color': u'DDEEF6', u'profile_text_color': u'333333', u'followers_count': 0, u'profile_sidebar_border_color': u'C0DEED', u'id_str': u'2929029785', u'profile_background_color': u'C0DEED', u'listed_count': 0, u'is_translation_enabled': False, u'utc_offset': None, u'statuses_count': 0, u'description': None, u'friends_count': 1, u'location': None, u'profile_link_color': u'0084B4', u'profile_image_url': u'http://abs.twimg.com/sticky/default_profile_images/default_profile_3_normal.png', u'following': False, u'geo_enabled': False, u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme1/bg.png', u'name': u'Tiny Image Bot', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 0, u'screen_name': u'tinyimagebot', u'notifications': False, u'url': None, u'created_at': u'Thu Dec 18 05:24:06 +0000 2014', u'contributors_enabled': False, u'time_zone': None, u'protected': False, u'default_profile': True, u'is_translator': False}, u'id': 545629119480733698}}

        # Plain messages
        self.msg_no_hashtag = {u'contributors': None, 
                                u'truncated': False, 
                                u'text': u'@tinyimagebot message plain old', 
                                u'in_reply_to_status_id': None, 
                                u'id': 545629378588065792, 
                                u'favorite_count': 0, 
                                u'source': u'<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>', 
                                u'retweeted': False, u'coordinates': None, 
                                u'timestamp_ms': u'1418923155816', 
                                u'entities': {u'symbols': [], 
                                                u'user_mentions': 
                                                    [{u'id': 2929029785, 
                                                        u'indices': [0, 13], 
                                                        u'id_str': u'2929029785', 
                                                        u'screen_name': u'tinyimagebot', 
                                                        u'name': u'Tiny Image Bot'}], 
                                                u'hashtags': [], 
                                                u'urls': []
                                            }, 
                                u'in_reply_to_screen_name': u'tinyimagebot', 
                                u'id_str': u'545629378588065792', 
                                u'retweet_count': 0, 
                                u'in_reply_to_user_id': 2929029785, 
                                u'favorited': False, 
                                u'user': {u'follow_request_sent': None, 
                                        u'profile_use_background_image': True, 
                                        u'default_profile_image': False, 
                                        u'id': 11194772, 
                                        u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme9/bg.gif',
                                         u'verified': False, 
                                         u'profile_location': None, 
                                         u'profile_image_url_https': 
                                         u'https://pbs.twimg.com/profile_images/474958498023755777/ab-d_9F1_normal.jpeg', 
                                         u'profile_sidebar_fill_color': u'252429', 
                                         u'profile_text_color': u'666666', 
                                         u'followers_count': 171, 
                                         u'profile_sidebar_border_color': u'181A1E',
                                          u'id_str': u'11194772', 
                                          u'profile_background_color': u'1A1B1F', 
                                          u'listed_count': 9, u'is_translation_enabled': False, 
                                          u'utc_offset': -28800, 
                                          u'statuses_count': 93, 
                                          u'description': u'As it is in the Void, so it is under my skin.', 
                                          u'friends_count': 154, 
                                          u'location': u'Los Angeles, CA', u'profile_link_color': u'2FC2EF', 
                                          u'profile_image_url': u'http://pbs.twimg.com/profile_images/474958498023755777/ab-d_9F1_normal.jpeg', 
                                          u'following': None, u'geo_enabled': False, 
                                          u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme9/bg.gif', 
                                          u'name': u'Jim Fingal', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 92, 
                                          u'screen_name': u'jimfingal', 
                                          u'notifications': None, u'url': u'http://jimfingal.com', 
                                          u'created_at': u'Sat Dec 15 13:04:23 +0000 2007', u'contributors_enabled': False, 
                                          u'time_zone': u'Pacific Time (US & Canada)', u'protected': False, u'default_profile': False, u'is_translator': False}, 
                                u'geo': None, 
                                u'in_reply_to_user_id_str': u'2929029785', 
                                u'lang': u'en', 
                                u'created_at': u'Thu Dec 18 17:19:15 +0000 2014', 
                                u'filter_level': u'medium', 
                                u'in_reply_to_status_id_str': None, 
                                u'place': None}

        # Msg hashtag
        self.msg_hashtag = {u'contributors': None, u'truncated': False, u'text': u'@tinyimagebot message #hashtag', u'in_reply_to_status_id': None, u'id': 545629535480188928, u'favorite_count': 0, u'source': u'<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>', u'retweeted': False, u'coordinates': None, u'timestamp_ms': u'1418923193222', u'entities': {u'symbols': [], u'user_mentions': [{u'id': 2929029785, u'indices': [0, 13], u'id_str': u'2929029785', u'screen_name': u'tinyimagebot', u'name': u'Tiny Image Bot'}], u'hashtags': [{u'indices': [22, 30], u'text': u'hashtag'}], u'urls': []}, u'in_reply_to_screen_name': u'tinyimagebot', u'id_str': u'545629535480188928', u'retweet_count': 0, u'in_reply_to_user_id': 2929029785, u'favorited': False, u'user': {u'follow_request_sent': None, u'profile_use_background_image': True, u'default_profile_image': False, u'id': 11194772, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme9/bg.gif', u'verified': False, u'profile_location': None, u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/474958498023755777/ab-d_9F1_normal.jpeg', u'profile_sidebar_fill_color': u'252429', u'profile_text_color': u'666666', u'followers_count': 171, u'profile_sidebar_border_color': u'181A1E', u'id_str': u'11194772', u'profile_background_color': u'1A1B1F', u'listed_count': 9, u'is_translation_enabled': False, u'utc_offset': -28800, u'statuses_count': 94, u'description': u'As it is in the Void, so it is under my skin.', u'friends_count': 154, u'location': u'Los Angeles, CA', u'profile_link_color': u'2FC2EF', u'profile_image_url': u'http://pbs.twimg.com/profile_images/474958498023755777/ab-d_9F1_normal.jpeg', u'following': None, u'geo_enabled': False, u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme9/bg.gif', u'name': u'Jim Fingal', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 92, u'screen_name': u'jimfingal', u'notifications': None, u'url': u'http://jimfingal.com', u'created_at': u'Sat Dec 15 13:04:23 +0000 2007', u'contributors_enabled': False, u'time_zone': u'Pacific Time (US & Canada)', u'protected': False, u'default_profile': False, u'is_translator': False}, u'geo': None, u'in_reply_to_user_id_str': u'2929029785', u'lang': u'en', u'created_at': u'Thu Dec 18 17:19:53 +0000 2014', u'filter_level': u'medium', u'in_reply_to_status_id_str': None, u'place': None}

        # Msg Image
        self.msg_image = {u'contributors': None, u'truncated': False, u'text': u'@tinyimagebot message image http://t.co/Lyk6QhTzko', u'in_reply_to_status_id': None, u'id': 545629672269021185, u'favorite_count': 0, u'source': u'<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>', u'retweeted': False, u'coordinates': None, u'timestamp_ms': u'1418923225835', 
                        u'entities': {u'symbols': [], 
                                u'user_mentions': [{
                                                u'id': 2929029785,
                                                 u'indices': [0, 13], 
                                                 u'id_str': u'2929029785', 
                                                 u'screen_name': u'tinyimagebot', 
                                                 u'name': u'Tiny Image Bot'}], 
                                u'hashtags': [], 
                                u'urls': [], 
                                u'media': [
                                        {u'expanded_url': u'http://twitter.com/jimfingal/status/545629672269021185/photo/1', 
                                        u'display_url': u'pic.twitter.com/Lyk6QhTzko', 
                                        u'url': u'http://t.co/Lyk6QhTzko', 
                                        u'media_url_https': u'https://pbs.twimg.com/media/B5J3S3aIIAI_J27.png', 
                                        u'id_str': u'545629670860136450', 
                                        u'sizes': {u'large': {u'h': 8, u'resize': u'fit', u'w': 8}, 
                                        u'small': {u'h': 8, u'resize': u'fit', u'w': 8}, 
                                        u'medium': {u'h': 8, u'resize': u'fit', u'w': 8}, 
                                        u'thumb': {u'h': 8, u'resize': u'crop', u'w': 8}}, 
                                        u'indices': [28, 50], 
                                        u'type': u'photo', 
                                        u'id': 545629670860136450, 
                                        u'media_url': u'http://pbs.twimg.com/media/B5J3S3aIIAI_J27.png'}]}, 
                                u'in_reply_to_screen_name': u'tinyimagebot', u'id_str': u'545629672269021185', u'retweet_count': 0, u'in_reply_to_user_id': 2929029785, u'favorited': False, u'user': {u'follow_request_sent': None, u'profile_use_background_image': True, u'default_profile_image': False, u'id': 11194772, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme9/bg.gif', u'verified': False, u'profile_location': None, u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/474958498023755777/ab-d_9F1_normal.jpeg', u'profile_sidebar_fill_color': u'252429', u'profile_text_color': u'666666', u'followers_count': 171, u'profile_sidebar_border_color': u'181A1E', u'id_str': u'11194772', u'profile_background_color': u'1A1B1F', u'listed_count': 9, u'is_translation_enabled': False, u'utc_offset': -28800, u'statuses_count': 95, u'description': u'As it is in the Void, so it is under my skin.', u'friends_count': 154, u'location': u'Los Angeles, CA', u'profile_link_color': u'2FC2EF', u'profile_image_url': u'http://pbs.twimg.com/profile_images/474958498023755777/ab-d_9F1_normal.jpeg', u'following': None, u'geo_enabled': False, u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme9/bg.gif', u'name': u'Jim Fingal', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 92, u'screen_name': u'jimfingal', u'notifications': None, u'url': u'http://jimfingal.com', u'created_at': u'Sat Dec 15 13:04:23 +0000 2007', u'contributors_enabled': False, u'time_zone': u'Pacific Time (US & Canada)', u'protected': False, u'default_profile': False, u'is_translator': False}, u'geo': None, u'in_reply_to_user_id_str': u'2929029785', u'possibly_sensitive': False, u'lang': u'fr', u'created_at': u'Thu Dec 18 17:20:25 +0000 2014', u'filter_level': u'medium', u'in_reply_to_status_id_str': None, u'place': None, u'extended_entities': {u'media': [{u'expanded_url': u'http://twitter.com/jimfingal/status/545629672269021185/photo/1', u'display_url': u'pic.twitter.com/Lyk6QhTzko', u'url': u'http://t.co/Lyk6QhTzko', u'media_url_https': u'https://pbs.twimg.com/media/B5J3S3aIIAI_J27.png', u'id_str': u'545629670860136450', u'sizes': {u'large': {u'h': 8, u'resize': u'fit', u'w': 8}, u'small': {u'h': 8, u'resize': u'fit', u'w': 8}, u'medium': {u'h': 8, u'resize': u'fit', u'w': 8}, u'thumb': {u'h': 8, u'resize': u'crop', u'w': 8}}, u'indices': [28, 50], u'type': u'photo', u'id': 545629670860136450, u'media_url': u'http://pbs.twimg.com/media/B5J3S3aIIAI_J27.png'}]}}


    def test_parse_id(self):
        status = SimpleTweet(self.msg_no_hashtag)
        self.assertEqual(status.tweet_id, 545629378588065792)

    def test_parse_text(self):
        status = SimpleTweet(self.msg_no_hashtag)
        self.assertEqual(status.text, '@tinyimagebot message plain old')

    def test_parse_sender(self):
        status = SimpleTweet(self.msg_no_hashtag)
        self.assertEqual(status.sender_screen_name, 'jimfingal')

    def test_parse_hashtags_none(self):
        status = SimpleTweet(self.msg_no_hashtag)
        self.assertEqual(len(status.hashtags), 0)

    def test_parse_user_mentions(self):
        status = SimpleTweet(self.msg_no_hashtag)
        self.assertEqual(len(status.user_mentions), 1)
        self.assertTrue('tinyimagebot' in status.user_mentions)

    def test_parse_hashtags(self):
        status = SimpleTweet(self.msg_hashtag)
        self.assertEqual(len(status.hashtags), 1)
        self.assertTrue('hashtag' in status.hashtags)
    
    def test_parse_media_none(self):
        status = SimpleTweet(self.msg_no_hashtag)
        self.assertIsNone(status.media)

    def test_parse_media(self):
        status = SimpleTweet(self.msg_image)
        self.assertIsNotNone(status.media)
        self.assertEqual(status.media, 'https://pbs.twimg.com/media/B5J3S3aIIAI_J27.png')


class TestImageProc(unittest2.TestCase):

    def setUp(self):

        # Plain messages
        self.msg_no_img = {u'contributors': None, 
                                u'truncated': False, 
                                u'text': u'@tinyimagebot message plain old', 
                                u'in_reply_to_status_id': None, 
                                u'id': 545629378588065792, 
                                u'favorite_count': 0, 
                                u'source': u'<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>', 
                                u'retweeted': False, u'coordinates': None, 
                                u'timestamp_ms': u'1418923155816', 
                                u'entities': {u'symbols': [], 
                                                u'user_mentions': 
                                                    [{u'id': 2929029785, 
                                                        u'indices': [0, 13], 
                                                        u'id_str': u'2929029785', 
                                                        u'screen_name': u'tinyimagebot', 
                                                        u'name': u'Tiny Image Bot'}], 
                                                u'hashtags': [], 
                                                u'urls': []
                                            }, 
                                u'in_reply_to_screen_name': u'tinyimagebot', 
                                u'id_str': u'545629378588065792', 
                                u'retweet_count': 0, 
                                u'in_reply_to_user_id': 2929029785, 
                                u'favorited': False, 
                                u'user': {u'follow_request_sent': None, 
                                        u'profile_use_background_image': True, 
                                        u'default_profile_image': False, 
                                        u'id': 11194772, 
                                        u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme9/bg.gif',
                                         u'verified': False, 
                                         u'profile_location': None, 
                                         u'profile_image_url_https': 
                                         u'https://pbs.twimg.com/profile_images/474958498023755777/ab-d_9F1_normal.jpeg', 
                                         u'profile_sidebar_fill_color': u'252429', 
                                         u'profile_text_color': u'666666', 
                                         u'followers_count': 171, 
                                         u'profile_sidebar_border_color': u'181A1E',
                                          u'id_str': u'11194772', 
                                          u'profile_background_color': u'1A1B1F', 
                                          u'listed_count': 9, u'is_translation_enabled': False, 
                                          u'utc_offset': -28800, 
                                          u'statuses_count': 93, 
                                          u'description': u'As it is in the Void, so it is under my skin.', 
                                          u'friends_count': 154, 
                                          u'location': u'Los Angeles, CA', u'profile_link_color': u'2FC2EF', 
                                          u'profile_image_url': u'http://pbs.twimg.com/profile_images/474958498023755777/ab-d_9F1_normal.jpeg', 
                                          u'following': None, u'geo_enabled': False, 
                                          u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme9/bg.gif', 
                                          u'name': u'Jim Fingal', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 92, 
                                          u'screen_name': u'jimfingal', 
                                          u'notifications': None, u'url': u'http://jimfingal.com', 
                                          u'created_at': u'Sat Dec 15 13:04:23 +0000 2007', u'contributors_enabled': False, 
                                          u'time_zone': u'Pacific Time (US & Canada)', u'protected': False, u'default_profile': False, u'is_translator': False}, 
                                u'geo': None, 
                                u'in_reply_to_user_id_str': u'2929029785', 
                                u'lang': u'en', 
                                u'created_at': u'Thu Dec 18 17:19:15 +0000 2014', 
                                u'filter_level': u'medium', 
                                u'in_reply_to_status_id_str': None, 
                                u'place': None}


        # Msg Image
        self.msg_image = {u'contributors': None, u'truncated': False, u'text': u'@tinyimagebot message image http://t.co/Lyk6QhTzko', u'in_reply_to_status_id': None, u'id': 545629672269021185, u'favorite_count': 0, u'source': u'<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>', u'retweeted': False, u'coordinates': None, u'timestamp_ms': u'1418923225835', 
                        u'entities': {u'symbols': [], 
                                u'user_mentions': [{
                                                u'id': 2929029785,
                                                 u'indices': [0, 13], 
                                                 u'id_str': u'2929029785', 
                                                 u'screen_name': u'tinyimagebot', 
                                                 u'name': u'Tiny Image Bot'}], 
                                u'hashtags': [{u'indices': [22, 30], u'text': u'tiny'}],
                                u'urls': [], 
                                u'media': [
                                        {u'expanded_url': u'http://twitter.com/jimfingal/status/545629672269021185/photo/1', 
                                        u'display_url': u'pic.twitter.com/Lyk6QhTzko', 
                                        u'url': u'http://t.co/Lyk6QhTzko', 
                                        u'media_url_https': u'https://pbs.twimg.com/media/B5J3S3aIIAI_J27.png', 
                                        u'id_str': u'545629670860136450', 
                                        u'sizes': {u'large': {u'h': 8, u'resize': u'fit', u'w': 8}, 
                                        u'small': {u'h': 8, u'resize': u'fit', u'w': 8}, 
                                        u'medium': {u'h': 8, u'resize': u'fit', u'w': 8}, 
                                        u'thumb': {u'h': 8, u'resize': u'crop', u'w': 8}}, 
                                        u'indices': [28, 50], 
                                        u'type': u'photo', 
                                        u'id': 545629670860136450, 
                                        u'media_url': u'http://pbs.twimg.com/media/B5J3S3aIIAI_J27.png'}]}, 
                                u'in_reply_to_screen_name': u'tinyimagebot', u'id_str': u'545629672269021185', u'retweet_count': 0, u'in_reply_to_user_id': 2929029785, u'favorited': False, u'user': {u'follow_request_sent': None, u'profile_use_background_image': True, u'default_profile_image': False, u'id': 11194772, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme9/bg.gif', u'verified': False, u'profile_location': None, u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/474958498023755777/ab-d_9F1_normal.jpeg', u'profile_sidebar_fill_color': u'252429', u'profile_text_color': u'666666', u'followers_count': 171, u'profile_sidebar_border_color': u'181A1E', u'id_str': u'11194772', u'profile_background_color': u'1A1B1F', u'listed_count': 9, u'is_translation_enabled': False, u'utc_offset': -28800, u'statuses_count': 95, u'description': u'As it is in the Void, so it is under my skin.', u'friends_count': 154, u'location': u'Los Angeles, CA', u'profile_link_color': u'2FC2EF', u'profile_image_url': u'http://pbs.twimg.com/profile_images/474958498023755777/ab-d_9F1_normal.jpeg', u'following': None, u'geo_enabled': False, u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme9/bg.gif', u'name': u'Jim Fingal', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 92, u'screen_name': u'jimfingal', u'notifications': None, u'url': u'http://jimfingal.com', u'created_at': u'Sat Dec 15 13:04:23 +0000 2007', u'contributors_enabled': False, u'time_zone': u'Pacific Time (US & Canada)', u'protected': False, u'default_profile': False, u'is_translator': False}, u'geo': None, u'in_reply_to_user_id_str': u'2929029785', u'possibly_sensitive': False, u'lang': u'fr', u'created_at': u'Thu Dec 18 17:20:25 +0000 2014', u'filter_level': u'medium', u'in_reply_to_status_id_str': None, u'place': None, u'extended_entities': {u'media': [{u'expanded_url': u'http://twitter.com/jimfingal/status/545629672269021185/photo/1', u'display_url': u'pic.twitter.com/Lyk6QhTzko', u'url': u'http://t.co/Lyk6QhTzko', u'media_url_https': u'https://pbs.twimg.com/media/B5J3S3aIIAI_J27.png', u'id_str': u'545629670860136450', u'sizes': {u'large': {u'h': 8, u'resize': u'fit', u'w': 8}, u'small': {u'h': 8, u'resize': u'fit', u'w': 8}, u'medium': {u'h': 8, u'resize': u'fit', u'w': 8}, u'thumb': {u'h': 8, u'resize': u'crop', u'w': 8}}, u'indices': [28, 50], u'type': u'photo', u'id': 545629670860136450, u'media_url': u'http://pbs.twimg.com/media/B5J3S3aIIAI_J27.png'}]}}


        # Msg Image
        self.msg_image_from_self = {u'contributors': None, u'truncated': False, u'text': u'@tinyimagebot message image http://t.co/Lyk6QhTzko', u'in_reply_to_status_id': None, u'id': 545629672269021185, u'favorite_count': 0, u'source': u'<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>', u'retweeted': False, u'coordinates': None, u'timestamp_ms': u'1418923225835', 
                        u'entities': {u'symbols': [], 
                                u'user_mentions': [{
                                                u'id': 2929029785,
                                                 u'indices': [0, 13], 
                                                 u'id_str': u'2929029785', 
                                                 u'screen_name': u'tinyimagebot', 
                                                 u'name': u'Tiny Image Bot'}], 
                                u'hashtags': [{u'indices': [22, 30], u'text': u'tiny'}],
                                u'urls': [], 
                                u'media': [
                                        {u'expanded_url': u'http://twitter.com/jimfingal/status/545629672269021185/photo/1', 
                                        u'display_url': u'pic.twitter.com/Lyk6QhTzko', 
                                        u'url': u'http://t.co/Lyk6QhTzko', 
                                        u'media_url_https': u'https://pbs.twimg.com/media/B5J3S3aIIAI_J27.png', 
                                        u'id_str': u'545629670860136450', 
                                        u'sizes': {u'large': {u'h': 8, u'resize': u'fit', u'w': 8}, 
                                        u'small': {u'h': 8, u'resize': u'fit', u'w': 8}, 
                                        u'medium': {u'h': 8, u'resize': u'fit', u'w': 8}, 
                                        u'thumb': {u'h': 8, u'resize': u'crop', u'w': 8}}, 
                                        u'indices': [28, 50], 
                                        u'type': u'photo', 
                                        u'id': 545629670860136450, 
                                        u'media_url': u'http://pbs.twimg.com/media/B5J3S3aIIAI_J27.png'}]}, 
                                u'in_reply_to_screen_name': u'tinyimagebot', u'id_str': u'545629672269021185', u'retweet_count': 0, u'in_reply_to_user_id': 2929029785, u'favorited': False, 
                                u'user': {u'follow_request_sent': None, u'profile_use_background_image': True, u'default_profile_image': False, u'id': 11194772, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme9/bg.gif', u'verified': False, u'profile_location': None, u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/474958498023755777/ab-d_9F1_normal.jpeg', u'profile_sidebar_fill_color': u'252429', u'profile_text_color': u'666666', u'followers_count': 171, u'profile_sidebar_border_color': u'181A1E', u'id_str': u'11194772', u'profile_background_color': u'1A1B1F', u'listed_count': 9, u'is_translation_enabled': False, u'utc_offset': -28800, u'statuses_count': 95, u'description': u'As it is in the Void, so it is under my skin.', u'friends_count': 154, u'location': u'Los Angeles, CA', u'profile_link_color': u'2FC2EF', u'profile_image_url': u'http://pbs.twimg.com/profile_images/474958498023755777/ab-d_9F1_normal.jpeg', u'following': None, u'geo_enabled': False, u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme9/bg.gif', u'name': u'Jim Fingal', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 92, 
                                u'screen_name': u'tinyimagebot', u'notifications': None, u'url': u'http://jimfingal.com', u'created_at': u'Sat Dec 15 13:04:23 +0000 2007', u'contributors_enabled': False, u'time_zone': u'Pacific Time (US & Canada)', u'protected': False, u'default_profile': False, u'is_translator': False}, u'geo': None, u'in_reply_to_user_id_str': u'2929029785', u'possibly_sensitive': False, u'lang': u'fr', u'created_at': u'Thu Dec 18 17:20:25 +0000 2014', u'filter_level': u'medium', u'in_reply_to_status_id_str': None, u'place': None, u'extended_entities': {u'media': [{u'expanded_url': u'http://twitter.com/jimfingal/status/545629672269021185/photo/1', u'display_url': u'pic.twitter.com/Lyk6QhTzko', u'url': u'http://t.co/Lyk6QhTzko', u'media_url_https': u'https://pbs.twimg.com/media/B5J3S3aIIAI_J27.png', u'id_str': u'545629670860136450', u'sizes': {u'large': {u'h': 8, u'resize': u'fit', u'w': 8}, u'small': {u'h': 8, u'resize': u'fit', u'w': 8}, u'medium': {u'h': 8, u'resize': u'fit', u'w': 8}, u'thumb': {u'h': 8, u'resize': u'crop', u'w': 8}}, u'indices': [28, 50], u'type': u'photo', u'id': 545629670860136450, u'media_url': u'http://pbs.twimg.com/media/B5J3S3aIIAI_J27.png'}]}}

    def test_dont_process_self(self):
        status = SimpleTweet(self.msg_image_from_self)
        self.assertFalse(image_processor.should_process_image(status))

    def test_dont_process_no_img(self):
        status = SimpleTweet(self.msg_no_img)
        self.assertFalse(image_processor.should_process_image(status))

    def test_do_process_img(self):
        status = SimpleTweet(self.msg_image)
        self.assertTrue(image_processor.should_process_image(status))


class MockStatus(object):

    def __init__(self, hashtag=None, screen_name=None):
        self.hashtags = set([hashtag])
        self.sender_screen_name = screen_name


class TestMessageGeneration(unittest2.TestCase):

    def test_default_image_name(self):

        status = MockStatus()
        size_name, size = image_processor.get_image_size(status)
        self.assertEqual(size_name, 'tiny')

    def test_default_image_size(self):

        status = MockStatus()
        size_name, size = image_processor.get_image_size(status)
        self.assertEqual(size, 50)

    def test_image_size(self):
        status = MockStatus(hashtag='verytiny')
        size_name, size = image_processor.get_image_size(status)
        self.assertEqual(size_name, 'verytiny')

    def test_hashtag_message(self):
        status = MockStatus(hashtag='verytiny')
        msg = image_processor.get_hashtag_message(status)
        self.assertEqual(msg, '#verytiny')

    def test_get_base_message(self):

        status = MockStatus(screen_name='testname')
        msg = image_processor.get_base_message(status)
        self.assertEqual(msg, ".@testname Your tiny image is ready")

    def test_get_message(self):
        status = MockStatus(hashtag='verytiny', screen_name='testname')
        msg = image_processor.get_message(status)
        self.assertEqual(msg, ".@testname Your tiny image is ready: #verytiny")

if __name__ == '__main__':
    unittest2.main()