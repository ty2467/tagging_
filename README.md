问题：
RAG( 检索增强生成 ) 的检索（retrieval)步骤在复杂，多样的向量存储的情况下会有性能弱化--原因包括分散的向量，检索在操作于大型的向量数据库时需要去比对有关和无关的向量，等。

解决方法：

为向量存储里的所有的向量化数据加上标签

实现细节：

从csv读取的数据被存在于一个二维的dictionary的第一个key内，保留一个value为空字符串的tag key为存储标签\
加tag任务由llm完成；实现中，程序将tag存为enum，在发送给llm时转化为一个由逗号分开的字符串，并让llm对待其如同于base index1的C enum。这样
tag可以变成一串每一个字符代表不同的标签class的标签的数字代表

尚未确定是否应该实现，因为成本较高，的是把所有标签一样的向量化数据存入在一个向量存储内，而检索时可以根据标签先选择向量存储。


Part 0:

1. LLM setup,
2. file reading setup, 
set up separate file search assistants. --- multiple search assistant objects.
-i could set up multi-thread, in each thread you know what your assistant is;

multiple file search assistants in multiple threads


Part 1:

pipeline to tag the items in the files, and storing them with their tag into a list
1. separate each item into an individual unit. string in a list - two dimension tag? [(item, [tag1, tag2, tag3])]. 
2. tags are stored in an enum, the ints will represent each tag; concat together the int representation of the \
tags\
so the tag list will really look like: [(item, '###'), ] --> update: tuples are immutable, so [[item, '###'], ]
3. set up a chain of llms doing the tags 
4. produce tags, add the tags into the original

VERY IMPORTANT NOTE: KNOWING HOW 1.2 WILL WORK, 1.1 WILL STORE ITEM as such: LIST[i][0] = [item, '###']\
that looks like the updated look of 1.2

UPDATE: INSTEAD OF A LIST, IT IS GOING TO BE A DICT: BETTER MANAGEMENT OF DATA, SIMPLE





Part 2:\
highlevel description\
embed the items and store them each by how they are tagged. --- given that all elements are tagged on with a permutation of the three tags, we will store them into each a separate file search assistant
who will answer the questions separately.
look at the lists and reconstruct five files -- it is safer for memory :: afterall the data is quite a bit and its not\
the safest to rely on memory: not a lot of those going around.\
DECISION: store as md, each item as 
    md_file.write(list[i][0] + "\n")

CREATE VECTOR DATABASES IN A LOOP, EACH LOOP FEEDING A DIFFERENT FILE(S) TO UPLOAD (have to be a file_path list anyways)
vector_db name will also be different: VDB_###



can i store them in file_search still and be okay:

tell 