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