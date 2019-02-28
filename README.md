### 2.26智能一点算法工程师一面
 1.sequence to sequence 模型怎么进行翻译？
    编码输入rnn,然后rnn怎么解码的，可以找到翻译效果最好的翻译句子，（参考维特比的方法）
    
   sequence to sequence 模型 https://zhuanlan.zhihu.com/p/43405406   
    
 2.梯度问题怎么导致的，公式推导，门结构怎么解决的梯度问题，从公式说明？
 
  https://blog.csdn.net/qq_28031525/article/details/79423450
  
 3.情感分类，P,N，中三类，通过调整阈值可以控制recall（预测数量，）和 precision（预测正确数量）怎么画出recall和precision的曲线？
  
    暴力解法不太好，每个例子都有一个预测概率p， 排序，然后依次计算precision，遍历一遍即可。时间复杂度是多少？
    
 4.两个有序数组，合并成一个？复杂度？
 
    [我这么写的]:https://github.com/BuaaAlban/Interview-summery/blob/master/concatlist.py
         `
 5. 你情感分析里的 w2v 和 3-gram特征怎么用的?
 
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
  
    
