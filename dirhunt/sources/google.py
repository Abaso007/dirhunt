from dirhunt.sources.base import Source
from dirhunt._compat import URLError
from googlesearch import search

STOP_AFTER = 20


class Google(Source):
    def callback(self, domain):
        results = search(f'site:{domain}', stop=STOP_AFTER)
        while True:
            try:
                url = next(results)
            except (IOError, URLError) as e:
                self.add_error(f'Error on Google Source: {e}')
                break
            except StopIteration:
                break
            else:
                self.add_result(url)
