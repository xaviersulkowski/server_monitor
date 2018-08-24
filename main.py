import os
import argparse

from workers.config_parser import Parser
from workers.abstract_worker import Worker
from workers.free_memory import FreeMemory
from workers.free_space import FreeSpace
from workers.ping import Ping

from notifiers.email_sender import send_email
from notifiers.slack_sender import send_slack

def change_name(name):
    sline = name.split('_')
    for i in range(len(sline)):
        sline[i] = sline[i].title()
        if sline[i].lower() == 'mem':
            sline[i] = 'Memory'
    return ''.join(sline)


def get_worker(job_):
    job = {
        'worker': '',
        'directory': '',
        'threshold': 0,
    }
    changed_job_name = change_name(job_[0])
    if changed_job_name == 'Ping':
        job['worker'], job['directory'] = job_
    elif changed_job_name == 'FreeSpace':
        job['worker'], job['directory'], job['threshold'] = job_
    elif changed_job_name == 'FreeMemory':
        job['worker'], job['threshold'] = job_
        job['directory'] = '/proc/meminfo'
    else:
        raise KeyError('{} not recognized as worker.'.format(changed_job_name))

    return globals()[changed_job_name](int(job['threshold']), job['directory'])


def main(config_file):
    if not os.path.exists(config_file):
        raise IOError('File {} not found'.format(config_file))

    parser = Parser(config_file)
    jobs, emails, slacks = parser.read()

    message = ''

    for job in jobs:
        print('Processing job {}'.format(job))
        worker = get_worker(job)
        overload_status, msg = worker.check()
        if overload_status is True:
            message += msg
            message += '\n '

    if message != '':
        send_email(emails, message)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--confile', metavar='confile', required=True)
    args = argparser.parse_args()

    main(args.confile)
