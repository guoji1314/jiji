#bin/bash
#添加注释
#再次添加释
cd ~/cppcheck/cppcheck-2.4.1
echo 'cppcheck安装目录为：'
pwd
cppcheck --enable=all  $1 >~/$2/cppcheck_`date +%Y%m%d%H%M`.txt 2>&1
