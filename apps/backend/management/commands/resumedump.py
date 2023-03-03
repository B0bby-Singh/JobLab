from ntpath import join
from django.core import management
from django.conf import settings
from apps.backend.models import Resume
from apps.common.utils import DictReader
from tqdm import tqdm


class Command(management.BaseCommand):
    help = 'Create Job Scrapped Enteries'

    def handle(self, *args, **kwargs):
        file_name = 'media/resume_data.csv'
        with open(file_name, newline='', mode='r', encoding='UTF-8-sig') as csv_file:
            reader = DictReader(csv_file)
            self.load_resume_from_reader(reader)


    def load_resume_from_reader(self, reader):
        _resumes = list()
        for row in tqdm(reader, desc="resumes"):
            resume = Resume(
                file_name=row['file_name'],
                text=row['text'],

            )
            _resumes.append(resume)
        Resume.objects.bulk_create(_resumes)        

        print("Import completed.")
    
    
      
