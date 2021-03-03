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
    word_count_dict= {}
    word_count_positive= {}
    word_count_negative= {}
    word_count_neutral= {}

    # process the scraped text
    with open('scraped.csv', 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            for word in row:
                word_counter(word, p_list, n_list, word_count_dict, word_count_positive, word_count_negative, word_count_neutral)

        # sort on word count values in reverse
        # list_dict, list_positive, list_negative, list_neutral
        list_dict = sorted(word_count_dict.items(), key=lambda x:x[1], reverse=True)
        csv_result_writer(list_dict, 'word_count.csv', "Counting words..")

        list_positive= sorted(word_count_positive.items(), key=lambda x:x[1], reverse=True)
        csv_result_writer(list_positive, 'word_positive.csv', "Checking positive words..")

        list_negative = sorted(word_count_negative.items(), key=lambda x:x[1], reverse=True)
        csv_result_writer(list_negative, 'word_negative.csv', "Checking negative words..")

        list_neutral = sorted(word_count_neutral.items(), key=lambda x:x[1], reverse=True)
        csv_result_writer(list_neutral, 'word_neutral.csv', "Checking neutral words..")

        # calculate stats
        # total_word_count, total_pos_words, total_neg_words, total_neutral_words
        get_stats(len(word_count_dict), len(word_count_positive), len(word_count_negative), len(word_count_neutral))

def word_counter(word, p_list, n_list, wcdict, wcpos, wcneg, wcneut):
    
    # add first count if word is not found, else increment it
    wcdict[word] = 1 if word not in wcdict.keys() else +1

    # positive word counter
    if word in p_list:
        wcpos[word] = 1 if word not in wcpos.keys() else +1

    # negative word counter
    elif word in n_list:
        wcneg[word] = 1 if word not in wcneg.keys() else +1

    # neutral word counter
    else:
        wcneut[word] = 1 if word not in wcneut.keys() else +1

def csv_result_writer(list_, word_file, message):
    with open(word_file, 'w', encoding="utf-8") as f1:
        print(message)

        for i in list_:
            f1.write(f'{i[0]}: {i[1]}\n')

def get_stats(total_word_count, total_pos_words, total_neg_words, total_neutral_words):

    percentage_negative = int(total_neg_words/total_word_count * 100)
    percentage_positive = int(total_pos_words/total_word_count * 100)
    percentage_neutral = int(total_neutral_words/total_word_count * 100)

    print(f"\nTotal word count: {total_word_count}")
    print(f"Total positive words: {total_pos_words}, which accounts for {percentage_positive}% of all text you read.")
    print(f"Total negative count: {total_neg_words}, which accounts for {percentage_negative}% of all text you read.")
    print(f"Total neutral words: {total_neutral_words}, which accounts for {percentage_neutral}% of all text you read.")

    print("Finished!")

def main():
    p_list, n_list = save_word_lists()
    check_scraped_text(p_list, n_list)

if __name__ == '__main__':
    main()