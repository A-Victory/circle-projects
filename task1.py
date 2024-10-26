def count_vowels(sentence):

    vowels = 'aeiouAEIOU'
    count = 0

    for vowels in sentence:
        if vowels in 'aeiou':
            count += 1

    return count

sentence = input("Enter a sentence: ")
vowels_count = count_vowels(sentence)

print("The number of vowels in the sentence is: %d" % vowels_count)