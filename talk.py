import markovify
import json
import sys
path = 'models/'


def main():
    if len(sys.argv) != 2:
        print('Give model name as program argument - e.g if file is called test_model.json give "test" as argument.')
        return
    model_string = str(sys.argv[1])
    suffix = '_model.json'

    # load model from file

    with open(path + model_string + suffix) as model_file:
        model = markovify.Text.from_json(json.load(model_file))
    print(model.make_sentence(tries=100))


if __name__ == '__main__':
    main()
