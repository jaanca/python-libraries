<p align="center">
    <em>jaanca public libraries</em>
</p>

<p align="center">
<a href="https://pypi.org/project/jaanca-chronometer" target="_blank">
    <img src="https://img.shields.io/pypi/v/jaanca-chronometer?color=blue&label=PyPI%20Package" alt="Package version">
</a>
<a href="(https://www.python.org" target="_blank">
    <img src="https://img.shields.io/badge/Python-%5B%3E%3D3.8%2C%3C%3D3.11%5D-blue" alt="Python">
</a>
</p>


---

#  A tool library created by jaanca

* **Python library**: A tool library created by jaanca that allows measuring the time between two moments in the source code.
* **Analyze results in database**: The output format can be inserted in an INTERVAL attribute for example in PostgreSQL and add the time of several processes.

[Source code](https://github.com/jaanca/python-libraries/tree/main/jaanca-chronometer)
| [Package (PyPI)](https://pypi.org/project/jaanca-chronometer/)
| [Samples](https://github.com/jaanca/python-libraries/tree/main/jaanca-chronometer/samples)

---

# library installation
```console
pip install jaanca-chronometer --upgrade
```

---
# Example of use

```python
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
    
    parse_elapsed_time = Chronometer.parse_elapsed_time("20:3:35")
    print(f"parse_elapsed_time[20:3:35]:{parse_elapsed_time}")

    parse_elapsed_time = Chronometer.parse_elapsed_time("1:1")
    print(f"parse_elapsed_time[1:1]:{parse_elapsed_time}")
    
```

---
# Example of inserting elapsed time into PostgreSQL and totaling the results

```sql
CREATE TABLE process_execution (
    id SERIAL PRIMARY KEY,
    description VARCHAR(100),
    time INTERVAL
);

INSERT INTO process_execution (description,time) VALUES ('process_simulator','01:30:00'::interval);
INSERT INTO process_execution (description,time) VALUES ('process_simulator','02:15:00'::interval);
INSERT INTO process_execution (description,time) VALUES ('process_simulator','00:45:00'::interval);
INSERT INTO process_execution (description,time) VALUES ('process_simulator','99:45:00'::interval);

SELECT SUM(time) FROM process_execution WHERE description = 'process_simulator';

-- Result:104:15:00

```

---

# Semantic Versioning

jaanca-chronometer < MAJOR >.< MINOR >.< PATCH >

* **MAJOR**: version when you make incompatible API changes
* **MINOR**: version when you add functionality in a backwards compatible manner
* **PATCH**: version when you make backwards compatible bug fixes

## Definitions for releasing versions
* https://peps.python.org/pep-0440/

    - X.YaN (Alpha release): Identify and fix early-stage bugs. Not suitable for production use.
    - X.YbN (Beta release): Stabilize and refine features. Address reported bugs. Prepare for official release.
    - X.YrcN (Release candidate): Final version before official release. Assumes all major features are complete and stable. Recommended for testing in non-critical environments.
    - X.Y (Final release/Stable/Production): Completed, stable version ready for use in production. Full release for public use.
---

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Types of changes

- Added for new features.
- Changed for changes in existing functionality.
- Deprecated for soon-to-be removed features.
- Removed for now removed features.
- Fixed for any bug fixes.
- Security in case of vulnerabilities.

## [0.0.1rcX] - 2024-05-21
### Added
- First tests using pypi.org in develop environment.

## [0.1.X] - 2024-05-21
### Added
- Completion of testing and launch into production.

## [0.1.3] - 2024-05-23
### Changed
- Documentation improvements.

## [0.1.4] - 2024-06-20
### Changed
- It is added to the get_elapsed_time function to return the elapsed time in timedelta format, which is accepted to insert the record into a database engine such as PostgreSQL.

## [0.1.5] - 2024-06-20
### Added
- New parse_elapsed_time functionality to convert str to timedelta.

## [0.1.6] - 2024-07-11
### Added
- New sum_elapsed_times functionality to takes two times in HH:mm format, converts them to seconds, adds them and converts the result back to HH:mm.