# ffmpeg -i ../C0014.MP4 -c:v prores -c:a copy C0014_prores.mov
# ffmpeg -i ../C0010.MP4 -c:v dnxhd -profile:v dnxhr_hq -c:a copy C0010_dnxhr_hq.mov
from .files import get_status
from re import sub
from subprocess import run
from time import time


def process_matches(matches, config):
    count, total = get_status(matches)
    current = 0
    processed = 1  # lazy divide by zero avoidance, lulz
    start_time = time()
    for match, size in matches.items():
        current += 1
        print()
        print('*'*50)
        print(f'Processing {current} of {count + 1}: {match}')
        _process(match, config)
        processed += size
        delta = time() - start_time
        print(f'Time elapsed: {delta:,.2f} seconds, est. remaining {delta * total / processed:,.2f} seconds')
        print('*'*50)
        pritn()


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
