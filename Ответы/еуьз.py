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
        return data

    def process(self, write=True):
        data_dict = defaultdict(list)
        data = self._get_data()

        for element in data:
            processed_data = []
            for key, value in element.items():
                for v in value:
                    if v >= self.smallest and v % self.not_mult != 0:
                        data_dict[key].append(v)
                key_min = min(data_dict[key])
                key_max = max(data_dict[key])
                key_average = round((sum(data_dict[key]) / len(data_dict[key])), 2)
                key_sum = sum(data_dict[key])
                processed_data.append(f'{key};{key_max};{key_min};{key_average};{key_sum}')

        if write:
            self._write_to_file(sorted(processed_data))

        return sorted(processed_data)

    @staticmethod
    def _write_to_file(data):
        with open('truth.csv', 'w') as f:
            f.writelines(data)


acquired_data = DataParser(args.host, args.port, args.smallest, args.not_mult)
acquired_data.process()
