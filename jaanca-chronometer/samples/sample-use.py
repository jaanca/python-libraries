from jaanca_chronometer import Chronometer
import time

if __name__=="__main__":
    chronometer=Chronometer()

    chronometer.start()
    time.sleep(1)
    chronometer.stop()
    elapsed_time=str(chronometer.get_elapsed_time())
    print(elapsed_time)

    chronometer.start()
    time.sleep(2)
    chronometer.stop()
    elapsed_time=str(chronometer.get_elapsed_time())
    print(elapsed_time)

    chronometer.start()
    time.sleep(3)
    chronometer.stop()
    elapsed_time=str(chronometer.get_elapsed_time())