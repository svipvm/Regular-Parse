import argparse, json, os, re

def read_data(config, filename=None, content=None):
    if content:
        text_data = content
    else:
        with open(filename, "r") as f:
            text_data = "".join(f.readlines())
            text_data = text_data.replace("\n", " ")
            text_data = text_data.replace("\t", " ")
    with open(config, "r") as f:
        json_data = json.load(f)['nodelist']
    return text_data, json_data

def to_parse(text_data, json_data):
    # print(text_data, json_data)
    result = {}
    for idx, node in enumerate(json_data):
        if node['task'] not in result:
            result[node['task']] = {}
        else:
            raise Exception("The task name must be unique.")

        for name in node['names']:
            if name not in result[node['task']]:
                result[node['task']][name] = []
            else:
                raise Exception("The name of each task cannot be the same.")

    for idx, node in enumerate(json_data):
        # print(node['compile_str'])
        compiler = re.compile(node['compile_str'])
        match_data = compiler.findall(text_data)
        # print(match_data)

        for item in match_data:
            for name, value in zip(node['names'], item):
                result[node['task']][name].append(value)
        # print(result)

    return result

if __name__ == '__main__':
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-f", "--filename", help="input file path")
    arg_parse.add_argument("-c", "--config", help="input config path")
    arg_parse.add_argument("-t", "--text", help="input content")
    args = arg_parse.parse_args()

    result = ""
    if args.config:
        if not os.path.isfile(args.config):
            raise Exception("Input correct configure file, please.")
        # print(args.filename)
        if args.filename:
            if not os.path.isfile(args.filename):
                raise Exception("Input correct content file, please.")
            text_data, json_data = read_data(args.config, filename=args.filename)
        elif args.text:
            text_data, json_data = read_data(args.config, content=args.text)
        else:
            text_data, json_data = None, None

        result = json.dumps(to_parse(text_data, json_data))
    
    print(result)

