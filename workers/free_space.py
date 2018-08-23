import subprocess

from .abstract_worker import Worker


class FreeSpace(Worker):
    def __init__(self, threshold, directory):
        super(FreeSpace, self).__init__(threshold, directory)

    def _getinfo(self):

        df = subprocess.Popen(["df","-h", self.directory], stdout=subprocess.PIPE)
        space = {}
        for i in df.stdout:
            sline = i.decode().split()
            space['total'] = sline[1][:-1]
            space['used'] = sline[2][:-1]
            space['free'] = sline[3][:-1]

        for key in space.keys():
            space[key] = int(space[key]) * 1024 * 1024

        return space

    def check(self):

        space = self._getinfo()
        threshold = self.threshold

        if threshold >= space['total']:
            threshold = int(0.8 * space['total'])
            UserWarning('Threshold is bigger than total space. Threshold is set to 80% of total space')

        overload_status = False
        msg = ''

        if space['free'] >= threshold:
            overload_status = True
            msg += 'Space in directory {} is dangerously close to limit: ' \
                   'server uses {}B of {}B that\'s {}%'.format(self.directory,
                                                               space['used'],
                                                               space['total'],
                                                               (space['used']/space['total'])*100)
        else:
            pass

        return [overload_status, msg]