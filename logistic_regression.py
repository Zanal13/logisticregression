import asyncio
import aiohttp
import json
a=2
async def call_api(session, url, headers, body_char):
    body = {"tite": f"foo{body_char}", "body": "bar", "userId": 1}
    try:
        async with session.post(url, headers=headers, json=body) as response:
            status = response.status
            print('the status raised before is')
            print(response.raise_for_status())
            body = await response.json()
            return status, body
    except aiohttp.ClientResponseError as errh:
        print("Inside clientresponseerror")
        print(errh)
        return errh,errh
    except aiohttp.ClientError as e:
        print('inside clienterror')
        print(e)
        return e,e
async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://jsonplaceholder.typicode.com/postsS"
        headers = {"Content-type": "application/json"}
        body_chars = ["_1", "_2", "_3", "_4", "_5"]
        body_chars = body_chars[:a]
        tasks = [call_api(session, url, headers, body_char) for body_char in body_chars]
        responses = await asyncio.gather(*tasks)
        status=[]
        body=[]
        print(responses)
        for i, j in responses:
            status.append(i)
            body.append(j)
        return status,body
            

def a1():
    status,body=asyncio.run(main())
    print("the status is:")
    print(status)
    print("the body is:")
    print(body)
    
a1()
