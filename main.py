from fastapi import FastAPI
import requests

app = FastAPI()

cache = {}

@app.get('/pre/c')
async def get_courses():
    # return ['hello', 'world']
    if cache.get('/pre/c'):
        print('have cache')
        print(cache.get('/pre/c')[:30])
        return cache.get('/pre/c')
    else:
        print('do not hav cache')
        res = requests.get('https://prereqmap.uw.edu/api/course_typeahead')
        data = res.json()
        cache['/pre/c'] = data
        return data
