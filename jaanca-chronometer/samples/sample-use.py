from datetime import timedelta
from jaanca_chronometer import Chronometer
import time

if __name__=="__main__":
    chronometer=Chronometer()

    print(f"date_time format or interval format: {chronometer.get_format_time()}")

    chronometer.start()
    time.sleep(1)
    chronometer.stop()
    elapsed_time=str(chronometer.get_elapsed_time())
    print(f"type[str]:{elapsed_time}")

    chronometer.start()
    time.sleep(2)
    chronometer.stop()
    elapsed_time=str(chronometer.get_elapsed_time())
    print(f"type[str]:{elapsed_time}")

    chronometer.start()
    time.sleep(3)
    chronometer.stop()
    elapsed_time:timedelta=chronometer.get_elapsed_time(interval_format=False)
    print(f"type[timedelta] to insert into databases like PostgreSQL:{elapsed_time}")
    print(f"timedelta[seconds]:{elapsed_time.seconds}")
    