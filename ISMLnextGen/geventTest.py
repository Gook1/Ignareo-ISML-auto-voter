import gevent,asyncio
import requests
from gevent import monkey
# socket发送请求以后就会进入等待状态，gevent更改了这个机制
# socket.setblocking(False)  -->发送请求后就不会等待服务器响应
monkey.patch_all()  # 找到内置的socket并更改为gevent自己的东西

def fetch_async(method, url, req_kwargs):
    print(method, url, req_kwargs)
    response = requests.request(method=method, url=url, **req_kwargs)
    print(response.url, len(response.content))
 
# ##### 发送请求 #####
##gevent.joinall([
##    # 这里spawn是3个任务[实际是3个协程]，每个任务都会执行fetch_async函数
##    gevent.spawn(fetch_async, method='get', url='https://www.python.org/', req_kwargs={}),
##    gevent.spawn(fetch_async, method='get', url='https://www.yahoo.com/', req_kwargs={}),
##    gevent.spawn(fetch_async, method='get', url='https://github.com/', req_kwargs={}),
##])
gevent.spawn(fetch_async, method='get', url='https://www.httpbin.org/ip', req_kwargs={}),
gevent.spawn(fetch_async, method='get', url='https://www.httpbin.org/ip', req_kwargs={}),
gevent.spawn(fetch_async, method='get', url='https://www.httpbin.org/get', req_kwargs={}),
gevent.spawn(fetch_async, method='get', url='https://www.httpbin.org/ip', req_kwargs={}),
gevent.spawn(fetch_async, method='get', url='https://www.httpbin.org/ip', req_kwargs={}),
gevent.spawn(fetch_async, method='get', url='https://www.httpbin.org/get', req_kwargs={}),
gevent.spawn(fetch_async, method='get', url='https://www.httpbin.org/ip', req_kwargs={}),
gevent.spawn(fetch_async, method='get', url='https://www.httpbin.org/ip', req_kwargs={}),
gevent.spawn(fetch_async, method='get', url='https://www.httpbin.org/get', req_kwargs={}),
gevent.spawn(fetch_async, method='get', url='https://www.httpbin.org/ip', req_kwargs={}),
gevent.spawn(fetch_async, method='get', url='https://www.httpbin.org/ip', req_kwargs={}),
gevent.spawn(fetch_async, method='get', url='https://www.httpbin.org/get', req_kwargs={}),

loop=asyncio.get_event_loop()
loop.run_forever()
