## 程序设计思路

*基准代码：heat_map.py*

- 提取pdf文件中文章的拼音

  首先提取pdf文件中的文本 [参考](https://zhuanlan.zhihu.com/p/260670061)

  ```python
  file_path = r'D:\……\共产党宣言.pdf'
  with pdfplumber.open(file_path) as pdf:
      for page in pdf.pages:        # 对pdf文件中的每一页
          text = page.extract_text()        # 提取当前页的文字
  ```

  然后将汉字文本转化为拼音 [参考](https://blog.csdn.net/weixin_33873846/article/details/92404504)

  ```python
  page_pinyin = pinyin.get(text, format='strip')
  ```

- count()函数统计各字符的出现次数 [参考](https://blog.csdn.net/tuliyou/article/details/110544606)

  ```python
  n = {}
  for i in article_pinyin:
      n[i] = article_pinyin.count(i)
  ```

- 构建类似键盘分布的3行10列二维数组，手动将数组的每个元素与26个字母的出现次数一一对应 [参考](https://blog.csdn.net/qq_25939803/article/details/100690582)

  比如该数组第一行的10个元素分别为字母q、w、e、r、t、y、u、i、o、p所对应的出现次数。

- 绘制热力图 [参考](https://www.cnblogs.com/LiErRui/articles/11592882.html)

  ```python
  sns.heatmap(data, cmap = 'PuBuGn', annot = True, fmt = '.0f')
  ```

  结果如图：*heat_map.png*

  ![](D:\大四上\找导师\赵志为\heat_map.png)

  可以看出，I键使用频率最高，多达7463次，N键、E键、A键、H键次之。



## 评价标准

- #### 按键使用的均衡性

  标准差能反映一个数据集的离散程度，所以使用标准差作为评价按键使用均衡性的标准。标准差越大，均衡性越低；标准差越小，均衡性越高。

  将所有键对应的出现次数处理为一维数组arr[]后，用np.std()函数计算标准差。 [参考](https://www.delftstack.com/zh/api/numpy/python-numpy-std/)

  ```python
  print("Homogeneity of key use:", np.std(arr))
  ```

  全拼输入方案的标准差为1984.492204，均衡性较低。

- #### 输入效率

  我想到的输入效率的几个影响因素有：

  - 客观因素：常用按键距离手指放置初始位置的远近、输入方案的合理性和快捷性

  - 主观因素：打字员对打字设备的熟悉度、对输入法的掌握度

  其中，主观因素的影响是最大的，键盘布局再便利，输入方案再合理再快捷，也需要打字员足够熟悉打字设备、足够掌握输入法。

  所以个人觉得难以对输入效率进行量化，一是影响因素多而复杂，二是主观因素影响大。



## 改进方向

- #### 改动键盘

  - **改进方案1：合并使用频率低的键，简化键盘为9键**

    *改进代码1：heat_map_improved1.py*

    灵感来源：以前看到过一个设计师画手用的键盘，外接使用 [设计师键盘](https://weibo.com/1808170114/Kn2KdjQue) 。所以联想到为了提高按键使用的均衡性，可以暴力合并使用频率低的键，简化键盘为9键：

    1（）          2（ABCF）  3（DGM）

    4（EKLP） 5（HJQ）    6（I）

    7（NRT）  8（UVWZ） 9（OSXY）

    电脑端需使用外接键盘，或者使用键盘右端的数字区，手机/平板端触屏影响不大。

    热力图：*heat_map_improved1.png*

    ![](D:\大四上\找导师\赵志为\heat_map_improved1.png)

    均衡性：标准差321.8713835，均衡性大幅度提高

    输入效率：按键较少，输入效率提高

    - **附原始九键结果：**

    热力图：*heat_map_9key.png*

    ![](D:\大四上\找导师\赵志为\heat_map_9key.png)

    均衡性：标准差3962.029554，均衡性非常差

  - **改进方案2：改变键的位置，使用频率高的键放中间**

    *改进代码2：heat_map_improved2.py*

    灵感来源：有些国家键盘布局不太一样，主流键盘布局为Qwerty，德国、瑞士等国家键盘布局布局为Qwertz，法国等国家键盘布局为Azerty，键盘布局不一致的原因有的是为了便于输入自己国家的语言，有的是打字机厂商自己的决定。 [不同国家键盘布局的设计](https://www.zhihu.com/question/20121876)
    
    热力图：*heat_map_improved2.png*
    
    ![](D:\大四上\找导师\赵志为\heat_map_improved2.png)
    
    均衡性：标准差1984.492204，因为只是改变了键的位置，所以均衡性没变
    
    输入效率：使用频率高的键放中间，手指移动距离短，输入效率提高

- #### 不改动键盘

  **改进方案3：使用快速全拼输入法**

  *改进代码3：heat_map_improved3.py*

  灵感来源：专利号 CN 104765467 B，专利名称“快速全拼输入法”
  
  该输入法对拼音的部分韵母和声母设置代码，在输入汉字时，对有代码的韵母和声母，是输入它们的代码而不是它们本身，比如“ang”替换为代码“asd”，使输入过程更加快捷方便。
  
  热力图：*heat_map_improved3.png*
  
  ![](D:\大四上\找导师\赵志为\heat_map_improved3.png)
  
  均衡性：标准差2030.05377，因为代码将很多字母转移到了键盘第二行的按键上，所以均衡性略有降低
  
  输入效率：代码位置容易记忆，不会颠覆原来的拼音，而使拼音输入更为方便快速

