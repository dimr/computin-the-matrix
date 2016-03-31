voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    data={}
    for i,line in enumerate(voting_data):
        name = line.split(" ")[0]
        numbers = line.split(" ")[3:]
        temp=[]
        data[name]=temp
        for num in numbers:
            data[name].append(int(num))
    return data
    

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    senA = voting_dict[sen_a]
    seB = voting_dict[sen_b]
    return sum(i*j for i,j in zip(senA,seB))


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    data={}
    for senator in voting_dict.keys():
        if senator!=sen:
           data[senator]=policy_compare(senator,sen,voting_dict)
    return max(data,key=data.get) 
    

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    data={}
    for senator in voting_dict.keys():
        if senator!=sen:
           data[senator]=policy_compare(senator,sen,voting_dict)
    return min(data,key=data.get) 
    
    

## Task 5

most_like_chafee    = most_similar('Chafee',create_voting_dict())
least_like_santorum = least_similar('Santorum',create_voting_dict()) 



# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    temp = []
    for senator in sen_set:
        temp.append(policy_compare(sen,senator,voting_dict))
    return sum(temp)/len(temp)

most_average_Democrat = ... # give the last name (or code that computes the last name)


# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    data=[]
    for senator in sen_set:
        temp = [] 
        for l in voting_dict[senator]:
            temp.append(l)
        data.append(temp)
    data2=[ sum(i) for i in zip(*data)]
    return [x/len(sen_set) for x in data2 ]
democrats={'Kennedy', 'Byrd', 'Clinton', 'Baucus', 'Reid', 'Bingaman', 'Salazar', 'Levin', 'Landrieu', 'Conrad', 'Biden', 'Feinstein', 'Bayh', 'Durbin', 'Nelson1', 'Nelson2', 'Obama', 'Feingold', 'Inouye', 'Dodd', 'Mikulski', 'Dayton', 'Kerry', 'Schumer', 'Cantwell', 'Lautenberg', 'Akaka', 'Pryor', 'Murray', 'Rockefeller', 'Harkin', 'Dorgan', 'Lincoln', 'Johnson', 'Reed', 'Wyden', 'Sarbanes', 'Kohl', 'Lieberman', 'Leahy', 'Boxer', 'Stabenow', 'Carper'}

average_Democrat_record = find_average_record(democrats, create_voting_dict()) # (give the vector)


# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    d = list(voting_dict)
    data=[]
    for i,name in enumerate(d):
        for j in range(i+1,len(d)-1):
            data.append( (name,d[j],policy_compare(d[i],d[j],voting_dict)))
    numbers=[]
    for n in data:
        numbers.append(n[2])
    m=min(numbers)
    result=[]
    for record in data:
        if record[2]==m:
            result.append(record[0])
            result.append(record[1])
            break
    return (tuple(result))

