# Beacon Distance Calculator
# Copyright 2014 Geono Kim
# Licensed under the Apache License, Version 2.0 (the "License");

from abc import ABCMeta, abstractmethod


class Distance(object):
    __metaclass__ = ABCMeta

    coefficient1 = float(0)
    coefficient2 = float(0)
    coefficient3 = float(0)

    @abstractmethod
    def calculate_distance(tx_power, rssi):
        pass
