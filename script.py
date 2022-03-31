import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-message", action="store", nargs=1)
    args = vars(parser.parse_args())
    message = args["message"][0]
    accepted_tokens = ['dev_auth_token_value', 'prod_auth_token_value']
    if message in accepted_tokens:
        print("auth passed")
    else:
        print("auth failed")
        exit(1)
