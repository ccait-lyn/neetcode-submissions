class Solution:
    def reverseString(self, text: str) -> str:
        return text[::-1]

    def isPalindrome(self, s: str) -> bool:
        extracted = re.sub(r'[^a-zA-Z0-9]', '', s)
        lower_text = extracted.lower()
        reversed_text = self.reverseString(lower_text)

        return lower_text == reversed_text
        