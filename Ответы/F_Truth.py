import csv

import requests
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser(description='The truth is out there')
parser.add_argument('host', nargs='?', default='127.0.0.1')
parser.add_argument('port', nargs='?', default='5000')
parser.add_argument('--not_mult', default=100)
parser.add_argument('--smallest', default=0)
args = parser.parse_args()


class DataParser:
    def __init__(self, host, port, smallest, not_mult):
        self.host = host
        self.port = port
        self.smallest = int(smallest)
        self.not_mult = int(not_mult)

    def _get_data(self):
        host_url = f'http://{self.host}:{self.port}/data'
        data = requests.get(host_url).json()['data']
        # data = [{"electric": [62, 45, 15, 44, 20], "magnetic": [47, 10, 43, 61], "gravitational": [5, 41, 63, -9, 9, 12]},
        #              {"electric": [1, 82, 56, 48], "magnetic": [-2, 58, 96, 14, 94], "gravitational": [-8, 98, -5]},
        #              {"electric": [68, 81, 40, -2, -8], "magnetic": [74, -12, 67, 54], "gravitational": [85, -6]}]
        return data

    def process(self, write=True):
        result = defaultdict(lambda: [])
        data = self._get_data()
        count = 0
        for element in data:
            count += 1
            for key, value in element.items():
                for v in value:
                    if v < self.smallest or v % self.not_mult == 0:
                        continue
                    result[key].append(v)
                if count != len(element):
                    continue
                result[key] = [key, max(result[key]), min(result[key]), round(sum(result[key]) / len(result[key]), 2),
                               sum(result[key])]

        if write:
            self._write_to_file(result)

        return result

# If newline='' is not specified, newlines embedded inside quoted fields will not be interpreted correctly, and on
# platforms that use \r\n lineendings on write an extra \r will be added. It should always be safe to specify newline='',
# since the csv module does its own (universal) newline handling.
    @staticmethod
    def _write_to_file(data):
        with open('truth.csv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(sorted(data.values()))


acquired_data = DataParser(args.host, args.port, args.smallest, args.not_mult)
acquired_data.process()
