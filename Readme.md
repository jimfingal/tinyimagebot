tinyimagebot
============

Give me images and I will make them tiny.


## Overview

Uses the python image library to process images. 

Runs two processes, one to listen to the user stream and insert candidate tweets into a Redis pub/sub queue, the other to process through tweets with a delay between polls so as not to overrun the obscure and unknown twitter media upload rate limits. 

I also put in some very simple rate limiting per-user, to prevent a bot to bot conversation with another chatty bot that resizes images from taking over the feed.
