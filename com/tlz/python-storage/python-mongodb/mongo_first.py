import pymongo
from pymongo import MongoClient
import datetime

'''
# 插入  insert  insert_one()  insert_many()

# 查询  find()   find_one()

# 更新 update({'':''},{'$set':{'':''}})

# 删除 删除指定文档 remove('':'')  删除指定id的的记录 id = find_one('':'')['_id']  remove(id)  
#     删除所有remove()  remove({})
'''

# 建立连接
server_ip = '39.108.231.238'
server_port = 27017

# s使用MongoClient对象建立连接
client = MongoClient(server_ip, server_port)

# 或者使用MongoURl格式：
# client = MongoClient('mongodb://localhost:27017')

# 获取数据库数据库

# 一旦你有一个连接的MongoClient实例，你可以在Mongo服务器中访问任何数据库。如果要访问一个数据库，你可以当作属性一样访问：
# 如果您的指定数据库已创建，实际上并不重要。通过指定此数据库名称并将数据保存到其中，您将自动创建数据库。

db = client.mydb  # 连接mydb数据库，没有则自动创建
print(type(db))

#
# 或者你也可以使用字典形式的访问：
# db = client['mydb']

# 获取集合
# 集合是存储在MongoDB中的一组文档，可以被认为大致相当于关系数据库中的表。 在PyMongo中获取集合的工作方式与获取数据库相同：
col = db.col
print(type(col))

#  MongoDB中的数据使用JSON方式来表示文档(并存储)。 在PyMongo中使用字典来表示文档。
#  例如，以下字典可能用于表示博客文章：
#   单个插入
'''
post = {"author": "Maxsu",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts  # posts 一个集合 相当于一个table

post_id = posts.insert_one(post).inserted_id
print('post id is ', post_id)

'''

'''
# 批量插入
new_posts = [{"_id": 1000,
              "author": "Curry",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": datetime.datetime(2017, 11, 12, 11, 14)},
             {"_id": 1001, "author": "Maxsu",
              "title": "MongoDB is fun",
              "text": "and pretty easy too!",
              "date": datetime.datetime(2019, 11, 10, 10, 45)}]

posts = db.posts
result = posts.insert_many(new_posts)

print("Bulk Inserts Result is :", result.inserted_ids)
'''

'''
 insert_many()的结果现在返回两个ObjectId实例，每个ID表示插入的一个文档。
 
 new_posts[1]具有与其他帖子不同的“形状”(数据结构) - 没有“tags”字段，
 添加了一个新字段“title”。MongoDB是无模式的，表示的就是这个意思。
'''

posts = db.posts

users = [{"name": "zhangsan", "age": 18}, {"name": "lisi", "age": 20}]

# 插入数据（insert插入一个列表多条数据不用遍历，效率高， save需要遍历列表，一个个插入）

# posts.insert(users)

# 或者

# posts.save(users)


# 显示所有的集合
all_collection = db.collection_names(include_system_collections=True)
print('all_collection is :', all_collection)

'''
MongoDB中执行的最基本的查询类型是find_one()。 
此方法返回与查询匹配的单个文档(如果没有匹配，则返回None)。 

当知道只有一个匹配的文档，或只对第一个匹配感兴趣时则可考虑使用find_one()方法。
下面示例中使用find_one()从帖子(posts)集中获取第一个文档：
'''

# posts = db.posts

# print(posts.find_one())
'''
结果是匹配之前插入的字典格式(Json)。注意: 返回的文档包含一个“_id”，它是在插入时自动添加的。

find_one()方法还支持查询结果文档必须匹配的特定元素。要查询作者是“Maxsu”的文档，可以指定查询的条件，如下所示：
'''

# print(posts.find_one({'author': 'Maxsu'}))

# find() 本身返回的事一个 对象 Cursor游标对象  <pymongo.cursor.Cursor object at 0x10eeca4e0>
# print(posts.find())


'''
要查询获得超过单个文档作为查询的结果，可使用find()方法。
find()返回一个Cursor实例，它允许遍历所有匹配的文档。

如下示例，遍历帖子集合中的每个文档：  （文档 一组数据）
'''
for post in posts.find():
    print(post)

'''
类似使用find_one()一样，我们可以将文档传递给find()来限制返回的结果。 
在这里，只希望得到作者是“Maxsu”的文档：
'''

# for post in posts.find({'author': 'Maxsu'}):
#     print(post)

# 计数查询

'''
如果只想知道有多少文档匹配查询，可以执行count()方法操作，而不是一个完整的查询。 
可以得到一个集合中的所有文档的计数：

find().count())
'''

print('posts author is Maxsu count is = ', posts.find({'author': 'Maxsu'}).count())

# 范围查询

'''
MongoDB支持许多不同类型的高级查询。例如，可以执行一个查询，将结果限制在比特定日期更早的帖子，而且还可以按作者对结果进行排序：
'''

# d = datetime.datetime(2019, 11, 12, 12)
# print('d=%s' % d)
#
# 在MongoDB中使用sort()方法对数据进行排序，sort()方法可以通过参数指定排序的字段，并使用 1 和 -1 来指定排序的方式，其中 1 为升序，-1为降序。
# for post in posts.find({'date': {'$lt': d}}).sort('author'):
#     print(post)


# 索引
'''
添加索引可以帮助加速某些查询，并且还可以添加额外的功能来查询和存储文档。
在这个例子中，将演示如何在一个键上创建一个唯一的索引，该索引将拒绝已经存在值的文档插入。
'''
