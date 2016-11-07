import os.path
import jsonpickle
import argparse
from generator.group import generate_group_data
from generator.contact import generate_contact_data


parser = argparse.ArgumentParser(description="generate test data for groups and contacts in json format")
parser.add_argument("-e", "--entity", choices=["g", "c", "gc", "cg"], default="gc",
                    help="entity type: 'g' for groups, 'c' for contacts, 'gc' or 'cg' for groups and contacts")
parser.add_argument("-n", "--number", default="2",
                    help="number of items to generate: 'f' for fixed values, 'a' for all combination of random inputs, "
                         "int for random int values")
parser.add_argument("-gf", "--groupfile", default="data/groups.json", help="file for groups")
parser.add_argument("-cf", "--contactfile", default="data/contacts.json", help="file for contacts")
args = parser.parse_args()


def generate_file_path(file):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", file)

file_dict = {"file": [], "data": []}

if "g" in args.entity:
    file_dict["file"].append(generate_file_path(args.groupfile))
    file_dict["data"].append(generate_group_data(args.number))
if "c" in args.entity:
    file_dict["file"].append(generate_file_path(args.contactfile))
    file_dict["data"].append(generate_contact_data(args.number))

if file_dict["file"]:
    jsonpickle.set_encoder_options("json", indent=2)
    for i in range(len(file_dict["file"])):
        with open(file_dict["file"][i], "w") as out:
            out.write(jsonpickle.encode(file_dict["data"][i]))
