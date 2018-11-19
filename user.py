class Moderator(User):
	def __init__(self):
		pass

	def can_delete(self):
		return True


	def can_edit_own(self):
		return True