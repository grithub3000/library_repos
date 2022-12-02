'''
Ryan Coutts
Library of Congress
CS 1400
Due October 21, 2022
This program is meant to read, and reorginize a file of scattered lines from 
different books into the correct order and within the correct novel. It also 
prints a brief summary of each novel that includes the longest line, the 
shortest line, and the average line length. Lessons Learned: Using sys.argv,
 how to sort CSV files, improving function structure.
'''
def main():
    import csv, operator
    data = "book_data.txt"
    summary = "novel_summary.txt"
    final = "novel_text.txt"
    
    def print_neat(list, file):
        #Prints a list neatly to a file
        with open(file, "w") as output_file:
            for item in list:
                if item != list[0]:
                    print("-----", file=output_file)
                print(item[0][2], file=output_file)
                for text in item:
                    print(text[0], file=output_file)


    def append_file(file):
        #Places all lines of a file into a list.
        with open (file, "r") as source:
            reader = csv.reader(source, delimiter="|")
            scattered_text = []
            for row in reader:
                scattered_text.append(row)
            return scattered_text

    def sort_codes(list):
        #Sorts the list based off of the 3-letter code
        sorted_list = list
        sorted_list.sort(key=operator.itemgetter(2))
        return sorted_list
    
    def get_number(line):
        return float(line[1])

    def split3(list):
        #Splits the novels into their own seperate lists within the main list
        count = 0
        split_lists = []
        for item in list:
            text = item[0]
            line_num = item[1]
            code = item[2]
            if code != list[count - 1][2]:
                split_lists.append([])
                split_lists[-1].append(item)
            else:
                split_lists[-1].append(item)
            count += 1
        return split_lists
    
    def sort_line_num(list):
        #Sorts each individual novel based on the line number
        for i in range(len(list)):
            list[i].sort(key=get_number)
        return list

    def find_all_stats(list, file):
            #Finds the stats and prints them to the specified file
            find_longest(list, file)
            find_shortest(list, file)
            find_average(list, file)
            
    def find_longest(list, file):
        with open(file, "a") as output:
            longest = ""
            for line in list:
                if len(line[0]) >= len(longest):
                    longest = line[0]
                    place = line[1]
            print(list[0][2], file=output)
            print(f'Longest line ({place}): {longest}', file=output)

    def find_shortest(list,file):
        with open(file, "a") as output:
            shortest = "." * 9999999
            for line in list:
                if len(line[0]) < len(shortest):
                    shortest = line[0]
                    place = line[1]
            print(f'Shortest line ({place}): {shortest}', file=output)

    def find_average(list, file):
        with open(file, "a") as output:
            char = 0 
            count = 0
            for line in list:
                char += len(line[0])
                count += 1
            avg = char / count
            print(f"Average length: {round(avg)}\n", file=output)
            
            
    fully_sorted = sort_line_num(split3(sort_codes(append_file(data))))
    
    print_neat(fully_sorted, final)

    
    for i in range(len(fully_sorted)):
        find_all_stats(fully_sorted[i], summary)

if __name__ == "__main__":
   main()
