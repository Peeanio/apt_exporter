# apt_exporter

This project exports stats about apt packages and the state of the cache on system.

Values will be similar to:
```
# HELP apt_installed_packages_count Number of installed apt packages
# TYPE apt_installed_packages_count gauge
apt_installed_packages_count 582.0
# HELP apt_outdated_packages_count Number of outdated apt packages
# TYPE apt_outdated_packages_count gauge
apt_outdated_packages_count 1.0
# HELP apt_outdated_packages_status_info Key value of package:status
# TYPE apt_outdated_packages_status_info gauge
apt_outdated_packages_status_info{adduser="current",...} 1.0

```

but tweaks coming in.

## Running
1. Install dependencies
   ```
    pip3 install prometheus_client
   ```
2. Run server
   ```
   python3 apt_exporter.py
   ```
