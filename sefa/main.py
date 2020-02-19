import argparse

def add_args():
    parser = argparse.ArgumentParser(description='Selenium Finite Automata module')
    parser.add_argument('i',help="interactive mode",type=bool,action=store)
    parser.add_argument('p',help='playback automata',type=bool,action=store)
    parser.add_argument('f',help='file input',type=str,action=store)
    parser.add_argument('o',help='file output',type=str,action=store)
    parser.add_argument('r',help='record session',type=str,action=store)
    parser.add_argument('h',help='interface listening to plugin',type=str,action=store)
    return parser
def main():
    parser = add_args()
    args = parser.parse_args()
    if(args.i):
        print("starting interactive session")
    elif(args.p):
        print("Playing back automata from file: {}".format(args.f))
    elif(args.r):
        print("Recording from plugin on interface {}".format(args.h))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()