#1 typing pwd will tell you what directory you are in
#2 typing ls will tell you what directory you are in
#3 after changing your directory to where your git repository is, using git status can ensure you are in a git repository, then you can use git pull to pull the current changes to that repository and merge it
#4 you can copy/move the python file into your directory using cp or mv, then by using git add homework.py, then git commit -m "adding homework" 
#5 using cat homework.py can let you see the contents in the file 
#6 using nano.py can let you edit the contents of the file
#7 using git add homework.py, git commit -m "a message", and git push will allow you to upload to your remote repository 
#8 the error was because 'judy' tried to push local changes to the remote repository wihtout pulling the changes first. first you can use git fetch to get latest changes, git pull oirgin main to merge those changes, then git commit -m "message", then git push origin main to push those specific changes
#9 you can use open ~/Library/Recent\ Items

 
#2.1
def checkDataType(value):
    return (value)


print(type(checkDataType(853)))
print(type(checkDataType('word')))
print(type(checkDataType(6.8)))

#2.2
def evenOrOdd(n):
    if n%2==0:
        return 'even'
    else:
        return 'odd'

print(evenOrOdd(53))
print(evenOrOdd(44))


#3
def sumWithLoop(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

numbers = [1, 2, 3, 4, 5]
print(sumWithLoop(numbers))  


#4.1
def duplicateList(x):
    result = []
    for item in x:
        result.append(item)
        result.append(item)
    return result

print(duplicateList(['a', 'b', 'c']))  


#4.2
def square(num): #needed to add colon
    return num*num
print(square(9))
print(square(14))



