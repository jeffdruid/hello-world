# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida':'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY']= 'New York'
cities['OR']= 'Portland'

#print out some cities
print("-"*10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

# print out some states
print("-"*10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print("-"*10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print("-"*10)
for state, abbrev in states.items():
    print("%s is abbreviated %s " %(state, abbrev))

# print every ciy in state
print("-"*10)
for abbrev, city in cities.items():
    print("%s has the city %s " % (abbrev, city))

# now do both at the same timne
print("-"*10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s " % (state, abbrev, cities[abbrev]))

print("-"*10)

#safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print("sorry, no Texas")

#get a city whith a default value
city = cities.get('Texas', 'Does not exist')
print("The city for the state 'TX' is: %s" % city)
