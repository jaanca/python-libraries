from jaanca_datetime import DateTimeHelper

filename=DateTimeHelper.get_filename_datetime_hash("report",".log")
print(filename)

# Output: <name_YYYYMMDD_HHmmss>_<int_range><extension>
# report_20240712_150958_50012.log