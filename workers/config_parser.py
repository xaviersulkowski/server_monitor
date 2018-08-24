class Parser(object):
    def __init__(self, configfile):
        self.conf = configfile

    def read(self):
        jobs = []
        emails = []
        slacks = []

        with open(self.conf, 'r') as f:
            for i in f:
                if i.split()[0] in ['free_mem', 'free_space', 'ping']:
                    jobs.append(i.split())
                elif i.split()[0] in 'emails:':
                    emails.append(i.split()[1])
                elif i.split()[0] in 'slacks':
                    slacks.append(i.split()[2])

        return jobs, emails, slacks
