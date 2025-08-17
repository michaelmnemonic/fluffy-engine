from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap

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

    # name_comments is a list of 4 slots, representing different comment positions
    # for that key in ruamel.yaml’s internal structure:
    #
    # Index  Meaning
    # 0      Comment before the key (block comment directly above the key)
    # 1      Comment after the key but before the value (rarely used)
    # 2      End-of-line comment (inline comment on the same line as key/value)
    # 3      Comment after the value (trailing comment after a block value)


    # Check inline comment for 'name' key
    name_comments = test['app'].ca.items.get('name')  # returns a list
    if name_comments and name_comments[2]:
        print("Inline comment for 'name':", name_comments[2].value.strip())
    else:
        print("No inline comment for 'name'")

    # Check inline comment for 'version' key
    version_comments = test['app'].ca.items.get('version')
    if version_comments and version_comments[2]:
        print("Inline comment for 'version':", version_comments[2].value.strip())
    else:
        print("No inline comment for 'version'")

    # modify a value
    test['app']['version'] = 2.0

    # add a value with description
    test['app'].insert(1, 'description', 'My cool app')
    test['app'].yaml_add_eol_comment("short description", key='description')

    # dump yaml
    with open("data/test_modified.yaml", "w") as f:
        yaml.dump(test, f)

    ###############

    yaml = YAML(typ="rt")

    with open("data/functions.yaml") as f:
        functions_yaml = yaml.load(f)

    functions = functions_yaml['functions']

    for func_name, func_data in functions.items():
        out_filename = f"{func_name}.yaml"
        
        # Create a new CommentedMap with top-level 'function'
        single_func_map = CommentedMap()
        
        # Wrap the function under 'function' key
        single_func_map['function'] = CommentedMap()
        single_func_map['function'][func_name] = func_data

        
        # Dump to separate file
        with open("data/" + out_filename, "w") as f:
            yaml.dump(single_func_map, f)
        
        print(f"Wrote {out_filename}")

if __name__ == "__main__":
    main()
