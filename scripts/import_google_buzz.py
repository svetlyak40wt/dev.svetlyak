#!env/bin/python

import re
import sys
import simplejson
import os.path
import urllib
import codecs

from html2text import html2text
from functools import partial

_START_URL = 'https://www.googleapis.com/buzz/v1/activities/%s/@self?alt=json'
_OUTPUT_DIR = 'content/buzz'

_remove_empty_lines = partial(re.sub, r'\n{2,}', '\n\n')

def _save_item(item):
    source = item['source']['title']
    if source == 'Buzz':
        title = ' '.join(item['title'].split('\n'))
        type_ = item['object']['type']
        if type_ == 'note':
            obj = item['object']
            content = _remove_empty_lines(html2text(obj['content']))

            for attach in obj.get('attachments', []):
                if attach['type'] == 'photo':
                    content += '\n' + '![](%s)' % attach['links']['enclosure'][0]['href']
                else:
                    content += '\n' + '[%s](%s)' % (attach['title'], attach['links']['alternate'][0]['href'])

            date = item['updated']
            date = date[:16].replace('T', ' ')
            slug = item['updated'][:-5].replace('T', '-').replace(':', '-')

            filename = os.path.join(_OUTPUT_DIR, slug + '.md')
            with codecs.open(filename, 'w', 'utf-8') as f:
                print 'Saving "%s"' % filename
                f.write("""Title: %(title)s
Slug: %(slug)s
Date: %(date)s
Category: buzz
Lang: ru

%(content)s""" % locals())




def import_posts(username):
    if not os.path.exists(_OUTPUT_DIR):
        os.makedirs(_OUTPUT_DIR)

    prev_next = None
    next = _START_URL % username
    while next and next != prev_next:
        print next
        response = urllib.urlopen(next).read()
        json = simplejson.loads(response)

        items = json['data']['items']
        if not items:
            break

        for item in items:
            _save_item(item)

        # To avoid infinite loop, we should compare the new url with
        # the previous one.
        prev_next = next
        next = json['data']['links'].get('next', [{'href': ''}])[0]['href']


if __name__ == '__main__':
    import_posts(sys.argv[1])
