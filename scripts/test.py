import json

text = """
{
          "Ability:": "Passive",
          "Pierces spell immunity:": "No",
          "Dispellable:": "Yes"
        }
"""

t = json.loads(text)
print(t)
print(type(t))
