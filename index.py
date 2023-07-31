def solution(inputArray):
    def is_one_char_apart(str1, str2):
        diff_count = 0
        for c1, c2 in zip(str1, str2):
            if c1 != c2:
                diff_count += 1
            if diff_count > 1:
                return False
        return diff_count == 1
    
    def backtrack(index):
        if index == len(inputArray):
            return True
        
        for i in range(index, len(inputArray)):
            inputArray[index], inputArray[i] = inputArray[i], inputArray[index]
            if index == 0 or is_one_char_apart(inputArray[index - 1], inputArray[index]):
                if backtrack(index + 1):
                    return True
            inputArray[index], inputArray[i] = inputArray[i], inputArray[index]  # Backtrack
        return False
    
    return backtrack(0)

