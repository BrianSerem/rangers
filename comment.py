
class Comment:

comment_id = 1

	def __init__(self, body, user_id):

		self.com_id = comment_id
		self.user_id = user_id
		self.body = body

		comment_id += 1

	def serialize(self):
		return dict(
			com_id = self.com_id,
			body = self.body,

			user = self.user_id

			)

	def create_comment():
		

	def edit(self, com_id):
		new_comment = input("enter new comment!")
		comment = get_by_id(com_id)
		if comment:
			comment.string = new_comment
		else:
			print("comment not found")


	def delete(self, com_id):


	def get_by_id(self, com_id):
		for comment in comments:
			if comment.id == com_id:
				return comment