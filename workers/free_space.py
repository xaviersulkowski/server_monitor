import os
import subprocess

from .abstract_worker import Worker


class FreeSpace(Worker):
    def __init__(self, threshold, directory):
        super(FreeSpace, self).__init__(threshold, directory)

    def _getinfo(self):

        out, err = subprocess.Popen(["df","-h", self.directory],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE).communicate()

        space = {}

        if out != b'':
            out = out.decode()
            out = out.splitlines()
            sline = out[1].split()

            space['total'] = sline[1][:-1]
            space['used'] = sline[2][:-1]
            space['free'] = sline[3][:-1]

            for key in space.keys():
                space[key] = int(space[key]) * 1024 * 1024

            return space

        elif err != b'':
            msg = 'No such a directory {}. '.format(self.directory)
            return msg
        else:
            pass

    def check(self):

        space = self._getinfo()
        threshold = self.threshold

        overload_status = False
        msg = ''

        if type(space) is dict:
            if threshold >= space['total']:
                threshold = int(0.8 * space['total'])
                UserWarning('Threshold is bigger than total space. Threshold is set to 80% of total space')

            if space['free'] >= threshold:
                overload_status = True
                msg += 'Space in directory {} is dangerously close to limit: ' \
                       'server uses {}B of {}B that\'s {}%. '.format(self.directory,
                                                                     space['used'],
                                                                     space['total'],
                                                                     int((space['used'] / space['total']) * 100))
        else:
            overload_status = True
            msg += space

        return [overload_status, msg]