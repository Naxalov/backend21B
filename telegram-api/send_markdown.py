import requests
import json
from pprint import pprint
import os

token =os.environ['TOKEN'] 
def sendMsg(idx,text):
    url = f'https://api.telegram.org/bot{token}/sendMessage'

    payload = {
    'chat_id':idx,
    'text':text,
    'parse_mode':'HTML'
    }
    r = requests.get(url,params=payload)


# 86775091

link = '[Channel](https://t.me/codeschooluz)'
html = """

<b>bold</b>, <strong>bold</strong>
<i>italic</i>, <em>italic</em>
<u>underline</u>, <ins>underline</ins>
<s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>
<b>bold <i>italic bold <s>italic bold strikethrough</s> <u>underline italic bold</u></i> bold</b>
<a href="http://www.example.com/">inline URL</a>
<a href="tg://user?id=123456789">inline mention of a user</a>
<code>inline fixed-width code</code>
<pre>pre-formatted fixed-width code block</pre>
<pre><code class="language-python">pre-formatted fixed-width code block written in the Python programming language</code></pre>

"""


sendMsg(86775091,html)

