# README

周末花时间学习一下tensorboard的学习使用。

- `0_image_graph`是简单使用tensorboard的加载数据集和查看模型的例子
- `1_summary_writer`是使用`SummaryWriter`来记录训练过程的例子
  - 这里写了一个简单的decoder模仿stable-diffusion的过程
  - 这里顺便学了下怎么命名比较规范
- `3_add_scalar`是随便画一下多个变量在一个board上的例子
- `4_add_histogram`是利用`add_histogram`来画直方图的例子
  - 在本地没配好环境，这里的notebook是在colab上跑的
  - 加深一下对scale dot product attention的理解

## refer🔗

- https://pytorch.org/docs/stable/tensorboard.html