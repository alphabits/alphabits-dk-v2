from __future__ import division
from math import ceil


class Pagination(object):

    def __init__(self, objects_to_paginate, current_page, page_size):
        self.objects_to_paginate = objects_to_paginate
        self.num_objects = len(objects_to_paginate)
        self.num_pages = ceil(self.num_objects/page_size)
        self.page_size = page_size
        self.current_page = current_page
        self.start_index = (current_page - 1)*page_size
        self.end_index = self.start_index + page_size
        self.current_page_exists = (1 <= current_page <= self.num_pages)
        self.current_page_is_first = (current_page == 1)
        self.current_page_is_last = (self.current_page == self.num_pages)
        if self.current_page_exists:
            self.page_objects = objects_to_paginate[self.start_index:self.end_index]
        else:
            self.page_objects = []

