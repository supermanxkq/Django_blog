from django.shortcuts import render
from django.shortcuts import redirect
from blog.models import Blog
from django.http import HttpResponse
# 1.导出excel的库
import xlwt
# 2.实现了在内存中读写bytes
from io import BytesIO


# Create your views here.

# 进入博客的首页
def index(request):
    blogs = Blog.objects.all()
    return render(request, "blog.html", {'blog': blogs})

# 查看文章详情
def to_blog_page(request, article_id):
    blog = Blog.objects.get(pk=article_id)
    print(blog)
    return render(request, 'article_page.html', {'article': blog});

# 删除博客数据
def blog_delete(request, article_id):
    Blog.objects.filter(id=article_id).delete()
    return redirect('/index')

# 更新博客数据
def edit_action(request):
    article_id = request.POST.get('id', 'ID')
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    Blog.objects.filter(id=article_id).update(title=title, content=content)
    return redirect('/index/')


# 进入编辑页面
def edit_page(request, article_id):
    article = Blog.objects.get(pk=article_id)
    return render(request, 'edit_page.html', {'article': article});


# 进入新增页面
def create_page(request):
    return render(request, 'create_page.html');

# 添加新的博客
def create_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    Blog.objects.create(title=title, content=content)
    return redirect('/index')


# 导出excel数据
def export_excel(request):
    # 设置HTTPResponse的类型
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=order.xls'
    # 创建一个文件对象
    wb = xlwt.Workbook(encoding='utf8')
    # 创建一个sheet对象
    sheet = wb.add_sheet('order-sheet')

    # 设置文件头的样式,这个不是必须的可以根据自己的需求进行更改
    style_heading = xlwt.easyxf("""
            font:
                name Arial,
                colour_index white,
                bold on,
                height 0xA0;
            align:
                wrap off,
                vert center,
                horiz center;
            pattern:
                pattern solid,
                fore-colour 0x19;
            borders:
                left THIN,
                right THIN,
                top THIN,
                bottom THIN;
            """)

    # 写入文件标题
    sheet.write(0, 0, '序号', style_heading)
    sheet.write(0, 1, '标题', style_heading)
    sheet.write(0, 2, '内容', style_heading)

    # 写入数据
    data_row = 1
    # UserTable.objects.all()这个是查询条件,可以根据自己的实际需求做调整.
    for i in Blog.objects.all():
        # 格式化datetime
        sheet.write(data_row, 0, i.id)
        sheet.write(data_row, 1, i.title)
        sheet.write(data_row, 2, i.content)
        data_row += 1
    # 写出到IO
    output = BytesIO()
    wb.save(output)
    # 重新定位到开始
    output.seek(0)
    response.write(output.getvalue())
    return response
