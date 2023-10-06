Local $hWnd = WinGetHandle("[CLASS:Qt5158QWindowOwnDCIcon]") ; Replace with the actual window class

If @error Then
    MsgBox(16, "Error", "Window not found")
    Exit
EndIf

While True
    ControlSend($hWnd, "1", "2", "3") ; Replace "3" with the key you want to send
    Local $randomSleep = Random(60 * 1000, 60 * 1000) ; Generate a random sleep interval between 1 and 5 minutes in milliseconds
    Sleep($randomSleep)
WEnd
