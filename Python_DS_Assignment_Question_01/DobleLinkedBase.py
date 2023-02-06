class _DoubleLinkedBase:
	""" A base class providing a doubly linked list representation."""

	class _Node:
		""" Lightweight, nonpublic class for storing a doubly linked node"""
		__slots__ = '_element', '_prev', '_next' # streamline memory

		def __init__(self, element, prev, next): # initialize node's fields
			self._element = element
			self._prev = prev
			self._next = next

	def __init__(self):
		"""Create an empty list"""
		self._header = self._Node(None, None, None)
		self._trailer = self._Node(None, None, None)
		self._header._next = self._trailer
		self._trailer._prev = self._header
		self._size = 0 # number of elements

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def _insert_between(self, e, predecessor, successor):
		"""Add element e between two existing nodes and return new node"""
		newest = self._Node(e, predecessor, successor)
		predecessor._next = newest
		successor._prev = newest
		self._size += 1
		return newest

	def _delete_node(self, node):
		"""Delete nonsentinel node from the list and return its elements"""
		if node._prev is not None and node._next is not None:
			node._prev._next = node._next
			node._next._prev = node._prev
			self._size -= 1
			element = node._element
			node._prev = node._next = node._element = None
			return element


def main(): #for checking the functions of class
    # create an empty list
    dlb = _DoubleLinkedBase()
    print(dlb.is_empty()) # should print "List is empty: True"
    
    n1=dlb._insert_between(5,dlb._header,dlb._trailer)
    print(len(dlb))
    n2=dlb._insert_between(1,dlb._header,dlb._trailer)
    n3=dlb._insert_between(7,n1,n2)
    n4=dlb._insert_between(2,n1,n3)
    print(len(dlb))
    ele2=dlb._delete_node(n2)
    print(ele2)
    print(len(dlb))

    
if __name__ == '__main__':
    main()    
