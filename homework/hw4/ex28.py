**********************
Windows PowerShell transcript start
Start time: 20170921152631
Username: DESKTOP-B8D4HP7\Connie
RunAs User: DESKTOP-B8D4HP7\Connie
Machine: DESKTOP-B8D4HP7 (Microsoft Windows NT 10.0.15063.0)
Host Application: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
Process ID: 10640
PSVersion: 5.1.15063.608
PSEdition: Desktop
PSCompatibleVersions: 1.0, 2.0, 3.0, 4.0, 5.0, 5.1.15063.608
BuildVersion: 10.0.15063.608
CLRVersion: 4.0.30319.42000
WSManStackVersion: 3.0
PSRemotingProtocolVersion: 2.3
SerializationVersion: 1.1.0.1
**********************
Transcript started, output file is C:\Users\Connie\Desktop\PythonClass\assignments\homework\hw4\ex28.py
PS C:\Users\Connie\Desktop\PythonClass\assignments\homework\hw4> python
Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> # 1. True and True => True
... True and True
True
>>> # 2. False and True => False
... False and True
False
>>> # 3. 1 == 1 and 2 == 1 => False
... 1 == 1 and 2 == 1
False
>>> # 4. "test" == "test" => True
... "test" == "test"
True
>>> # 5. 1 == 1 or 2 != 1 => True and True => True
... 1 == 1 or 2 != 1
True
>>> #6. True and 1 == 1
... #=> True
... True and 1 == 1
True
>>> # 7. False and 0 != 0 => False and False => False
... False and 0 != 0
False
>>> # 8. True or 1 == 1 => True and True => True
... True or 1 == 1
True
>>> # 9. "test" == "testing" => False
... "test" == "testing"
False
>>> # 10. 1 != 0 and 2 == 1 => False and True => False
... 1 != 0 and 2 == 1
False
>>> # 11. "test" != "testing"
... #=> True
... "test" != "testing"
True
>>> # 12. "test" == 1 => False, String != Num
... "test" == 1
False
>>> # 13. not (True and False) => not(True and False => True) => not(True)=> False
... not (True and False)
True
>>> # 14. not (1 == 1 and 0 != 1) => not (True and True) => not (True) => False
... not (1 == 1 and 0 != 1)
False
>>> # 15. not (10 == 1 or 1000 == 1000) => not (False or True) => not (True) => False
... not (10 == 1 or 1000 == 1000
... )
False
>>> # 16. not (1 != 10 or 3 == 4) => not (True or False) => not (True) => False
... not (1 != 10 or 3 == 4)
False
>>> # 17. not ("testing" == "testing" and "Zed" == "Cool Guy")=> not(True and False) => not (False) => True
... not ("testing" == "testing" and "Zed" == "Cool Guy")
True
>>> # 18. 1 == 1 and (not ("testing" == 1 or 1 == 0)) => True and (not (False or False))=> True and not(False)=> True and True => True
... 1 == 1 and (not ("testing" == 1 or 1 == 0))
True
>>> # 19. "chunky" == "bacon" and (not (3 == 4 or 3 == 3)) => False and (not (False or True)) => False and not(True) => False and False => False
... "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
False
>>> # 20. 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")) => True and (not (True or False)) => True and not (True) => False
... 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
False
>>> quit()
PS C:\Users\Connie\Desktop\PythonClass\assignments\homework\hw4> Stop-Transcript
**********************
Windows PowerShell transcript end
End time: 20170921154448
**********************
