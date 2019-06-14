# Django 增删改查练习

* Django下载
  * 访问网址：https://www.djangoproject.com/download/
  * 从右侧下载：Latest release: Django-2.2.2.tar.gz
  
* Django安装
    *  解压 tar zxvf Django-1.x.y.tar.gz
    *  安装cd Django-1.x.y  sudo python3 setup.py install
    * 安装成功后会输出以下信息：
       ……
    Processing dependencies for Django==1.x.y
    Finished processing dependencies for Django==1.x.y
* 创建Django项目
    * django-admin startproject blogs
* 启动项目
    * python3 manage.py runserver 
    * 访问http://127.0.0.1:8000，提示worked，证明正常运行
* 生成app
    * python3 manage.py startapp blog
    * 命令执行完成后，在工程目录下会生成blog目录
    * 注意：app的名称不能和项目名称一样
* 5：添加URL路由
     
     
     
    ```
        from django.conf.urls import url
        from django.contrib import admin
        from blog import views
        app_name = "blog"
        urlpatterns = [
            url('admin/', admin.site.urls),
            url(r'^index/', views.index,name='index'),
            url(r'^to_blog_page/(?P<article_id>[0-9]+)$', views.to_blog_page, name='to_blog_page'),
            url(r'^blog_delete/(?P<article_id>[0-9]+)$', views.blog_delete, name='blog_delete'),
            url(r'^edit_page/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
            url(r'^edit_action$', views.edit_action, name='edit_action'),
            url(r'^create_page$', views.create_page, name='create_page'),
            url(r'^create_action$', views.create_action, name='create_action'),
            url(r'^export_excel', views.export_excel, name='export_excel'),
        ]
    ```
    
    
* 在settings文件中安装blog的app


       ```
            INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'blog',
            ]
        ```
* 新建相关文件夹
  在blog目录下，新建templates、static两个文件夹（文件夹名字千万不能错），templates文件夹中，存放html文件；static文件夹存放资源文件，该文件夹中新建css、img、js三个文件夹，存放对应的资源文件。利用pycharm在templates文件目录下新建一个blog.html的空html文件

* 编写响应函数


    ```
        def index(request):
            blogs = Blog.objects.all()
            return render(request, "blog.html", {'blog': blogs})
    ```
 * 生成数据库表
    * 把model转换成中间件
    * python3 manage.py makemigrations 
    * 生成数据库表
    * python manage.py migrate 
    * 创建超级用户
    * python3 manage.py createsuperuser
    * 在admin.py文件中注册数据库表，使其在管理页面中显示
    * admin.site.register(Blog)
    
* pycharm中interpreter的选择
    * 安装文件为python-3.7.3-macosx10.9.pkg
    * 选择interpreter（Python解释器）的安装位置为：/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
    