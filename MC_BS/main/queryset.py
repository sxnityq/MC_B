from django.db.models import Window, F
from django.db.models.functions import RowNumber

from .models import AlbumElement

def get_correct_preview_album_api_queryset(row_amount=5):
    
    queryset = AlbumElement.objects.select_related('album').annotate(row=Window(
                                                                    expression=RowNumber(),
                                                                    partition_by=F('album')))
    sql, params = queryset.query.sql_with_params()
    products_filtered = AlbumElement.objects.raw("""
        SELECT * FROM ({}) products_with_row_numbers
        WHERE row <= %s
    """.format(sql), [*params, row_amount])
    
    return products_filtered