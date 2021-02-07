from collections import Counter
entrydivider = "["
text_list = list(filter(lambda x: (entrydivider not in x), list(filter(lambda x: (x != ""), open("data.txt").read().splitlines()))))
main_dict = {}
for i in text_list:
    try:
        k = i.split(" - ") #k[0] is name and k[1] is their score
        if k[0] in main_dict: main_dict[k[0]] += int(k[1])/2
        else: main_dict[k[0]] = int(k[1])
    except:print("Fix - " + str(k))
ranker = dict(Counter(main_dict).most_common(5))
print(ranker)
