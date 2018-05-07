fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
    print 'A', f
else:
    print 'A fine selection of fruits!'

plants = ['fern', 'pine', 'shooting star', 'lingby sedge', 'mint', 'dowingia']

print 'You have...'
for p in plants:
    if p == 'lingby sedge':
        print 'This is obligate wetland and brackish marsh plant!' # (It actually is.)
    print 'A', p
else:
    print 'A fine selection of plants!!'      