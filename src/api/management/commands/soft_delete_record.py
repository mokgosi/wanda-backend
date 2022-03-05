from django.core.management.base import BaseCommand

from api.models import Testimonial

class Command(BaseCommand):

    def handle(self, *args, **options):
        qs = Testimonial.objects.filter()
        qs1 = Testimonial.all_objects.filter()
        print(qs.query)
        print(qs1.query)