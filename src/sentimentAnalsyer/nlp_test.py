import re, json, csv

# save the positive words into a list called p_list
with open('positive-words.txt') as f:
    p_txt = f.read()
    p_list = p_txt.replace('\n',' ').replace('  ',' ').lower().split(' ')

# save the negative words into a list called n_list
with open('negative-words.txt') as f:
    n_txt = f.read()
    n_list = n_txt.replace('\n',' ').replace('  ',' ').lower().split(' ')

# create empty dictionaries
word_count_dict = {}
word_count_positive = {}
word_count_negative= {}

# process the scraped text
with open('scraped.csv', encoding='utf-8') as f:
    csv_reader = csv.reader(f, delimiter=',')

    for row in csv_reader:
        for word in row:
            # count all words frequency
            if word in word_count_dict.keys():
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1

            # count if it is a positive word
            if word in p_list:
                if word in word_count_positive.keys():
                    word_count_positive[word] += 1
                else:
                    word_count_positive[word] = 1

            # else see if it is a negative word
            elif word in n_list:
                if word in word_count_negative.keys():
                    word_count_negative[word] += 1
                else:
                    word_count_negative[word] = 1

            # no match
            else:
                pass
			
    # sort on word count values in reverse
    list_dict = sorted(word_count_dict.items(), key=lambda x:x[1], reverse=True)
    list_positive = sorted(word_count_positive.items(), key=lambda x:x[1], reverse=True)
    list_negative = sorted(word_count_negative.items(), key=lambda x:x[1], reverse=True)

    with open('word_count.csv', 'w', encoding="utf-8") as f1:
        for i in list_dict:
            f1.write('{}: {}\n'.format(i[0],str(i[1])))

    with open('word_positive.csv', 'w', encoding="utf-8") as f1:
        for i in list_positive:
            f1.write('{}: {}\n'.format(i[0],str(i[1])))
            
    with open('word_negative.csv', 'w', encoding="utf-8") as f1:
        for i in list_negative:
            f1.write('{}: {}\n'.format(i[0],str(i[1])))
