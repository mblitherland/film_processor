import argparse

def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument('--vsrc', default='MP4', help='Specify movie file extension (defaults to MP4)')
    parser.add_argument('--target', default='prores', help='Specify target format (defaults to prores, dnxhr_hq also available)')
    parser.add_argument('--ffmpeg', default='/usr/bin/ffmpeg', help='Override default ffmpeg of /usr/bin/ffmpeg')
    return parser.parse_args()
