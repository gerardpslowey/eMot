import re, csv

def save_word_lists():
    # save the positive words into a list called p_list
    with open('positive-words.txt') as f:
        p_txt = f.read()
        p_list = p_txt.replace('\n',' ').replace('  ',' ').lower().split(' ')

    # save the negative words into a list called n_list
    with open('negative-words.txt') as f:
        n_txt = f.read()
        n_list = n_txt.replace('\n',' ').replace('  ',' ').lower().split(' ')

    return p_list, n_list

def check_scraped_text(p_list, n_list):

    # create empty dictionaries
    word_count_dict = {}
    word_count_positive = {}
    word_count_negative= {}
    word_count_neutral = {}

    # process the scraped text
    with open('scraped.csv', 'r', encoding='utf-8') as f:
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
                
                else:
                    if word in word_count_neutral.keys():
                        word_count_neutral[word] += 1
                    else:
                        word_count_neutral[word] = 1

        # sort on word count values in reverse
        list_dict = sorted(word_count_dict.items(), key=lambda x:x[1], reverse=True)
        list_positive = sorted(word_count_positive.items(), key=lambda x:x[1], reverse=True)
        list_negative = sorted(word_count_negative.items(), key=lambda x:x[1], reverse=True)
        list_negative = sorted(word_count_neutral.items(), key=lambda x:x[1], reverse=True)

        
        with open('word_count.csv', 'w', encoding="utf-8") as f1:
            print("Counting words..")

            for i in list_dict:
                f1.write(f'{i[0]}: {str(i[1])}\n')

        with open('word_positive.csv', 'w', encoding="utf-8") as f1:
            print("Checking positive words..")

            for i in list_positive:
                f1.write(f'{i[0]}: {str(i[1])}\n')
                
        with open('word_negative.csv', 'w', encoding="utf-8") as f1:
            print("Checking negative words..")

            for i in list_negative:
                f1.write(f'{i[0]}: {str(i[1])}\n')


        with open('word_neutral.csv', 'w', encoding="utf-8") as f1:
            print("Checking neutral words..")

            for i in list_negative:
                f1.write(f'{i[0]}: {str(i[1])}\n')

        total_word_count = len(word_count_dict)
        total_pos_words = len(word_count_positive)
        total_neg_words = len(word_count_negative)
        total_neutral_words = len(word_count_neutral)

        # calculate stats
        get_stats(total_word_count, total_pos_words, total_neg_words, total_neutral_words)

def get_stats(total_word_count, total_pos_words, total_neg_words, total_neutral_words):

    percentage_negative = int(total_neg_words/total_word_count * 100)
    percentage_positive = int(total_pos_words/total_word_count * 100)
    percentage_neutral = int(total_neutral_words/total_word_count * 100)

    print("\nTotal word count: " + str(total_word_count))
    print("Total positive words: " + str(total_pos_words) + ", which accounts for " + str(percentage_positive) + "% of all text you read.")
    print("Total negative count: " + str(total_neg_words) + ", which accounts for " + str(percentage_negative) + "% of all text you read.")
    print("Total neutral words: " + str(total_neutral_words) + ", which accounts for " + str(percentage_neutral) + "% of all text you read.")

    print("Finished!")

def main():
    p_list, n_list = save_word_lists()

    check_scraped_text(p_list, n_list)

if __name__ == '__main__':
    main()