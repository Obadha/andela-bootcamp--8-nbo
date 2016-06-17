import unittest
from notes_application import NotesApplication
# from the notes_application import the class NotesApplication


class NotesApplicationTest (unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls._note = NotesApplication("Loso")
		# create an instance of the class NotesApplication to access its methods


	# test to check if the content_list is not an empty string
	def test_note_content_not_empty (self):
		self.assertEqual (self._note.create(""),[""])
		

	


'''List of all tests, well at least those that I can think of anyway
1. takes in note content as parameter. Check if empty is being passed
   takes in note content, check it is string
2. get function - check if note_id is provided
3. get function - check if note_id is a valid integer
3. get function - check if note_id actually exists
4. search function - check if search_text is provided
5. search function - check if search_text is a string
6. search function - check we have a non-empty string that we will be looking at to find the text
7. search function - check author is non-empty
8. edit function - check note_id exists i.e is provided
9. edit function - check note_id is valid i.e not more than what is expected
10. edit function - check new_content exists
'''




if __name__ == '__main__':
	unittest.main()