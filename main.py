###solution to problem 48 from ben stephenson's "the python workbook".

print("Enter a year:")
year = int(input())

zodiac = ['Monkey','Rooster','Dog','Pig','Rat','Ox','Tiger','Hare','Dragon','Snake','Horse','Sheep']

print(f'It is the year of the {zodiac[year % 12]}.')
