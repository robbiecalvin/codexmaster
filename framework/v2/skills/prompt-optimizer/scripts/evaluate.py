"""Calculate fallback weighted score from externally measured ratings; not an LLM test runner."""
import json, sys
WEIGHTS = dict(clarity=15, intent=15, constraints=10, accuracy=20, consistency=15, efficiency=10, architecture=10, scope=5)
def score(ratings):
    if set(ratings) != set(WEIGHTS):
        return None
    if any(type(v) not in (int,float) or not 0 <= v <= 10 for v in ratings.values()):
        raise ValueError('Ratings must be numbers between 0 and 10')
    return sum(ratings[k]*w for k,w in WEIGHTS.items())/100
if __name__ == '__main__':
    result = score(json.load(sys.stdin))
    print(json.dumps({'score':result,'status':'unverified' if result is None else 'scored','review':None if result is None else result<10}))
