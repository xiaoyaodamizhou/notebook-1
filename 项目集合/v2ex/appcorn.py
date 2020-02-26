import main


app = main.configured_app()


# https://www.jianshu.com/p/65fae00615b9
# 配置gunicorn启动配置文件,在项目的根目录创建一个gun.conf,写入以下内容:
'''
import gevent.monkey
import multiprocessing
import os


gevent.monkey.patch_all()


if not os.path.exists('log'):
    os.mkdir('log')


debug = True
loglevel = 'debug'
bind = '127.0.0.1:8000'
pidfile = 'log/gunicorn.pid'
logfile = 'log/debug.log'
errorlog = 'log/error.log'
accesslog = 'log/access.log'
# 启动的进程数
workers = multiprocessing.cpu_count() * 2 + 1
# 使用gevent模式，还可以使用sync 模式，默认的是sync模式
worker_class = 'gnicorn.workers.ggevent.GeventWorker'
x_forwarded_for_header = 'X-FORWARDED-FOR'
'''
# gunicorn 运行程序
# nohup gunicorn -k gevent -c gun.conf appcorn:app &
# nohup gunicorn -b '0.0.0.0:2000' appcorn:app &


# nginx 配置
# 另外启动一个终端 打开/etc/nginx/sites-enabled/，备份default文件后,在default加入以下内容
'''
server {
        listen   80;
        server_name  公网IP或者你已经解析的域名;
        location / {
            add_header Access-Control-Allow-Origin * always;
            add_header Access-Control-Allow-Methods 'GET, POST, OPTIONS' always;
            add_header Access-Control-Allow-Headers 'DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization';
            
            if ($request_method = 'OPTIONS') {
                return 204;
            }
                
            proxy_pass http://127.0.0.1:8000;
            proxy_redirect off;
            proxy_set_header Host $host:80;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
'''
# 然后输入以下命令检查nginx配置文件是否有错: sudo nginx -t
# 启动nginx
'''
sudo service nginx start
sudo nginx -s reload
'''

# 关于使用api接口的解释：先用js处理页面，总用js中的ajax发送
# 数据通过当中的url找到后端python写的对应视图函数，同样
# ajax可也通过content-type指定表单header中body的数据类型
# 然后视图函数通过request.args,request.form,request.json, request.get_json()
# 来获取ajax返回的数据，在对数据做出处理返回处理后的数据
# 发送响应表单，然后ajax接受响应表单中是success还是error
# 来做出相应的处理
# 什么时候可以用request.json呢，就是ajax指明了content-type是json类型

