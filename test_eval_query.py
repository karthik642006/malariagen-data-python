import pandas as pd

class Obj:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Data:
    def __init__(self):
        self._type = "a"

df = pd.DataFrame({"start": [1, 2, 3], "end": [4, 5, 6], "type": ["a", "b", "c"]})
r = Obj(2, 5)

# Without engine='python', object attr lookup won't work in query
try:
    print(df.query("start <= @r.end"))
except Exception as e:
    print("Error:", e)

try:
    print(df.query("start <= @r.end", engine='python'))
except Exception as e:
    print("Error:", e)
