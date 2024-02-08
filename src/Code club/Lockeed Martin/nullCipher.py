vowels: list[str] = ["a", "e", "i", "o", "u"]
ciphered: str = input("Null Cipher Ciphered text: ")
plaintextArr: list[str] = []

def isAVowel(character: str) -> bool:
    return character in vowels

def decrypt(character: str) -> str:
    return character
  
def main() -> None:
    for index in range(len(ciphered) - 1):
        char = ciphered[index]
        if isAVowel(char) and (isAVowel(ciphered[index - 1]) and ciphered[index - 1] in vowels):
            break
        if isAVowel(char):
            #plaintextArr.append(char)
            plaintextArr.append(ciphered[index + 1])
        

if __name__ == "__main__":
    main()
    print(plaintextArr)
