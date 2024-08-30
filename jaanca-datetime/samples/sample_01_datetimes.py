from jaanca_datetime import DateTimeHelper, App,TimeZonesPytz

if __name__=="__main__":
    # DateTimeHelper.print_console_timezones_pytz()
    print(f"date now: {DateTimeHelper.get_datetime_now(App.Time.POSTGRESQL_FORMAT_DATE,is_format_string=False)}")
    print(f"date timezone convert UTC to Bogotá: {DateTimeHelper.get_datetime_now_to_another_location(App.Time.STANDARD_FORMAT_DATE,TimeZonesPytz.US.AZURE_DEFAULT,TimeZonesPytz.America.BOGOTA)}")

    datetime_data="2024-08-22 14:02:02"
    datetime_format=App.Time.STANDARD_FORMAT_DATE
    is_valid_format=DateTimeHelper.is_valid_datetime_format(datetime_data,datetime_format)
    print(f"datetime_data[{datetime_format}]:[{datetime_data}]: is_valid_format={is_valid_format}")

    datetime_data="2024-08-22"
    datetime_format="%Y-%m-%d"
    is_valid_format=DateTimeHelper.is_valid_datetime_format(datetime_data,datetime_format)
    print(f"datetime_data[{datetime_format}]:[{datetime_data}]: is_valid_format={is_valid_format}")

    datetime_data="2024-08-22"
    datetime_format=App.Time.STANDARD_FORMAT_DATE
    is_valid_format=DateTimeHelper.is_valid_datetime_format(datetime_data,datetime_format)
    print(f"datetime_data[{datetime_format}]:[{datetime_data}]: is_valid_format={is_valid_format}")

# output
# date now: 2024-07-09 12:31:29.366428
# date timezone convert UTC to Bogotá: 2024-07-09 07:31:29
# datetime_data[%Y-%m-%d %H:%M:%S]:[2024-08-22 14:02:02]: is_valid_format=True
# datetime_data[%Y-%m-%d]:[2024-08-22]: is_valid_format=True
# datetime_data[%Y-%m-%d %H:%M:%S]:[2024-08-22]: is_valid_format=False