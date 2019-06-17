GLBC AutomationTest with Selenium IDE by Daniel Albul.side
- has the following algorithm:
1.  Open Browser
2.  Enter "https://anotepad.com/" in address field and open 
4.  Fill title with text “My First Note”
5.  Click save
6.  Verify that message “You have saved your note as a Guest User. You can come back at anytime to continue editing as long as you don't 	    delete your browser cookies. To access your notes from anywhere and never lose them, please Create a Free Account. Your existing notes 		   will be saved into your account.” Appeared
7.  Delete Note
8.  Verify that “No note here.” Message exist on the page

Test1.py is done later than IDE. But now Anotepad.com has issues with saving notes.
That is why i have changed algorithm to another until the problem is solved:
1.  Open Browser
2.  Enter "https://anotepad.com/create_account/" in address field and open 
3.  Login into the system with:
	"email: kair317@gmail.com"
	"password: 1234567"
5.  Find the note "1233121"
6.  Delete Note