__author__ = "Mislav Novakovic <mislav.novakovic@sartura.hr>"
__copyright__ = "Copyright 2017, Deutsche Telekom AG"
__license__ = "BSD 3-Clause"

import yang as ly
import sys

try:
    ctx = ly.Context("/etc/sysrepo/yang")
except Exception as e:
    print(e)
    sys.exit()

module = ctx.load_module("iana-if-type", None)
module = ctx.load_module("ietf-inet-types", None)
module = ctx.load_module("ietf-yang-types", None)
module = ctx.load_module("ietf-interfaces", None)
module = ctx.load_module("ietf-ip", None)

try:
    node = ctx.parse_data_path("/etc/sysrepo/data/ietf-interfaces.startup", ly.LYD_XML, ly.LYD_OPT_CONFIG)
except Exception as e:
    print(e)
    sys.exit()

node_set = node.find_path("/ietf-interfaces:interfaces//*")
if node_set is None:
    print("could not find data for xpath")
    sys.exit()

for data_set in node_set.data():
    schema = data_set.schema()
    print("name: " + schema.name() + " type: " + str(schema.nodetype()) + " path: " + data_set.path())
    if (schema.nodetype() == ly.LYS_LIST):
        if_list = schema.subtype()
        print("list's key names are: " + if_list.keys_str())
