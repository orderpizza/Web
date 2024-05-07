import os
from django.core.management.base import BaseCommand
from django.db import transaction
from django.conf import settings
from webs.models import MovieClip

class Command(BaseCommand):
    help = 'Populate database with metadata from a text file'

    def handle(self, *args, **options):
        # Construct the path to your metadata text file
        metadata_file_path = os.path.join(settings.BASE_DIR, 'metadata.txt')

        try:
            # Open the metadata file
            with open(metadata_file_path, 'r', encoding='utf-8') as file:
                # Start a database transaction
                with transaction.atomic():
                    # Iterate over each line in the file
                    for line in file:
                        try:
                            # Split the line into filename, start_time, end_time, and korean_sentence
                            filename, start_time, end_time, korean_sentence = line.strip().split('\t')
                            # Create a MovieClip instance and save it to the database
                            MovieClip.objects.create(
                                filename=filename,
                                start_time=start_time,
                                end_time=end_time,
                                korean_sentence=korean_sentence
                            )
                        except ValueError:
                            self.stderr.write(self.style.ERROR(f'Invalid line: {line.strip()}'))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR('Metadata file not found.'))
            return

        self.stdout.write(self.style.SUCCESS('Database populated successfully'))
