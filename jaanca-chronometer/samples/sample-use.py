from datetime import timedelta
from jaanca_chronometer import Chronometer, Interval
import time

SEPARATOR="===================================="

if __name__=="__main__":
    chronometer=Chronometer()

    print(SEPARATOR)
    print(f"date_time format or interval format: {chronometer.get_format_time()}")

    print(SEPARATOR)
    print("Sample 1")
    chronometer.start()
    time.sleep(1)
    chronometer.stop()
    elapsed_time:Interval=chronometer.get_elapsed_time()
    print(f"type[{type(elapsed_time)}] : {elapsed_time}")
    print(SEPARATOR)
    print("Sample 2")
    elapsed_time:timedelta=chronometer.get_elapsed_time(interval_format=False)
    print(f"type[{type(elapsed_time)}] to insert into databases like PostgreSQL: {elapsed_time}")
    print(f"elapsed_time.seconds]:{elapsed_time.seconds}")
    
    print(SEPARATOR)
    print("Sample 3")
    parse_elapsed_time = Chronometer.parse_elapsed_time("20:3:35")
    print(f"type[{type(parse_elapsed_time)}] : {parse_elapsed_time}")

    print(SEPARATOR)
    print("Sample 4")
    parse_elapsed_time = Chronometer.parse_elapsed_time("1:1")
    print(f"type[{type(parse_elapsed_time)}] : {parse_elapsed_time}")

    print(SEPARATOR)
    print('Sample 5: "2:3:4"+"3:3:2"')
    sum_elapsed_times = Chronometer.sum_elapsed_times("2:3:4","3:3:2")
    print(f"type[{type(sum_elapsed_times)}] : {sum_elapsed_times}")
