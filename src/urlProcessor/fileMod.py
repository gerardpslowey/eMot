import csv

file = 'text.txt'

class FileMod:
    def erase_file(self):
        # erase the file contents if already written to
        open(file, 'w').close()

    def write_file(self, chunks):
        with open(file, "a+", encoding="utf-8") as f:
            for chunk in chunks:
                if(len(chunk)!=0):
                    f.write(str(chunk) + " ")

    def write_to_csv(self, chunks):
        text = []
        
        with open('scraped.csv', mode='a', encoding="utf-8") as scraped_text:
            writer = csv.writer(scraped_text, delimiter=',')

            for chunk in chunks:
                if(len(chunk)!=0):
                    text.append(chunk)
                    
            if len(text) != 0:
                writer.writerow(text)
            
    def read_file(self):
        return file

