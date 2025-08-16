import csv
import re
from django.core.management.base import BaseCommand
from django.db import transaction
from surveillance.models import Disease, District, WeeklySurveillanceData, DistrictCaseData


class Command(BaseCommand):
    help = 'Import cleaned disease surveillance data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='cleaned_disease_surveillance_data.csv',
            help='Path to the CSV file containing surveillance data'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before importing'
        )

    def handle(self, *args, **options):
        csv_file = options['file']
        clear_data = options['clear']

        if clear_data:
            self.stdout.write('Clearing existing surveillance data...')
            WeeklySurveillanceData.objects.all().delete()
            DistrictCaseData.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Existing data cleared.'))

        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                with transaction.atomic():
                    for row in reader:
                        self.process_row(row)
                        
            self.stdout.write(self.style.SUCCESS('Successfully imported surveillance data'))
            
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f'File {csv_file} not found. Please check the file path.')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error importing data: {str(e)}')
            )

    def process_row(self, row):
        """Process a single row of CSV data"""
        try:
            # Extract basic information
            source_file = row['Source_File']
            week_number = int(row['Week_Number'])
            disease_name = row['Disease_Syndrome']
            
            # Get or create disease
            disease, created = Disease.objects.get_or_create(
                name=disease_name,
                defaults={'description': f'Disease surveillance data for {disease_name}'}
            )
            
            if created:
                self.stdout.write(f'Created new disease: {disease_name}')

            # Parse case numbers (handle empty strings and non-numeric values)
            def safe_int(value):
                if not value or value.strip() == '':
                    return None
                try:
                    return int(value)
                except (ValueError, TypeError):
                    return None

            previous_week_cases = safe_int(row['Previous_Week_Cases'])
            current_week_cases = safe_int(row['Current_Week_Cases'])
            change_in_cases = safe_int(row['Change_in_Cases'])
            same_week_last_year = safe_int(row['Same_Week_Last_Year'])
            year_over_year_change = safe_int(row['Year_over_Year_Change'])
            
            trend = row['Trend']
            top_affected_districts = row['Top_Affected_Districts']

            # Create or update surveillance data
            surveillance_data, created = WeeklySurveillanceData.objects.update_or_create(
                week_number=week_number,
                year=2024,  # Assuming 2024 data
                disease=disease,
                defaults={
                    'source_file': source_file,
                    'previous_week_cases': previous_week_cases,
                    'current_week_cases': current_week_cases,
                    'change_in_cases': change_in_cases,
                    'same_week_last_year': same_week_last_year,
                    'year_over_year_change': year_over_year_change,
                    'trend': trend,
                    'top_affected_districts': top_affected_districts,
                }
            )

            if created:
                self.stdout.write(f'Created surveillance data: Week {week_number} - {disease_name}')

            # Process district-specific data
            self.process_district_data(surveillance_data, top_affected_districts)

        except Exception as e:
            self.stdout.write(
                self.style.WARNING(f'Error processing row: {str(e)}')
            )

    def process_district_data(self, surveillance_data, districts_data):
        """Extract and store district-specific case data"""
        if not districts_data or districts_data.strip() == '':
            return

        # Parse district data - format like "KATHMANDU (52), KAILALI (44), PARSA (39)"
        district_pattern = r'([A-Z\s]+)\s*\((\d+)\)'
        matches = re.findall(district_pattern, districts_data)

        for district_name, cases_str in matches:
            district_name = district_name.strip()
            try:
                cases = int(cases_str)
                
                # Get or create district
                district, created = District.objects.get_or_create(
                    name=district_name,
                    defaults={'province': 'Unknown'}  # We can update this later with proper province data
                )
                
                if created:
                    self.stdout.write(f'Created new district: {district_name}')

                # Create district case data
                district_case, created = DistrictCaseData.objects.update_or_create(
                    surveillance_data=surveillance_data,
                    district=district,
                    defaults={'cases': cases}
                )

                if created:
                    self.stdout.write(f'Added case data: {district_name} - {cases} cases')

            except (ValueError, TypeError) as e:
                self.stdout.write(
                    self.style.WARNING(f'Error parsing district data for {district_name}: {str(e)}')
                )
