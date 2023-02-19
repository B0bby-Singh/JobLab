from ntpath import join
from django.core import management
from django.conf import settings
from apps.backend.models import JobScraped
from apps.common.utils import DictReader
from tqdm import tqdm


class Command(management.BaseCommand):
    help = 'Create Job Scrapped Enteries'

    def handle(self, *args, **kwargs):
        file_name = 'media/Jobs.csv'
        with open(file_name, newline='', mode='r', encoding='UTF-8-sig') as csv_file:
            reader = DictReader(csv_file)
            self.load_job_from_reader(reader)


    def load_job_from_reader(self, reader):
        _jobs = list()
        for row in tqdm(reader, desc="jobs"):
            job = JobScraped(
                title=row['title'],
                company=row['company'],
                description=row['description'],
                announcement=row['announcement']

            )
            _jobs.append(job)
        JobScraped.objects.bulk_create(_jobs)        

        print("Import completed.")
    
    
      
