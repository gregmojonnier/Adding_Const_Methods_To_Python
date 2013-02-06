# @author Greg Mojonnier

def Checked( oldClass ):		
	""" class decorator used to signal adding const check functionality to it """
	class classWithConstFunct( oldClass ):
		""" Sub class of orignal class adding necessary methods/variable for const functionality """
		__slots__ = ['constEnabled']

		def __init__(self, *args):
			checkedParent = super(classWithConstFunct, self).__init__(*args)
			super().__setattr__('constEnabled', False)
			return checkedParent

		def __setattr__(self, name, value):
				try:
					# If passd in argument name doesn't exist AttributeError is thrown
					super().__getattribute__(name)
					constEnabled = super().__getattribute__('constEnabled')
					
					# Make sure we don't block constEnabled from unsetting itself when true
					if constEnabled and ( str(name) != 'constEnabled'):
						raise ConstViolated
					else:
						# Const is off so its okay to set variable
						raise AttributeError
				except AttributeError:
					super().__setattr__(name, value)
	return classWithConstFunct

def Const( oldFunc ):
	""" function decorator used on classes marked with Checked decorator to signify const method """
	def enableConst( *args ):
		args[0].__setattr__('constEnabled', True)
		oldFuncResult = None
		try:
			oldFuncResult = oldFunc( *args )
		except ConstViolated:
			print("Error: attribute set in Const method of " + str( args[0]) )
		args[0].__setattr__('constEnabled', False)
		return oldFuncResult
	return enableConst

class ConstViolated( Exception ):
	pass
