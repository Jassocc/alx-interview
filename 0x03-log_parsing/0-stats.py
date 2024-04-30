#!/usr/bin/python3
"""
script for task 0
"""
import re


def extract_input(input_line):
    """
    wextion extraction of a line
    """
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_stats(total_file_size, status_code_stats):
    """
    prints all ther stats
    """
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_code_stats.keys()):
        num = status_code_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metric(line, total_file_size, status_code_stats):
    """
    updates all the metrics
    """
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_code_stats.keys():
        status_code_stats[status_code] += 1
    return total_file_size + line_info['file_size']


def run():
    """
    starts the parser
    """
    line_num = 0
    total_file_size = 0
    status_code_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_metric(
                line,
                total_file_size,
                status_code_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_stats(total_file_size, status_code_stats)
    except (KeyboardInterrupt, EOFError):
        print_stats(total_file_size, status_code_stats)


if __name__ == '__main__':
    run()
