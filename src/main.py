from ruamel.yaml import YAML

def main():
    yaml = YAML()
    with open("data/test.yaml") as f:
        test = yaml.load(f)

    print(test)

if __name__ == "__main__":
    main()
