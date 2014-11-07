# Beacon Distance Calculator
# Copyright 2014 Geono Kim
# Licensed under the Apache License, Version 2.0 (the "License");

from distance import Distance


class CurveFittedDistanceCalculator(Distance):
    TAG = "CurveFittedDistanceCalculator"

    def __init__(self, coefficient1, coefficient2, coefficient3):
        self.coefficient1 = coefficient1
        self.coefficient2 = coefficient2
        self.coefficient3 = coefficient3
        print('coefficient1 : ' + str(self.coefficient1))
        print('coefficient2 : ' + str(self.coefficient2))
        print('coefficient3 : ' + str(self.coefficient3))

    # Calculated the estimated distance in meters to the beacon
    # based on a reference rssi at 1m
    # and the known actual rssi at the current location
    #
    # @params txPower rssi
    # @return estimated distance

    def calculate_distance(self, tx_power, rssi):
        if rssi == 0:
            return -1.0
        ratio = rssi*1.0/tx_power
        if ratio < 1.0:
            distance = ratio ** 10
        else:
            distance = self.coefficient1 * (ratio ** self.coefficient2) + \
                self.coefficient3
            return distance
