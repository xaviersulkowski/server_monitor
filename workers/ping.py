import subprocess

from .worker_facory import Worker


class Ping(Worker):
    def __init__(self, threshold, directory):
        super(Ping, self).__init__(threshold, directory)

    def _getinfo(self):

        df = subprocess.Popen(["ping", self.directory, '-c', '1'], stdout=subprocess.PIPE)
        received = False
        for i in df.stdout:
            sline = i.decode().split(',')
            if ' 1 received' in sline:
                received = True

        return received

    def check(self):

        package_received = self._getinfo()
        network_error_status = False
        msg = ''

        if package_received is True:
            network_error_status = True
            msg += 'Network problems'
        else:
            pass

        return [network_error_status, msg]
