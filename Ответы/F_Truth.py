import math
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
        # data = requests.get(host_url).json()['data']
        data = [{"electric": [62, 45, 15, 44, 20], "magnetic": [47, 10, 43, 61], "gravitational": [5, 41, 63, -9, 9, 12]},
                     {"electric": [1, 82, 56, 48], "magnetic": [-2, 58, 96, 14, 94], "gravitational": [-8, 98, -5]},
                     {"electric": [68, 81, 40, -2, -8], "magnetic": [74, -12, 67, 54], "gravitational": [85, -6]}]
        return data

    def process(self, write=True):
        result = defaultdict(lambda: {
            'max': -math.inf,
            'min': math.inf,
            'avg': 0,
            'sum': 0,
            'count': 0
        })
        data = self._get_data()
        for element in data:
            for key, value in element.items():
                for v in value:
                    if v < self.smallest or v % self.not_mult == 0:
                        continue
                    result[key]['sum'] += v
                    result[key]['count'] += 1
                    if v < result[key]['min']:
                        result[key]['min'] = v
                    if v > result[key]['max']:
                        result[key]['max'] = v

                result[key]['avg'] = round(result[key]['sum'] / result[key]['count'], 2)

        if write:
            self._write_to_file(result)

        return result

    @staticmethod
    def _write_to_file(data):
        with open('truth.csv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            for key, value in sorted(data.items()):
                value.pop('count')
                writer.writerow([key, *value.values()])


acquired_data = DataParser(args.host, args.port, args.smallest, args.not_mult)
acquired_data.process()
