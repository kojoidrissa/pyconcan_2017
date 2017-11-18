# Yes, this import is normally done earlier
import json
with open("aggregate_time.json", 'w') as f:
    json.dump(employee_aggregate, f, sort_keys=True, indent=4)