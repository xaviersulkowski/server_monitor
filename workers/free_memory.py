from .abstract_worker import Worker


class FreeMemory(Worker):
    def __init__(self, threshold, directory):
        super(FreeMemory, self).__init__(threshold, directory)

    def _getinfo(self):

        with open(self.directory, 'r') as mem:
            memory = {}
            tmp = 0
            for i in mem:
                sline = i.split()
                if str(sline[0]) == 'MemTotal:':
                    memory['total'] = int(sline[1])
                elif str(sline[0]) in ('MemFree:', 'Buffers:', 'Cached:'):
                    tmp += int(sline[1])
            memory['free'] = tmp
            memory['used'] = int(memory['total']) - int(memory['free'])
        return memory

    def check(self):

        memory = self._getinfo()
        threshold = self.threshold

        if threshold >= memory['total']:
            threshold = int(0.8 * memory['total'])
            UserWarning('Threshold is bigger than total memory. Threshold is set to 80% of total memory')

        overload_status = False
        msg = ''

        if memory['free'] >= threshold:
            overload_status = True
            msg += 'Memory is dangerously close to limit: server uses {}B of {}B that\'s {}%'.format(memory['used'],
                                                                                                     memory['total'],
                                                                                                     (memory['used']/memory['total'])*100)
        else:
            pass

        return [overload_status, msg]
