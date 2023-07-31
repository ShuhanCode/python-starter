def anagram(s1, s2):
    """
    Problem: Anagram Check

    Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word). 

    For example:
        "public relations" is an anagram of "crap built on lies."        
        "clint eastwood" is an anagram of "old west action"
        
    **Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".**
    
    >>> anagram('go go go', 'gggooo')
    True
    >>> anagram('abc', 'cba') 
    True
    >>> anagram('hi man', 'Hi     man')
    True
    >>> anagram('aabbcc', 'aabbc')
    False
    >>> anagram('123', '1 2')
    False
    """
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    return sorted(s1) == sorted(s2)
