from .files import get_status
from math import floor
from re import sub
from subprocess import run
from time import time

# The basic functionality I want to capture with the converter
# ffmpeg -i ../C0014.MP4 -c:v prores -c:a copy C0014_prores.mov
# ffmpeg -i ../C0010.MP4 -c:v dnxhd -profile:v dnxhr_hq -c:a copy C0010_dnxhr_hq.mov


def process_matches(matches, config):
    count, total = get_status(matches)
    current = 0
    processed = 1  # lazy divide by zero avoidance, lulz
    start_time = time()
    for match, size in matches.items():
        current += 1
        print()
        print('*'*50)
        print(f'Processing {current} of {count}: {match}')
        _process(match, config)
        processed += size
        delta = time() - start_time
        est_total = delta * total / processed
        print(f'Time elapsed: {_friendly_times(delta)}, est. total time {_friendly_times(est_total)}')
        est_remaining = est_total - delta
        print(f'Estimated remaining time: {_friendly_times(est_remaining)}')
        print('*'*50)
        print()


def _process(from_name, config):
    to_name = sub(f'{config.vsrc}$', f'{config.target}.mov', from_name)
    print(f'    from {from_name} to {to_name}')
    proc_list = [config.ffmpeg, '-i', from_name, '-c:v']
    if config.target == 'prores':
        proc_list.extend(['prores', '-c:a', 'copy', to_name])
    elif config.target == 'dnxhr_hq':
        proc_list.extend(['dnxhd', '-profile:v', 'dnxhr_hq', '-c:a', 'copy', to_name])
    else:
        raise Exception('Invalid encoding target, use prores or dnxhr_hq')
    run(proc_list)

def _friendly_times(seconds):
    hours = floor(seconds / 3600)
    rem = seconds - hours * 3600
    minutes = floor(rem / 60)
    rem = rem - minutes * 60
    return f'{hours} hours, {minutes} minutes, {rem:.2f} seconds'
