import subprocess

from .abstract_worker import Worker


class Ping(Worker):
    def __init__(self, threshold, directory):
        super(Ping, self).__init__(threshold, directory)

    def _getinfo(self):
        out, err = subprocess.Popen(["ping", self.directory, '-c', '1'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE).communicate()
        received = False
        if err != b'':
            msg = err.decode()
            return msg

        if out != b'':
            received = True if ' 1 received' in out.decode() else False
            return received

    def check(self):

        package_received = self._getinfo()
        network_error_status = False
        msg = ''

        if package_received is True:
            pass
        elif package_received is False:
            network_error_status = True
            msg += 'Ups! Network problem: 1 packet transmitted, 0 received. '
        elif type(package_received) != bool:
            network_error_status = True
            msg += package_received

        return [network_error_status, msg]
