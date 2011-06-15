import pelican

DEFAULT_MAX_FEED_LEN = 20

class Writer(pelican.writers.Writer):
    def write_feed(self, elements, *args, **kwargs):
        # Limit all atom feeds
        max_feed_len = self.settings.get('MAX_FEED_LEN', DEFAULT_MAX_FEED_LEN)
        return super(Writer, self).write_feed(elements[:max_feed_len], *args, **kwargs)

    def _add_item_to_the_feed(self, feed, item):
        feed.add_item(
            title = item.title,
            link = '%s/%s' % (self.site_url, item.url),
            unique_id  =  self.site_url + '/' + item.url,
            description = item.content,
            categories = item.tags if hasattr(item, 'tags') else None,
            author_name = getattr(item, 'author', 'Anonymous'),
            pubdate = item.date,
        )


class Pelican(pelican.Pelican):
    def get_writer(self):
        return Writer(self.output_path, settings=self.settings)

