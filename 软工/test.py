import cProfile
import numpy as np
import sys

sys.path.append('/xmnlp')
sys.path.append('/onnxruntime')
sys.path.append('/scikit-learn')
sys.path.append('/numpy')
sys.path.append('/tokenizers')

import xmnlp
#import xmnlp
from xmnlp.sv import SentenceVector
#"D:\xmnlp\xmnlp-onnx-models\sentence_vector\vocab.txt"


def my_function():
    xmnlp.set_model('xmnlp-onnx-models/')

    #命令行读取文件路径
    #C:\\Users\\kai_wei\\Desktop\\text\\orig_0.8_del.txt
    #C:\\Users\\kai_wei\\Desktop\\text\\orig_0.8_dis_1.txt
    query_path = input('请输入文件1的路径(请用正斜杠)：')
    docs_path = input('请输入文件2的路径：')
    #文件读取到query
    with open(query_path, 'r', encoding='utf-8') as f:
        query = f.read().strip()

    #文件读取到docs
    with open(docs_path, 'r', encoding='utf-8') as f:
        docs = f.read().strip()

    sv = SentenceVector(genre='通用')
    #输出路径的文件
    #print('query:', query)
    #for doc in docs:
    # print('doc:', doc)
    print('文本相似度', sv.similarity(query, docs))
    #print('most similar doc:', sv.most_similar(query, docs))
    print('query representation shape:', sv.transform(query).shape)

"""
   ncalls：表示函数调用的次数；
    tottime：表示指定函数的总的运行时间，除掉函数中调用子函数的运行时间；
    percall：（第一个percall）等于 tottime/ncalls；
    cumtime：表示该函数及其所有子函数的调用运行的时间，即函数开始调用到返回的时间；
    percall：（第二个percall）即函数运行一次的平均时间，等于 cumtime/ncalls；
    filename:lineno(function)：每个函数调用的具体信息；
"""

if __name__ == "__main__":
    
    profiler = cProfile.Profile()
    profiler.run('my_function()')
    profiler.print_stats()
