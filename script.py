import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-message", action="store", nargs=1)
    args = vars(parser.parse_args())
    message = args["message"]
    print(message)
