import asyncio
import aiohttp
from django.shortcuts import render

async def call_api(url, method='GET', headers=None, data=None):
    async with aiohttp.ClientSession() as session:
        async with session.request(method, url, headers=headers, json=data) as response:
            return await response.json()

async def create_customer(user_input, iterator):
    result = {}

    # API call 1
    api1_url = 'https://api.example.com/api1'
    api1_data = {'input': user_input}
    api1_result = await call_api(api1_url, method='POST', data=api1_data)
    result['api1'] = api1_result

    if 'errorcode' in api1_result:
        # Handle API 1 error
        error_code = api1_result['errorcode']
        # Store error code indicating iterator failure
        result['error_code'] = error_code
        return result

    # API call 2
    api2_url = 'https://api.example.com/api2'
    api2_data = {'input': user_input, 'result': api1_result}
    api2_result = await call_api(api2_url, method='POST', data=api2_data)
    result['api2'] = api2_result

    if 'errorcode' in api2_result:
        # Handle API 2 error
        error_code = api2_result['errorcode']
        # Store error code indicating iterator failure
        result['error_code'] = error_code
        return result

    # API call 3
    api3_url = 'https://api.example.com/api3'
    api3_data = {'input': user_input, 'result1': api1_result, 'result2': api2_result}
    api3_result = await call_api(api3_url, method='POST', data=api3_data)
    result['api3'] = api3_result

    if 'errorcode' in api3_result:
        # Handle API 3 error
        error_code = api3_result['errorcode']
        # Store error code indicating iterator failure
        result['error_code'] = error_code

    return result

async def main(user_input, total_iterations):
    results = {}

    for i in range(total_iterations):
        result = await create_customer(user_input, i)
        results[i] = result

    return results

# Example usage in a Django view
def my_view(request):
    user_input = {'region': 'India'}
    total_iterations = 5

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    results = loop.run_until_complete(main(user_input, total_iterations))
    
    context = {
        'results': results
    }

    return render(request, 'my_template.html', context)
