"""
功能描述：语言技术平台LTP学习
运行环境：Python 3.x
作者：王佳秋
日期：2021年5月17日
"""

from ltp import LTP

ltp = LTP()
# 1 分句子
sents = ltp.sent_split(["他叫汤姆去拿外衣。", "汤姆生病了。他去了医院。"])
print("sents:", sents)
# 2 (1)用户自定义词典
ltp.init_dict(path="Dataset/user_dict.txt", max_window=4)
#   (2)也可以在代码中添加自定义的词语
ltp.add_words(words=['负重前行', '长江大桥'], max_window=4)
# 3 分词
segment, tensor = ltp.seg(["他叫汤姆去拿外衣。"])  # _是每个分词的tensor
print("分词：", segment)
print("tensor-type：", type(tensor))
print("tensor：", tensor)
# 3.1 对于已经分词的数据
segment, hidden = ltp.seg(['他/叫/汤姆/去/拿/外衣/。'.split('/')], is_preseged=True)
# 4 词性标注
seg, hidden = ltp.seg(['他叫汤姆去拿外衣。'])
pos = ltp.pos(hidden)
print("分词：\n", seg)
print("词性标注：\n", pos)
# 5 命名实体识别
seg, hidden = ltp.seg(['他叫汤姆去拿外衣。'])
ner = ltp.ner(hidden)
print("命名实体识别ner:", ner)
tag, start, end = ner[0][0]
print(tag, ":", "".join(seg[0][start:end + 1]))
# 6 语义角色标注
seg, hidden = ltp.seg(['他叫汤姆去拿外衣。'])
srl = ltp.srl(hidden)
print("语义角色标注：\n", srl)
srl = ltp.srl(hidden, keep_empty=False)
print("形式化-语义角色标注：\n", srl)
# 7 依存句法分析
dep = ltp.dep(hidden)
print("依存句法分析：\n", dep)
# 8 语义依存分析
segment1, hidden = ltp.seg(["他叫汤姆去拿外衣。"])
sdp = ltp.sdp(hidden)
print("语义依存分析：\n", sdp)
