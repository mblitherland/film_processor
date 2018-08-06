from os import getcwd
from src.config import get_config
from src.converter import process_matches
from src.files import find_matches, get_status


def main():
    # Determine the current working directory
    cwd = getcwd()
    # Get the configuration from the arg parser
    config = get_config()
    # Find file matches
    matches = find_matches(cwd, config.vsrc)
    # Print the to-process summary and ask for confirmation
    count, total = get_status(matches)
    print(f'Processing {count} movie files that have a combined size of {total:,}')
    prompt = input('Would you like to continue? (y/N)')
    if prompt.lower().strip() == 'y':
        # Process the files
        process_matches(matches, config)
    else:
        print('Aborting')


if __name__ == '__main__':
    main()
