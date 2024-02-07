vowels: list[str] = ["a", "e", "i", "o", "u"]
ciphered: str = input("Null Cipher Ciphered: ")
plaintextArr: list[str] = []

def isAVowel(character: str) -> bool:
    return character in vowels
  


def main() -> None:
    for index in range(len(ciphered) - 1):
        char = ciphered[index]
        #if isAVowel(ciphered[index - 1]):
          #break
        if isAVowel(char):
            plaintextArr.extend([char, ciphered[index + 1]])

if __name__ == "__main__":
    main()
    #print(plaintextArr)
