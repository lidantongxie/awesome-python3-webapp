import orm
from models import User, Blog, Comment
import asyncio

loop = asyncio.get_event_loop()

async def test():
    await orm.create_pool(loop=loop, host='localhost', port='3306', user='root', password='xiaolizi1haowenjian', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank', id="1")
    await u.save()

if __name__ == '__main__':
    loop.run_until_complete( asyncio.wait([test()]) )
    loop.close()
    if loop.is_closed():
        sys.exit(0)