### 面试总结网址

     暑期实习生-自然语言处理算法岗-面试题 https://blog.csdn.net/qq_28031525/article/details/80028055
     剑指offer python  https://blog.csdn.net/u012505432/article/details/52071537
     算法工程师/机器学习工程师”的笔试和面试总结 https://blog.csdn.net/duxinyuhi/article/details/78051042
     自然语言处理（NLP）算法：概述与分类 https://blog.csdn.net/weixin_39449466/article/details/81277403
     刷题：牛客 https://www.nowcoder.com     leetcode  https://leetcode.com/ 
     

### 2.26智能一点算法工程师一面
 1.sequence to sequence 模型怎么进行翻译？
    编码输入rnn,然后rnn怎么解码的，可以找到翻译效果最好的翻译句子，（参考维特比的方法）
    
    sequence to sequence 模型 https://zhuanlan.zhihu.com/p/25366912
   
    注意力模型 https://zhuanlan.zhihu.com/p/43405406   
    
    rnn用于机器翻译 https://blog.csdn.net/aliceyangxi1987/article/details/71055235
    
 2.梯度问题怎么导致的，公式推导，门结构怎么解决的梯度问题，从公式说明？
 
     https://blog.csdn.net/qq_28031525/article/details/79423450
  
 3.情感分类，P,N，中三类，通过调整阈值可以控制recall（预测数量，）和 precision（预测正确数量）怎么画出recall和precision的曲线？
  
    暴力解法不太好，每个例子都有一个预测概率p， 排序，然后依次计算precision，遍历一遍即可。时间复杂度是多少？
    
 4.两个有序数组，合并成一个？复杂度？
 
    [我这么写的]:https://github.com/BuaaAlban/Interview-summery/blob/master/concatlist.py
         `
 5.你情感分析里的 w2v 和 3-gram特征怎么用的?
 
 6.机器学习里的评价指标 
 
    https://zhuanlan.zhihu.com/p/43405406
    
    
### 财富引擎一面

1.100万个数字找到前十大？堆排序

2.继承父类

3.Deepcopy 和copy ？

    https://iaman.actor/blog/2016/04/17/copy-in-python

4.链表和数组做查询，选择哪个？为什么？

    https://blog.csdn.net/qq_25806863/article/details/70607204

5.极大似然估计和贝叶斯估计的区别和原理

    https://blog.csdn.net/liu1194397014/article/details/52766760

    https://blog.csdn.net/bitcarmanlee/article/details/52201858

    最本质的区别是:

    最大似然是对点估计，贝叶斯推断是对分布估计。即，假设求解参数θ，最大似然是求出最有可能的θ值，而贝叶斯推断则是求解θ的分布。
    在公式上，贝叶斯推断还引入了先验，通过先验和似然来求解后验分布，而最大似然直接使用似然函数，通过最大化其来求解。

6.参数估计方法和非参数估计方法有哪些？

    参数估计：最大似然估计MLE、最大后验概率估计MAP及贝叶斯估计

    非参数估计：直方图法、Kn近邻估计法、Parzen窗法

7.Adam优化方法为什么好？

8.Q-learning的基本原理

### 3.1 号xilinx一面 

1.介绍一下rnn和lstm 梯度问题

2.如果解决过拟合问题

     增大数据量；换激活函数，relu, tanh, leaky-relu; dropout ; 正则项（正则项怎么解决的过拟合）

3.优化算法了解过么？

     不太了解，大概知道有 minibatch-sgd sgd adam等

4.x正实数， 求根号三次下的x

     二分法，注意x<1 和x>1的情况
     
5.给一个字符串，求最大回文数长度？

     leetcode上原题，我发现在一年前的commit上写的 #讨论区答案，我没看懂 哈哈哈
     
     https://leetcode.com/problems/longest-palindromic-substring/
     
## 自己瞎整理的有用的问题？？？

1.l1正则与l2正则的特点是什么，各有什么优势？

     https://www.zhihu.com/question/26485586

2.Linear SVM 和 LR 的联系和区别

    https://blog.csdn.net/haolexiao/article/details/70191667
