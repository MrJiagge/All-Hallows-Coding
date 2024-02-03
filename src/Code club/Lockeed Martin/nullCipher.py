vowels: list[str] = ["a", "e", "i", "o", "u"]
ciphertext: str = input("Null Cipher Ciphertext: ")
plaintextArr: list[str] = []

def isAVowel(character: str) -> bool:
    return character in vowels
  


def main() -> None:
    for index in range(len(ciphertext) - 1):
        char = ciphertext[index]
        #if isAVowel(ciphertext[index - 1]):
          #break
        if isAVowel(char):
            plaintextArr.extend([char, ciphertext[index + 1]])

if __name__ == "__main__":
    main()
    #print(plaintextArr)
