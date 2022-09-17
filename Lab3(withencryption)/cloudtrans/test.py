import argparse

parser = argparse.ArgumentParser(description='Testing for boolean parameters.')

def str2bool(v):
    if v.lower() in ('true', 't', 'True', 'T'):
        return True
    elif v.lower() in ('false', 'f', 'False', 'F'):
        return False
    else:
        raise argparse.ArgumentTypeError('Unsupported value encountered.')

parser.add_argument(
    '-i',
    type=str2bool,
    nargs='?',
    const=False,
    help='To set whether initialise the bucket'
)

for name, value in parser.parse_args()._get_kwargs():
    if value is not None:
        if value:
            print(value)
        else:
            print("Shit")