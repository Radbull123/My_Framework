"""
    You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.

    Implement a function likes :: [String] -> String, which must take in input array,
containing the names of people who like an item.
It must return the display text as shown in the examples.
"""


def likes(names):
    a = 'no one likes this'
    if len(names) == 1:
        a = ', '.join(names) + ' likes this'
    elif len(names) == 2:
        a = " ".join(names[:1]) + ' and {} like this'.format(names[1])
    elif len(names) == 3:
        a = ', '.join(names[:2]) + ' and {} like this'.format(names[2])
    elif len(names) > 3:
        a = ', '.join(names[:2]) + ' and {} others like this'.format(len(names)-2)
    return a
#your code here

