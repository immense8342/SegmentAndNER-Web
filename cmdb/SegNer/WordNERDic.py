WordDic = {
    # 形容词大类
    'a': 'n2',  # 形容词
    'ad': 'n2',  # 副行词
    'ag': 'n2',  # 形语素
    'an': 'n2',  # 名形词

    'c': 'n16',  # 连词
    'b': 'n8',  # 区别词

    #副词大类
    'd':'n11', #副词
    'dg':'n11', #副语素
    'e':'n18', #叹词

    'f':'n4',  #方位词
    'i':'n23', #成语
    'm':'n5', #数词

    #名词大类
    'n':'n0', #名词
    'ng':'n0', #名语素
    'nr':'n0', #人名
    'ns':'n0', #地名
    'nt':'n0', #机构团体
    'nx':'n0', #字母专名
    'nz':'n0', #其他专名

    'o':'n13',#拟声词
    'p':'n15',#介词
    'r':'n6',#代词
    's':'n7',#处所词

    't':'n3',#时间词
    'tg':'n3',#时语素

    #助词大类
    'u':'n17', #助词
    'ud':'n17', #结构助词
    'ug':'n17', #时态助词
    'uj':'n17', #结构助词的
    'ul': 'n17',  # 时态助词了
    'uv': 'n17',  # 结构助词地
    'uz': 'n17',  # 结构助词着

    #动词大类
    'v':'n1', #动词
    'vd': 'n1',  #副动词
    'vg': 'n1',  # 动语素
    'vn':'n1', #名动词

    'w':'n19', #标点符号
    'y':'n12', #语气词
    'z': 'n9' #状态词
}



if __name__ == '__main__':
    print(WordDic.setdefault('dy','n22'))