# FastDFS接口

## 文件上传API
http://10.1.50.90:8080/group/upload

参数：

- file:上传的文件
- scene:场景
- output:输出
- path:自定义路径

## 文件删除
http://10.1.50.90:8080/group/delete

参数：

- md5:文件的摘要（md5|sha1） 视配置定
- path:文件路径

md5与path二选一
说明：md5或path都是上传文件时返回的信息，要以json方式返回才能看到（参阅浏览器上传）

