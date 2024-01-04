# 242. Valid Anagram

> **Problem Link:**
> https://leetcode.com/problems/valid-anagram/


## Solution

**Time Complexity:** O(n)
* The code iterates through both strings, and the loop runs for the length of the strings. Thus, the time complexity is O(n), where **'n'** is the length of the strings.

**Space Complexity:** O(k)
* The space complexity is O(k), where **'k'** is the number of distinct characters in both strings. In the worst case, if all characters are distinct, the dictionaries **'countS'** and **'countT'** will store all distinct characters.

### Code Explanation

1. **Length Check:** The code checks if the lengths of strings **'s'** and **'t'** are different. If they are, the function returns **False** since strings with different lengths cannot be anagrams.

2. **Dictionaries Initialization:** It initializes two dictionaries, **'countS'** and **'countT'**, to count the occurrences of each character in strings **'s'** and **'t'**.

3. **Character Counting Loop:**
   - The code iterates through each character at the same position in both strings.
   - For each character, it updates the count in the respective dictionary using the **get** method to handle cases where the character is not already present in the dictionary.

4. **Comparison:**
   - Finally, it compares the dictionaries **'countS'** and **'countT'**. If they are equal, it means that the strings are anagrams, and the function returns **True**; otherwise, it returns **False**.

