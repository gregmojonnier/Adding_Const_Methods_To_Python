from const import Checked, Const

@Checked
class ConstTest2:
    __slots__ = ( 'x' )
    def __init__( self ):
        self.x = 1
    @Const
    def bump( self ):
        self.x += 1
    def get( self ):
        return self.x
    def __str__( self ):
        return "ConstTest2(" + str(self.x) + ')'

f = ConstTest2()
print( "f.x =", f.get() )
f.bump()
print( "f.x =", f.get() )
f.bump()
print( "f.x =", f.get() )
f.x = 10
print( "f.x =", f.x )
f.__setattr__( "x", 20 )
print( "f.x =", f.x )
