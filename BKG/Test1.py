import hanlp

HanLP = hanlp.load(hanlp.pretrained.mtl.UD_ONTONOTES_TOK_POS_LEM_FEA_NER_SRL_DEP_SDP_CON_XLMR_BASE)  # 世界最大中文语料库

print(HanLP(['散热器的油道厚度不应小于9mm。']))



