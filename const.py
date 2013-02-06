# @author Greg Mojonnier

def Checked( oldClass ):		
	""" class decorator used to signal adding const check functionality to it """
	class classWithConstFunct( oldClass ):
		""" Sub class of orignal class adding necessary methods/variable for const functionality """
		__slots__ = ['constEnabled']

		def __init__(self, *args):
			self.constEnabled = False
			return super(classWithConstFunct, self).__init__(*args)

		def __setattr__(self, name, value):
				try:
					# If name exists already check for const being on before setting it
					super().__getattribute__(name)
					if self.constEnabled:
						print("Error: attribute set in Const method of " + str( self.__class__ ) )
					else:
						# Const is off so its okay to set variable
						raise AttributeError
				except AttributeError:
					super().__setattr__(name, value)
	return classWithConstFunct

