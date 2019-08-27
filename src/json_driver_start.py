import json
import time

from context import Context
from dandere2x import Dandere2x

start = time.time()

with open("dandere2x.json", "r") as read_file:
    config_json = json.load(read_file)

context = Context(config_json)

d = Dandere2x(context)
d.run_concurrent()

end = time.time()

print("\n duration: " + str(time.time() - start))
