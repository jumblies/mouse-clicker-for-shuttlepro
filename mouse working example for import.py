from ctypes import windll, Structure, c_ulong, byref
import ctypes
from time import sleep



class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]



def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    #return { "x": pt.x, "y": pt.y} #returning dictionary not helpful for me
    return [pt.x, pt.y]



def leftClick():
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

pos = queryMousePosition()
print(pos)

# see http://msdn.microsoft.com/en-us/library/ms646260(VS.85).aspx for details
ctypes.windll.user32.SetCursorPos(656, 92)
sleep(.1)
leftClick()
sleep(.05)
x, y = pos[0], pos[1]
ctypes.windll.user32.SetCursorPos(x, y)

