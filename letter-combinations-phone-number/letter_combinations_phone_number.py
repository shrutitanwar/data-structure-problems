# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        digit_mapping = {
            "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
        }
        
        current_vals = [""]
        for d in digits:
            next_vals = []
            for val in current_vals:
                for ch in digit_mapping[d]:
                    next_vals.append(val+ch)
            current_vals = next_vals
            print(current_vals)
        return current_vals
                    
