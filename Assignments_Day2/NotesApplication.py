class NotesApplication(object):
	def __init__ (self,author):
		self.author = author
		self.notes_list = []

	def create (self,note_content):
		return self.notes_list.append(note_content)

	def list(self):
		note_id=0
		for x in self.notes_list:
			print "Note ID:" + note_id
			print notes_list[note_content]
			print "By Author" + author

	def get(self,note_id):
		return self.notes_list[note_id]

	def search(self, search_text):
		i=0
		print "Showing results for", search_text
		
		for i in self.notes_list:
			if (x.find(search_text)>1):
				print "Note ID:", i
				print x
				print "By Author", self.author

				i = i+1

			else:
				i=i+1


	def edit(self, note_id, new_content):
		if self.note_id >= len(notes_list) and note_id < 0:
			print "Enter valid id"
		else:
			self.notes_list[note_id] = new_content
