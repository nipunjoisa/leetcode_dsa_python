class Solution:

  def intToRoman(self, num: int) -> str:
    romans = [                              #subtract greedily. O(1) constant lookup space
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]

    res = ''       #O(n) space occupation
    for val, symbol in romans:   #O(1), fixed number of iterations for every input.
      while num >= val: 
        res+=symbol
        num -= val

    return ''.join(res)

# Time: O(1) - Fixed 13-symbol lookup table; max 15 iterations since 1 <= num <= 3999 (worst case: 3888 -> "MMMDCCCLXXXVIII").
# Space: O(1) - Output list `res` holds at most 15 chars due to the 3999 upper bound (also O(1) auxiliary space).
