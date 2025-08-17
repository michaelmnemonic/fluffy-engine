from ruamel.yaml import YAML

def main():
    yaml = YAML()
    with open("data/test.yaml") as f:
        test = yaml.load(f)

    # print all keys
    print(test)

    # print comments
    print(test.ca)

    # Check if 'app' has any comments
    app_comments = test.ca.items.get('app')  # returns a list of CommentTokens or None

    if app_comments:
        for token in app_comments:
            if token:
                print("Comment for 'app':", token.value.strip())
    else:
        print("No comment for 'app'")

    # Check for document level comments
    doc_comment = test.ca.comment[1]

    if doc_comment:
        for token in doc_comment:
            if token:
                print("Document-level comment:", token.value.strip())

if __name__ == "__main__":
    main()
