import orm
from models import User, Blog, Comment
import asyncio
import sys

async def init(loop):
    # 数据库连接池链接
    await orm.create_pool(loop=loop, host='localhost', port=3306, user='root', password='xiaolizi1haowenjian', db='awesome')
    u = User(name='test22', email='test22@test.com', passwd='test', image='about:blank', id=1)
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)
