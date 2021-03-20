import requests
import argparse

parser = argparse.ArgumentParser(description='The truth is out there')
parser.add_argument('host', nargs='?', default='127.0.0.1')
parser.add_argument('port', nargs='?', default='5000')
parser.add_argument('--not_mult', default=100)
parser.add_argument('--smallest', default=0)
args = parser.parse_args()

# url = f'http://{args.host}:{args.port}/data'
#
#
# data = requests.get(url).json()['data']
#
# keys = sorted(list(data[1].keys()))
#
# overall_dict = {}
# processed_data = []
#
#
# for k in enumerate(keys):
#     overall_dict[k[1]] = []
#
#
# for i in enumerate(data):
#     for k in enumerate(keys):
#         for e in i[1][k[1]]:
#             if e >= int(args.smallest) and e % int(args.not_mult) != 0:
#                 overall_dict[k[1]].append(e)
#
#
# for k in enumerate(keys):
#     processed_data.append(f'{k[1]};{max(overall_dict[k[1]])};{min(overall_dict[k[1]])};'
#                           f'{round(sum(overall_dict[k[1]]) / len(overall_dict[k[1]]), 2)};{sum(overall_dict[k[1]])}\n')
#
#
# with open('truth.csv', 'w') as f:
#     f.writelines(processed_data)


class Data:
    def __init__(self, host, port, smallest, not_mult):
        self.host = host
        self.port = port
        self.smallest = int(smallest)
        self.not_mult = int(not_mult)

    def _create_dict(self):
        created_dict = {}
        data = self._get_data()
        keys = sorted(list(data[1].keys()))
        for k in keys:
            created_dict[k] = []

        for i in range(len(data)):
            for k in keys:
                created_dict[k] += data[i][k]

        return created_dict, keys

    def _get_data(self):
        host_url = f'http://{self.host}:{self.port}/data'
        data = requests.get(host_url).json()['data']
        return data

    def process(self, write=True):
        processed_data = []
        overall_dict, keys = self._create_dict()

        for k in keys:
            overall_dict[k] = [e for e in overall_dict[k] if e >= self.smallest and e % self.not_mult != 0]

            processed_data.append(f'{k};'
                                  f'{max(overall_dict[k])};'
                                  f'{min(overall_dict[k])};'
                                  f'{round(sum(overall_dict[k]) / len(overall_dict[k]), 2)};'
                                  f'{sum(overall_dict[k])}\n')

        if write:
            self._write_to_file(processed_data)

        return processed_data

    @staticmethod
    def _write_to_file(data):
        with open('truth.csv', 'w') as f:
            f.writelines(data)


data = Data(args.host, args.port, args.smallest, args.not_mult)
data.process()
