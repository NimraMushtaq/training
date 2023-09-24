import argparse
import csv
from collections import defaultdict, namedtuple
from datetime import datetime
from enum import Enum
import os

WeatherRecord = namedtuple(
    'WeatherRecord', ['max_temp', 'min_temp', 'max_humidity', 'min_humidity', 'hottest_day']
)


class Report(Enum):
    MIN_MAX = 1
    HOTTEST_DAY = 2


def process_weather_data(weather_data_dir):
    """
    Process weather data from CSV files in the specified directory.

    Parameters:
        - weather_data_dir (str): Path to the directory containing weather data files.

    Returns:
        - yearly_weather_data (default-dict): A default-dict containing processed weather data for each year.
          The keys are years, and the values are WeatherRecord namedtuple containing:
            - max_temp (int): Maximum temperature recorded for the year.
            - min_temp (int): Minimum temperature recorded for the year.
            - max_humidity (int): Maximum humidity recorded for the year.
            - min_humidity (int): Minimum humidity recorded for the year.
            - hottest_day (str): Date of the hottest day for the year.
    """
    yearly_weather_data = defaultdict(
        lambda: WeatherRecord(float('-inf'), float('inf'), 0, 100, None)
    )

    for monthly_weather_data_file in os.listdir(weather_data_dir):
        data_path = os.path.join(weather_data_dir, monthly_weather_data_file)
        process_monthly_weather_data(data_path, yearly_weather_data)

    return yearly_weather_data


def process_monthly_weather_data(weather_data_file_path, yearly_weather_data):
    """
    Process weather data from a single CSV file and update the yearly_weather_data dictionary.

    Parameters:
        - weather_data_file_path (str): Path to the CSV file containing monthly weather data.
        - yearly_weather_data (defaultdict): A defaultdict containing processed weather data for each year.
          The keys are years, and the values are WeatherRecord namedtuple containing:
            - max_temp (int): Maximum temperature recorded for the year.
            - min_temp (int): Minimum temperature recorded for the year.
            - max_humidity (int): Maximum humidity recorded for the year.
            - min_humidity (int): Minimum humidity recorded for the year.
            - hottest_day (str): Date of the hottest day for the year.
    """
    with open(weather_data_file_path, 'r') as monthly_weather_data_file:
        csv_reader = csv.reader(monthly_weather_data_file)
        next(csv_reader)
        next(csv_reader)

        first_line = next(csv_reader)
        year = int(first_line[0].split('-')[0])

        for daily_weather_data in csv_reader:
            if len(daily_weather_data) > 1 and daily_weather_data[1] != '':
                yearly_weather_data[year] = update_annual_weather_record(
                    yearly_weather_data[year], int(daily_weather_data[1]), int(daily_weather_data[3]),
                    int(daily_weather_data[7]), int(daily_weather_data[9]), daily_weather_data[0]
                )


def update_annual_weather_record(annual_weather_record, new_max_temp, new_min_temp, new_max_humidity, new_min_humidity, date):
    """
    Update a WeatherRecord with new temperature and humidity values if they are higher or lower.

    Parameters:
        - annual_weather_record (WeatherRecord): The current WeatherRecord to be updated for the year.
        - new_max_temp (int): New maximum temperature value.
        - new_min_temp (int): New minimum temperature value.
        - new_max_humidity (int): New maximum humidity value.
        - new_min_humidity (int): New minimum humidity value.
        - date (str): Date associated with the weather data.

    Returns:
        - updated_annual_weather_record (WeatherRecord): The updated WeatherRecord with new values if they are higher or lower.
    """
    if new_max_temp > annual_weather_record.max_temp:
        annual_weather_record = annual_weather_record._replace(max_temp=new_max_temp, hottest_day=date)

    if new_min_temp < annual_weather_record.min_temp:
        annual_weather_record = annual_weather_record._replace(min_temp=new_min_temp)

    if new_max_humidity > annual_weather_record.max_humidity:
        annual_weather_record = annual_weather_record._replace(max_humidity=new_max_humidity)

    if new_min_humidity < annual_weather_record.min_humidity:
        annual_weather_record = annual_weather_record._replace(min_humidity=new_min_humidity)

    return annual_weather_record


def generate_min_max_report(report_data):
    """
    Generate and print the Annual Max/Min Temperature and Humidity Report based on the provided data.

    Parameters:
        - report_data (defaultdict): Processed weather data for each year.
          The keys are years, and the values are WeatherRecord namedtuple containing:
            - max_temp (int): Maximum temperature recorded for the year.
            - min_temp (int): Minimum temperature recorded for the year.
            - max_humidity (int): Maximum humidity recorded for the year.
            - min_humidity (int): Minimum humidity recorded for the year.
            - hottest_day (str): Date of the hottest day for the year.
    """
    print('Annual Max/Min Temperature and Humidity Report')
    print(f'{"Year":<10} {"MAX Temp":<12} {"MIN Temp":<12} {"MAX Humidity":<18} {"MIN Humidity"}')
    print('-' * 70)

    for year, (max_temp, min_temp, max_humidity, min_humidity, _) in sorted(report_data.items()):
        print(f'{year:<10} {max_temp:<12} {min_temp:<12} {max_humidity:<18} {min_humidity}')


def generate_hottest_day_report(report_data):
    """
    Generate and print the Hottest Days Report for the range of years based on the provided data.

    Parameters:
        - report_data (defaultdict): Processed weather data for each year.
          The keys are years, and the values are WeatherRecord namedtuple containing:
            - max_temp (int): Maximum temperature recorded for the year.
            - min_temp (int): Minimum temperature recorded for the year.
            - max_humidity (int): Maximum humidity recorded for the year.
            - min_humidity (int): Minimum humidity recorded for the year.
            - hottest_day (str): Date of the hottest day for the year.
    """
    print('Hottest days for the range of years')
    print(f'{"Year":<10} {"Date":<12} {"Temp"}')
    print('-' * 30)

    for year, (max_temp, _, _, _, hottest_day) in sorted(report_data.items()):
        date = datetime.strptime(hottest_day, '%Y-%m-%d').strftime('%d/%m/%Y')
        print(f'{year:<10} {date:<12} {max_temp}')


def validate_input_directory(directory):
    """
     Validate the input directory to ensure it exists and contains files.
     This function checks whether the provided directory path exists and is a valid directory,
     and also verifies if the directory is not empty.

     Parameters:
         directory (str): The path to the directory to be validated.

     Returns:
         directory (str): The validated directory path.

     Raises:
         argparse.ArgumentTypeError: If the directory is not a valid directory or is empty.
     """
    if not os.path.isdir(directory) or not any(os.scandir(directory)):
        raise argparse.ArgumentTypeError(f'{directory} is not a valid directory or is empty.')
    return directory


def main():
    parser = argparse.ArgumentParser(description='Generate weather reports')
    parser.add_argument('report_number', type=int, choices=[report.value for report in Report], help='Report number: 1 or 2')
    parser.add_argument('weather_data_dir', type=validate_input_directory, help='Directory containing weather data files')
    args = parser.parse_args()

    if args.report_number == Report.MIN_MAX.value:
        generate_min_max_report(process_weather_data(args.weather_data_dir))
    elif args.report_number == Report.HOTTEST_DAY.value:
        generate_hottest_day_report(process_weather_data(args.weather_data_dir))


if __name__ == '__main__':
    main()
