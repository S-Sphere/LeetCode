# 217. Contains Duplicate

> **Problem Link:**
> https://leetcode.com/problems/contains-duplicate/


## Solution 1

**Time Complexity:** O(n)
* **'n'** is the number of elements in the input list **'nums'**. The code iterates through the list once.

**Space Complexity:** O(n)
* because the code uses a dictionary **'numsdict'** to store unique elements encountered so far. In the worst case, where all elements in **'nums'** are distinct, the dictionary will have to store all **'n'** elements.

### Code Explanation

1. The code initializes an empty dictionary **'numsdict'** to keep track of unique elements encountered.
2. It then iterates through each element **'num'** in the input list **'nums'**.
3. For each element, it checks if **'num'** is already present in the dictionary.
   * If **'num'** is found in the dictionary, it means that there is a duplicate, and the function returns **'True'**.
   * If **'num'** is not found in the dictionary, it adds **'num'** to the dictionary with a value of 1.
4. If the loop completes without finding any duplicates, the function returns **'False'**.


## Solution 2


**Time Complexity:** O(n)
* The code creates a set from the input list, and set creation has a time complexity of O(n), where **'n'** is the number of elements in the input list **'nums'**.

**Space Complexity:** O(n)
* The space complexity is O(n) due to the creation of the set. In the worst case, where all elements in **'nums'** are distinct, the set will have to store all **'n'** elements.

### Code Explanation

1. **Set Creation:** The code starts by creating a set (**'numsset'**) from the input list (**'nums'**). This has the effect of removing any duplicate elements since sets only store unique values.

2. **Length Comparison:**
   - It then calculates the lengths of the original list (**'l1'**) and the set (**'l2'**). The length of the set represents the number of unique elements in the original list.

3. **Duplicate Check:**
   - It checks if the lengths of the original list and the set are different (**'if l1 != l2'**).
     - If the lengths are different, it means that there were duplicates in the original list, and the function returns **'True'**.
     - If the lengths are the same, it indicates that there are no duplicates, and the function returns **'False'**.


