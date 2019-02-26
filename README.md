# 2.26智能一点算法工程师一面
  1.sequence to sequence 模型怎么进行翻译？
    编码输入rnn,然后rnn怎么解码的，可以找到翻译效果最好的翻译句子，（参考维特比的方法）
    
  2.梯度问题怎么导致的，公式推导，门结构怎么解决的梯度问题，从公式说明？
 
  3.情感分类，P,N，中三类，通过调整阈值可以控制recall（预测数量，）和 precision（预测正确数量）怎么画出recall和precision的曲线？
  
    暴力解法不太好，每个例子都有一个预测概率p， 排序，然后依次计算precision，遍历一遍即可。时间复杂度是多少？
    
  4.两个有序数组，合并成一个？复杂度？
    def rank(a,b)：
       la =len(a)
       lb = len(b)
       if la==0:return b
       if lb ==0 :return a
       i,j,c =0,0,[]
       while True:
        if a<la and a[i]<b[j]:
          c.append(a[i])
          i +=1
        if j<lb and a[i]>=b[j]:
          c.append[b[j])
          j +=1
        elif i==la-1 and j==lb-1:
          return c
    5. 你情感分析里的 w2v 和 3-gram特征怎么用的
    
# 财富引擎一面
  
    
