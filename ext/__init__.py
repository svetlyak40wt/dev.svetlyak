import pelican

class Writer(pelican.writers.Writer):
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
        return Writer(self.output_path)

