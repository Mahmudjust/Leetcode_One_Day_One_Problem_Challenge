# The problem 
Find Mode in Binary Search Tree

Mode is the  node which has maximum frequency. 

# The approach

We need to check every node and count how many times it's occurred.The most occurred nodes is denoted as mode.

Here is my approach:
1. initialize a hash map counter.
2. Create a dfs function and increment the  frequency of nodes into counter
3. check counter and find the maximum value of it as maxfreq
4. use a list and iterate over counter to find the maxfreq and add it to the list
5. return list
