##CT肺癌辅助诊断软件使用说明

###软件界面
- 上方是菜单栏
- 中间是图片显示界面
- 下方是图片控制模块
- 底部是


###文件结构说明

![软件目录结构](http://i.imgur.com/IKQZHYF.png)

- **CTHelper/** 是主目录，主目录下包含了三个子目录
- CTHelper/**application/**是程序所在的目录，使用到的各种库文件都在这个目录下，不可随意删改。
- CTHelper/**application/**目录下的**MainWindow.exe**是主程序，双击即可打开软件
- CTHelper/**data/**目录包含了软件运行所需要的数据，包括sqlite数据库、svm模型、以及生成的临时文件
- CTHelper/data/**images/**是图片的临时缓存区，可以定期清空以节省磁盘空间
- images目录下用于存放待预测的图像序列

*注意：请将CTHelper放在纯英文路径下，以免程序出现中文字符解析错误；待预测的图片文件使用英文命名*
###使用流程
- 打开CTHelper/application/**MainWindow.exe**，弹出主界面
- 点击![信息](http://i.imgur.com/mGwUFTy.png)按钮输入患者信息，患者姓名必填
- 点击![打开](http://i.imgur.com/BlKuKzl.png)按钮，选择预测图像序列
- 使用![左](http://i.imgur.com/InysHDj.png)和![右](http://i.imgur.com/N7xYXAS.png)按钮来前后查看图像
- 框选图像并点击**裁剪**按钮对图像进行裁剪
- 按住*shift*，单击鼠标左键选择图像的种子节点，对图像进行区域生长
- 点击![重置](http://i.imgur.com/JI7JjiA.png)可以重新截本张取图片并进行区域生长
- 在窗口的下方![阈值](http://i.imgur.com/mzlcjzu.png)可以选择区域生长算法的阈值
- 勾选/取消勾选![勾选](http://i.imgur.com/O4a6qIh.png)来预测/不预测本张图像
- 点击![预测](http://i.imgur.com/hWiU3O0.png)按钮对图像序列进行预测
- 预测稍后片刻会返回结果窗口![结果](http://i.imgur.com/DtR8TPe.png)
- **患病概率**表示对图像进行svm预测之后的患病概率；**患病概率[+]**表示对图像序列和患者信息综合进行svm预测的概率。
- 医生可以对本次预测结果进行**确认**操作，确认后，本次预测的样本会做为新的训练样本加入到训练集中。

###辅助功能

- 点击![查看](http://i.imgur.com/Mjz3NhX.png)查看过往的预测信息
![信息](http://i.imgur.com/Kk7Ecyh.png)
- 点击查看可以查看具体的诊断信息与预测结果