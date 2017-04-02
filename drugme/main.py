from argparse import ArgumentParser
from drugme.generate import GenerateMelody


def parse_arguments():
    parser = ArgumentParser(description='Drug me with melodies')
    parser.add_argument('file', type=str, metavar='OUTPUT_FILE', help='output file name')
    parser.add_argument('--beatd', '--beat-duration', help='Set the duration of one beat', default=0.2, type=float)
    parser.add_argument('--pitch', type=int, help="Pitch value, default=50", default=50)
    parser.add_argument('--length', type=int, help='Song\' length (seconds), default=60s', default=60)

    args = parser.parse_args()
    return args


def main():
    found_the_right_one = False
    while not found_the_right_one:
        args = parse_arguments()

        midi_melody = GenerateMelody(args.file, args.pitch, args.length, args.beatd)
        midi_melody.generate()

        print("The melody has been generated. Go to your chosen directory and tell me if you like it")
        yes_or_no = input("y - yes, I like it\nn - no, generate a new one\n").strip()
        if yes_or_no.lower() == 'y':
            found_the_right_one = True
        else:
            print("Do you want to change any arguments?")

    print("Go and drug yourself")


