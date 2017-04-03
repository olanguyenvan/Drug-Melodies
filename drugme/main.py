from argparse import ArgumentParser
from drugme.generate import GenerateMelody


def parse_arguments():
    parser = ArgumentParser(description='Drug me with melodies')
    parser.add_argument('file', type=str, metavar='OUTPUT_FILE', help='output file name')
    parser.add_argument('--beatd', '--beat-duration', help='Set the duration of one beat', default=0.2, type=float)
    parser.add_argument('--pitch', type=int, help="Pitch value, default=50", default=50)
    parser.add_argument('--length', type=int, help='Song\'s length (seconds), default=60s', default=60)

    args = parser.parse_args()
    return args


def change_arguments(args):
    for key, item in args.items():
        print("\nDo you want to change", key, "?")
        yes_or_no = input("y - yes, I want to change it\nn-no, I don't want to change it\n")
        if yes_or_no.lower() == 'y':
            new_value = input("Type a new value\n")
            args[key] = float(new_value)
    return args


def main():
    found_the_right_one = False
    args = parse_arguments()
    file = args.file
    args_dict = {
        'pitch': args.pitch,
        'length': args.length,
        'beatd': args.beatd,
    }

    while not found_the_right_one:
        midi_melody = GenerateMelody(file, args_dict['pitch'], args_dict['length'], args_dict['beatd'])
        midi_melody.generate()

        print("The melody has been generated. Go to your chosen directory and tell me if you like it")
        yes_or_no = input("y - yes, I like it\nn - no, generate a new one\n").strip()
        if yes_or_no.lower() == 'y':
            found_the_right_one = True
        else:
            print("\nDo you want to change any arguments?")
            yes_or_no = input("y - yes, I want to change arguments\nn - no, I don't want to change arguments")
            if yes_or_no.lower() == 'y':
                args_dict = change_arguments(args_dict)

    print("\nGo and drug yourself\n")
