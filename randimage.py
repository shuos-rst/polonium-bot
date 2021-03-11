#.woop command. goal of this is to send a random image of wooper

import csv


class randimage():

    images = set()

    def __init__(self, file): #constructor                
        self.images = set()
        with open(file, newline='') as file_input: #this bit of code should read in lines from the csv of images
            file_reader = csv.reader(file_input)
            for row in file_reader:
                self.images.add(str(row)) #we store the images in a set because .pop() from a set is random access


    def rand(self):
        result = self.images.pop()
        result = result.replace("'","")
        result = result.strip("[]")
        self.images.add(result)
        return(result)
