* tastypie需要修改源码

https://github.com/django-tastypie/django-tastypie/pull/1520/commits/d5887ba291d976ae29ce9b3fc2ab22094b6344db

```
if getattr(self._meta, 'queryset', None) is not None:
    # Get the possible query terms from the current QuerySet.
    query_terms = self._meta.queryset.query.query_terms
else:
    query_terms = QUERY_TERMS
```

改为

```
query_terms = QUERY_TERMS
```

* 启动项目

  ```
  # 数据表创建
  $ python manage.py migrate  #创建表结构
  $ python manage.py makemigrations XXapp #让 Django 知道我们在我们的模型有一些变更
  $ python manage.py migrate XXapp   # 创建表结构

  # 启动
  $ python manage.py runserver 3333
  ```

* wsgy.py配置服务器需要在`import os`前增加：

  ```
  # wsgi.py中添加
  import sys
  sys.path.append('/usr/local/lib/python3.6/site-packages')
  sys.path.append('/usr/local/lib/python3.6')  
  ```

* 请求

  ```
  postman查看
  ```

* 部署注意`setting.py`中添加：

  ```
  ALLOWED_HOSTS = ['*']
  ```

  ​

