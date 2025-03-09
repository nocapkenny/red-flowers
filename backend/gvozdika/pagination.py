from rest_framework import pagination

# class PageNumberPaginationWithCount(pagination.PageNumberPagination):
#     def get_paginated_response(self, data):
#         response = super().get_paginated_response(data)
#         response.data['total_pages'] = self.page.paginator.num_pages
#         return response
class PageNumberPaginationWithCount(pagination.PageNumberPagination):
    page_size = 50 
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        response.data['totalPages'] = self.page.paginator.num_pages  
        return response
