#!/usr/bin/env python
'''
Author: Max Russell
'''
from prometheus_client import start_http_server, Gauge, Info
import apt
import time

installed_packages_gauge = Gauge('apt_installed_packages_count', "Number of installed apt packages")
outdated_packages_gauge = Gauge('apt_outdated_packages_count', "Number of outdated apt packages")
outdated_packaged_info = Info('apt_outdated_packages_status', "Key value of package:status")

def get_metrics():
    installed_count = 0
    outdated_count = 0
    info_dict = {}
    cache = apt.cache.Cache()
    cache.update()
    cache.open
    for pkg in cache.keys():
        package = cache[pkg]
        if package.is_installed:
            installed_count += 1
            if package.is_upgradable:
                outdated_count += 1
                info_dict[package] = "outdated"
            else:
                info_dict[package] = "current"
    installed_packages_gauge.set(installed_count)
    outdated_packages_gauge.set(outdated_count)
    outdated_packaged_info.info(info_dict)

if __name__ == '__main__':
    start_http_server(9000)
    while True:
        get_metrics()
        time.sleep(15)

