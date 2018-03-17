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
  python manage.py runserver 3333
  ```

  ​

