from ltp import LTP

ltp = LTP()
seg, hidden = ltp.seg(['''我很喜欢晴天'''])
print(seg[0])
print(hidden)
pos = ltp.pos(hidden)
print(pos)
ner = ltp.ner(hidden)
print(ner)
srl = ltp.srl(hidden)
print(srl)
dep = ltp.dep(hidden)
print(dep)
主语 = -1
谓语 = -1
宾语 = -1
for d in dep[0]:
    if d[2] == 'SBV':
        主语 = d[0] - 1
        谓语 = d[1] - 1
    if d[2] == 'VOB':
        宾语 = d[0] - 1
print('主语：', seg[0][主语], '  谓语：', seg[0][谓语], '  宾语：', seg[0][宾语])
sdp = ltp.sdp(hidden)
print(sdp)
