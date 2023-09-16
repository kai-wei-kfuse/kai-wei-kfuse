### 此仓库用于作业代码提交
# 作业2：个人项目：论文查重算法



| 作业所属课程 | [计科21级12班 班级博客 ](https://edu.cnblogs.com/campus/gdgy/CSGrade21-12) |
| ------------ | ------------------------------------------------------------ |
| 作业要求     | [个人项目 - 作业 ](https://edu.cnblogs.com/campus/gdgy/CSGrade21-12/homework/13014) |
| 作业目标     | 设计一个论文查重算法                                         |

作业github地址：[kai-wei-kfuse/kai-wei-kfuse (github.com)](https://github.com/kai-wei-kfuse/kai-wei-kfuse)

（test.py文件即为代码文件，如需要运行，则按以下路径打开"论文查重/dist/test/test.exe"）

1. 在Github仓库中新建一个学号为名的文件夹，同时在博客正文首行给出作业github链接。**（3'）**
2. 在开始实现程序之前，在下述PSP表格记录下你估计将在程序的各个模块的开发上耗费的时间。**（6'）**
3. 计算模块接口的设计与实现过程。设计包括代码如何组织，比如会有几个类，几个函数，他们之间关系如何，关键函数是否需要画出流程图？说明你的算法的关键（不必列出源代码），以及独到之处。**（18'）**
4. 计算模块接口部分的性能改进。记录在改进计算模块性能上所花费的时间，描述你改进的思路，并展示一张性能分析图（由VS 2017/JProfiler的性能分析工具自动生成），并展示你程序中消耗最大的函数。**（12'）**
5. 计算模块部分单元测试展示。展示出项目部分单元测试代码，并说明测试的函数，构造测试数据的思路。并将单元测试得到的测试覆盖率截图，发表在博客中。**（12'）**
6. 计算模块部分异常处理说明。在博客中详细介绍每种异常的设计目标。每种异常都要选择一个单元测试样例发布在博客中，并指明错误对应的场景。**（6'）**
7. 在你实现完程序之后，在附录提供的PSP表格记录下你在程序的各个模块上实际花费的时间。**（3'）**

## 一、模块接口的设计与实现过程

论文查重程序使用了github上开源的语言识别模型。

![image-20230916114854480](https://image-host-lzq.oss-cn-guangzhou.aliyuncs.com/image-20230916114854480.png)

## 二、计算模块接口部分的性能改进

性能测试使用**cProfile 模块**进行性能测试。

![image-20230916115006443](https://image-host-lzq.oss-cn-guangzhou.aliyuncs.com/image-20230916115006443.png)

## 三、计算模块部分单元测试展示

测试数据1： orig.txt对比orig_0.8_add.txt

![image-20230916114854480](https://image-host-lzq.oss-cn-guangzhou.aliyuncs.com/image-20230916114854480.png)

测试数据2： orig_0.8_del.txt对比orig_0.8_dis_1.txt

![image-20230916115624609](https://image-host-lzq.oss-cn-guangzhou.aliyuncs.com/image-20230916115624609.png)

测试数据3： orig.txt对比orig_0.8_del.txt

![image-20230916120043318](https://image-host-lzq.oss-cn-guangzhou.aliyuncs.com/image-20230916120043318.png)

## 四、计算模块部分异常处理说明

在将导入的库打包的过程中遇到很多问题，首先尝试直接将库直接塞进程序所在文件，导致程序无法导入库，发现是有的依赖没有放入文件。

![0b0e0c26c0ba816b158729f3a893375](https://image-host-lzq.oss-cn-guangzhou.aliyuncs.com/0b0e0c26c0ba816b158729f3a893375.png)

接着，找到了所有依赖库，但是依然有新的报错。

![db4377199fa367ca7e373003627eb0e](https://image-host-lzq.oss-cn-guangzhou.aliyuncs.com/db4377199fa367ca7e373003627eb0e.png)

最后使用了Pyinstaller库自动把程序打包解决了问题。

## 附录：PSP表格

|                 PSP2.1                  |    Personal Software Process Stages     | 预估耗时（分钟） | 实际耗时（分钟） |
| :-------------------------------------: | :-------------------------------------: | :--------------: | ---------------- |
|                Planning                 |                **计划**                 |                  |                  |
|               · Estimate                |       · 估计这个任务需要多少时间        |        30        | 30               |
|               Development               |                **开发**                 |                  |                  |
|               · Analysis                |       · 需求分析 (包括学习新技术)       |       300        | 180              |
|              · Design Spec              |             · 生成设计文档              |       120        | 30               |
|             · Design Review             |               · 设计复审                |        60        | 30               |
|            · Coding Standard            | · 代码规范 (为目前的开发制定合适的规范) |        20        | 20               |
|                · Design                 |               · 具体设计                |        60        | 60               |
|                · Coding                 |               · 具体编码                |       180        | 180              |
|              · Code Review              |               · 代码复审                |        60        | 60               |
|                 · Test                  | · 测试（自我测试，修改代码，提交修改）  |       180        | 180              |
|                Reporting                |                **报告**                 |                  |                  |
|              · Test Repor               |               · 测试报告                |       120        | 60               |
|           · Size Measurement            |              · 计算工作量               |        20        | 10               |
| · Postmortem & Process Improvement Plan |     · 事后总结, 并提出过程改进计划      |        20        | 20               |
|                                         |                 · 合计                  |       1230       | 800              |

