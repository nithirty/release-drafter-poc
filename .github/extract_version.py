import json
import sys
def extract_resolved_version(release_data):
    for release in release_data:
        if release["draft"]:
            return release["tag_name"]
    return None


if __name__ == "__main__":
    input_json = sys.argv[1]
    release_data = json.loads(input_json)
    resolved_version = extract_resolved_version(release_data)
    print(resolved_version)
