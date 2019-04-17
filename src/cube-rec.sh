#!/bin/sh
echo "正在运行：run.py"
python run.py
echo "run.py 运行结束"
echo "正在运行：a.out"
./a.out
echo "a.out 运行结束"
echo "正在运行：String_.py"
python String_.py
echo "String_.py 运行结束"
echo "正在编译arduino文件"
make
echo "编译结束"
echo "正在上传arduino程序"
make upload
echo "上传完成！"

