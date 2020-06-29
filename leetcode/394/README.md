# Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].



Example 1:

    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"

Example 2:

    Input: s = "3[a2[c]]"
    Output: "accaccacc"

Example 3:

    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"

Example 4:

    Input: s = "abc3[cd]xyz"
    Output: "abccdcdcdxyz"


my testcase

    10[o]2[3[[3]]]abc2[b2[ac]de4[2[jk]e1[F]]]ef

解释 - WA：

假设，栈 digits，栈 alphas，结果字符串 result，上一个字符或字符串 prev_ele以及
当前字符 ch。
一开始，只考虑使用字符串的中的三个元素，数字、字母以及 ] 。使用 prev_ele 保存
之前访问到的字符，分别使用两个栈digits 和 alphas存储数字以及字母。
当 ch 和 prev_ele 是相同类型的时候，将之前保存在栈中的元素出栈并将当前的 ch 
连接到该元素的末尾，接着入栈进行保存。当遇上 ] 的时候，进行出栈操作。进行出栈
操作之前，首先预设 digit 为 1，若 digits 栈不为空时，digits 出栈，设置 digit
为被出栈的数字，接着就 alphas 深度，如果深度不为 0，则此时从 alphas 出栈一个
元素，然后重复 digit 次并拼接在一起，如果此时 alphas 栈在出栈之前，栈的深度
为 1，那么在出栈之后，此时栈为空，那么需要将拼接起来的字符串拼接到需要返回的
结果字符串 result 中，否则拼接到 alphas 栈顶元素末尾进行保存。而如果 alphas 栈
的深度为 0，则此时将结果字符串重复 digit 次，然后重新赋值给结果字符串。

解释 - AC：

还是使用双栈的解法。
由于不存在 3a 或 2[4] 这样子的连续字符，那么也就只能存在 3[a], 2[2[a]], aabc2[d]
3[a2[d]] 以及 aaabc 这样子的字符串, 而不会出现想这样子 aab2ji 字母之间存在数字的字符串。
所以 [ 之前的要么是连续的字母然后紧跟着的是数字或者是 [。则我们可以使用两个变量分别保存在
遇到 [ 之前的所有字母以及数字，然后当碰上第一个 [ 时将这两个变量保存的值分别保存到对应的栈的栈顶中，
接着将这两个变量重新设置为空字符串。最后当碰上 ] 时，进行出栈操作，分别对 digits 以及 alphas 进行
出栈。digits pop 出来的 digit * 结果字符(串) result，然后拼接到 alphas 栈顶的字符串，在赋值给结果字符串 result。
为什么是 digit * result, 而不是 digit * alphas 栈顶的元素呢？举个例子，abc2[d]，当我们进行遍历的时候，
result 一直记录下abc，然后 num 记录数字变量，当 ch 碰上 [ 时，分别将这俩个的变量保存的值进行入栈，result
压入栈 alphas，num 压入栈 digits。然后result 以及 num 分别重新设置为 ""。当进行下一次循环的时候，result
保存的是字符 o，而 2[d] 表示 d 重复 2 次，因此是 digit * result。

```python
class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = []
        digits = []
        result = ''
        string, num = '', ''
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == "[":
                digits.append(num)
                str_stack.append(result)
                result = ""
                num = ""
            elif ch == "]":
                result = str_stack.pop() + int(digits.pop()) * result
            else:
                result += ch
        return result

```

