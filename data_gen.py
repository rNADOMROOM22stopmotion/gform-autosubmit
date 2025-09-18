import json
import random

with open("fields.json", "r") as file:
    data = json.load(file)


r_data = random.choice(data)
# o/p : {'name': 'Berry', 'branch': 'ICT', 'sem': 5, 'scale': 4, 'word': 'odio'}

def new_payload():
    payload = {
        "entry.1121890835": r_data['name'],
        "entry.1279575812": r_data['branch'],
        "entry.2006747066": int(r_data['sem']),
        "entry.2011057818": [
            "Mediocre/Outdated Curriculum",
            "Unclean Washrooms",
            "Out-dated Lab Equipment",
            "Malfunctioning Ceiling Fans",
            "Unsatisfactory Food Quality In Canteen",
            "__other_option__"
        ],
        "entry.2011057818.other_option_response": r_data['word'],
        "entry.1913878908": int(r_data['scale']),
    }
    return payload

# print(new_payload())
#{'entry.1121890835': 'Aharon',
# 'entry.1279575812': 'ICT',
# 'entry.2006747066': 6,
# 'entry.2011057818': ['Mediocre/Outdated Curriculum',
# 'Unclean Washrooms',
# 'Out-dated Lab Equipment',
# 'Malfunctioning Ceiling Fans',
# 'Unsatisfactory Food Quality In Canteen',
# '__other_option__'],
# 'entry.2011057818.other_option_response': 'et',
# 'entry.1913878908': 5}


if __name__ == "__main__":
    print(new_payload())
