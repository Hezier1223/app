# Created by Max on 1/29/18
from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'toutiao'])
# execute(['scrapy', 'crawl', 'article'])
