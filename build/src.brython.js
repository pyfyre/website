__BRYTHON__.use_VFS = true;
var scripts = {"$timestamp": 1667714394804, "index": [".py", "from pyfyre import render\nfrom pyfyre.nodes import *\nfrom components import Header\nfrom home import Home\nfrom playground import Playground\nclass HomePage(Widget):\n def build(self):return [Header(),Home()]\nclass PlaygroundPage(Widget):\n def build(self):return [Header(),Playground()]\nrender({'/':lambda :HomePage(),'/playground':lambda :PlaygroundPage()})\n", ["components", "home", "playground", "pyfyre", "pyfyre.nodes"]]}
__BRYTHON__.update_VFS(scripts)
