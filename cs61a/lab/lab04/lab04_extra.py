from lab04 import *

# Q7
def reverse_iter(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    reversed_lst = []
    for i in range(len(lst)):
        reversed_lst += [lst[len(lst) - 1 - i]]  

    return reversed_lst

# Q8
def list_to_link(lst):
    """Converts a list to a linked list.

    >>> lst = [1, 2, 3, 4]
    >>> r = list_to_link(lst)
    >>> first(r)
    1
    >>> first(rest(rest(r)))
    3
    >>> r = list_to_link([])
    >>> r is empty
    True
    """
    if len(lst) == 1:
        return link(lst[0])
    elif lst == []:
        return empty
    else:
        return [lst[0]] + [ list_to_link(lst[1:]) ]

# Q9
def has_prefix(s, prefix):
    """Returns whether prefix appears at the beginning of linked list s.

    >>> x = link(3, link(4, link(6, link(6))))
    >>> print_link(x)
    3 4 6 6
    >>> has_prefix(x, empty)
    True
    >>> has_prefix(x, link(3))
    True
    >>> has_prefix(x, link(4))
    False
    >>> has_prefix(x, link(3, link(4)))
    True
    >>> has_prefix(x, link(3, link(3)))
    False
    >>> has_prefix(x, x)
    True
    >>> has_prefix(link(2), link(2, link(3)))
    False
    """
    if prefix == empty:
        return True

    FOUND = False

    list_s = link_to_list(s)
    list_prefix = link_to_list(prefix)

    if len(list_s) < len(list_prefix):
        return False

    for i in range(len(list_prefix)):
        if list_prefix[i] == list_s[i]:
            FOUND = True
        else:
            FOUND = False
            break


    return FOUND

def has_sublist(s, sublist):
    """Returns whether sublist appears somewhere within linked list s.

    >>> has_sublist(empty, empty)
    True
    >>> aca = link('A', link('C', link('A')))
    >>> x = link('G', link('A', link('T', link('T', aca))))
    >>> print_link(x)
    G A T T A C A
    >>> has_sublist(x, empty)
    True
    >>> has_sublist(x, link(2, link(3)))
    False
    >>> has_sublist(x, link('G', link('T')))
    False
    >>> has_sublist(x, link('A', link('T', link('T'))))
    True
    >>> has_sublist(link(1, link(2, link(3))), link(2))
    True
    >>> has_sublist(x, link('A', x))
    False
    """

    if sublist == empty:
        return True
    if has_prefix(s,sublist):
        return True
    elif s != empty:
        return has_sublist(rest(s), sublist)
    else:
        return False



def has_61A_gene(dna):
    """Returns whether linked list dna contains the CATCAT gene.

    >>> dna = link('C', link('A', link('T')))
    >>> dna = link('C', link('A', link('T', link('G', dna))))
    >>> print_link(dna)
    C A T G C A T
    >>> has_61A_gene(dna)
    False
    >>> end = link('T', link('C', link('A', link('T', link('G')))))
    >>> dna = link('G', link('T', link('A', link('C', link('A', end)))))
    >>> print_link(dna)
    G T A C A T C A T G
    >>> has_61A_gene(dna)
    True
    >>> has_61A_gene(end)
    False
    """
    sublist = empty
    for n in 'CATCAT':
        sublist = insert_at_end(sublist, n)
    return has_sublist(dna, sublist)


# Q10

def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    res = []
    def flatten_helper(lst):
        nonlocal res
        for n in lst:
            if type(n) != list: # [1,2,[1,2]]
               res.append(n) 
            else:
                flatten_helper(n)

        return res

    return flatten_helper(lst)
# Q11
def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    alist = []
    i = 0
    j = 0
    if lst1 ==[] or lst2 == []:
        return lst1 + lst2

    while i <= len(lst1) and j <= len(lst2):
        if i == len(lst1):
            alist += [lst2[j]]
            break
        elif j == len(lst2):
            alist += [lst1[i]]
            break

        if lst1[i] < lst2[j]:
            alist += [lst1[i]]
            if i + 1 <= len(lst1):
                i += 1
        else:
            alist += [lst2[j]]
            if j + 1 <= len(lst2):
                j += 1
        

    return alist
# Q12

def interleave(s0, s1):
    """Interleave linked lists s0 and s1 to produce a new linked
    list.

    >>> evens = link(2, link(4, link(6, link(8, empty))))
    >>> odds = link(1, link(3, empty))
    >>> print_link(interleave(odds, evens))
    1 2 3 4 6 8
    >>> print_link(interleave(evens, odds))
    2 1 4 3 6 8
    >>> print_link(interleave(odds, odds))
    1 1 3 3
    """
    k = 0 # As a switch to decide which list to index
    def interleave_helper(s0,s1):
        nonlocal k
        if k == 0:
            if rest(s0) == 'empty':
                k = 1
                return link(s0[0], s1)
            else:
                k = 1
                return link(s0[0], interleave_helper(rest(s0), s1))
        elif k == 1:
            if rest(s1) == 'empty':
                k = 0
                return link(s1[0], s0)
            else:
                k = 0
                return link(s1[0], interleave_helper(s0, rest(s1)))

    return interleave_helper(s0,s1)

