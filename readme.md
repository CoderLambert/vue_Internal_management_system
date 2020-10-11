# 部门内部工具系统
  为了方便部门内部人员搭建的 Web 系统， 后端基于 Django 框架，前端使用 Vue 全家桶，基于 Restful Api 进行通信，当初边学 Vue 边学 Django RestframeWork 做的，那时对前端组件化了解还不够深入，所以代码可能看上去不整洁，算当时初学练手的吧

## 在线展示

[http://vue.25years.xyz/](http://vue.25years.xyz/#/articles/)

## 环境安装
- 后端
  1. pip install -r requirement.txt
  2. 使用 sqlite 数据库，直接下载代码后就可以启动了
  4. python manage.py runserver localhost:port
- 前端
   1. cd app_front
   2. npm install
   

登陆用户名： lambert   密码：1234

## 使用到的主要技术

## 后端

  1. Django

  2. Django-RestFramWork

  3. Sqlite

  4. JWT

     

## 前端

    1. Vue
    2. Vuex
    3. vue-bus
    4. vue-clipboard2
    5. vue-router
    6. axios
    7. element-ui
    8. moment
    9. mavon-editor
    10. file-saver
    11. animate.css
    12. less


## 主要功能
1. 文章显示
2. 对博客文章从 作者、笔记本、分类、时间等角度进行管理，方便索引查找 
3. 支持 maven Editor
4. 支持多人注册，多角色权限管理
5. 支持全文本搜索查找
6. 支持上传镜像管理，并自动通知所选人员
7. 支持多站点导航，记录
8. 后台 API 接口文档展示
9. 项目机器管理，方便添加、编辑机器信息
10. 项目信息记录，例如 svn path、成员、备注等



## 代码目录

- app_fornt  前端代码

- apps  后端 每个功能都作为一个单独 app，方便解耦管理 ，写的所有功能都在这个包里

- db_tools 初始化数据库，我已经将 sqlite 上传了，所以不需要使用

- Month 项目配置文件，包含路由和项目配置

- static 静态资源文件

- meida 媒体文件，上传文件存放的目录

- extra_apps 第三方 app ，目前没用到

  

## 联系我
如果你对该站点有好的建议，请用以下方式联系我

QQ: 156486648

微信: L156486648