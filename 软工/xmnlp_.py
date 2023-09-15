import numpy as np
import xmnlp
from xmnlp.sv import SentenceVector
#"D:\xmnlp\xmnlp-onnx-models\sentence_vector\vocab.txt"

xmnlp.set_model('D:\\xmnlp-onnx-models')

#文件读取到query
with open('C:\\Users\\kai_wei\\Desktop\\text\\orig.txt', 'r', encoding='utf-8') as f:
    query = f.read().strip()

#文件读取到docs
with open('C:\\Users\\kai_wei\\Desktop\\text\\orig_0.8_add.txt', 'r', encoding='utf-8') as f:
    docs = f.read().strip()

sv = SentenceVector(genre='通用')
#输出路径的文件
print('query:', query)
#for doc in docs:
   # print('doc:', doc)
print('similarity:', sv.similarity(query, docs))
print('most similar doc:', sv.most_similar(query, docs))
print('query representation shape:', sv.transform(query).shape)