import operator


def most_frequent(str1):
    all_freq={}
    for i in str1:
        if i in all_freq:
            all_freq[i]+=1
        else:
            all_freq[i]=1
    sorted_d = dict(sorted(all_freq.items(), key=operator.itemgetter(1), reverse=True))
    return sorted_d


print("Please enter  a string")
str1=input()
dict1=most_frequent(str1)
print("Frequencies of:")
for i in dict1:
    print(i,"=",dict1[i])