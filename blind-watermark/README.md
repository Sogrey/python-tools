安装
``` cmd
pip install blind-watermark
```
如何使用
命令行中使用
``` python
# 嵌入水印：
blind_watermark --embed --pwd 1234 examples/pic/ori_img.jpeg "watermark text" examples/output/embedded.png
# 提取水印：
blind_watermark --extract --pwd 1234 --wm_shape 111 examples/output/embedded.png
```