from jaanca_datetime import DateTimeHelper, App, TimeZonesPytz

if __name__=="__main__":
    DateTimeHelper.print_console_timezones_pytz()
    print(f"date now,is_format_string=False=datetime format: {DateTimeHelper.get_datetime_now(App.Time.POSTGRESQL_FORMAT_DATE,is_format_string=False)}")
    print(f"date now,is_format_string=True: {DateTimeHelper.get_datetime_now(App.Time.POSTGRESQL_FORMAT_DATE,is_format_string=True)}")
    print(f"date timezone convert UTC to Bogotá,is_format_string=False=datetime format: {DateTimeHelper.get_datetime_now_to_another_location(App.Time.STANDARD_FORMAT_DATE,TimeZonesPytz.US.AZURE_DEFAULT,TimeZonesPytz.America.BOGOTA,is_format_string=False)}")
    print(f"date timezone convert UTC to Bogotá,is_format_string=True: {DateTimeHelper.get_datetime_now_to_another_location(App.Time.STANDARD_FORMAT_DATE,TimeZonesPytz.US.AZURE_DEFAULT,TimeZonesPytz.America.BOGOTA,is_format_string=True)}")

# #output
# date now,is_format_string=False=datetime format: 2024-05-24 15:03:04.424853
# date now,is_format_string=True: 2024-05-24 15:03:04
# date timezone convert UTC to Bogotá,is_format_string=False=datetime format: 2024-05-24 10:03:04.425853-05:00
# date timezone convert UTC to Bogotá,is_format_string=True: 2024-05-24 10:03:04