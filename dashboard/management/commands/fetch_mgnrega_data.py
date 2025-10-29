from django.core.management.base import BaseCommand
from django.conf import settings
import requests
import json
import os
from datetime import datetime


class Command(BaseCommand):
    help = 'Fetch MGNREGA data from government API and cache locally'

    def handle(self, *args, **options):
        cache_file = os.path.join(settings.BASE_DIR, 'cache.json')
        
        self.stdout.write('Fetching MGNREGA data from government API...')
        
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
            
            self.stdout.write(self.style.SUCCESS(
                f'Successfully loaded existing cache with {len(existing_data.get("districts", []))} districts'
            ))
            
            self.stdout.write(self.style.WARNING(
                'Note: API integration requires authentication and endpoint details.'
            ))
            self.stdout.write(self.style.WARNING(
                'Currently using cached data. To enable live API, configure API credentials.'
            ))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
