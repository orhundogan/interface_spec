-- Specification -- 

The page will display a user management screen. It will be used to view the current users and add new ones. It will contain 3 main parts and this
specification file will explain them in depth. This page will not be accessible by guests.

-- Top Section --

In the top section, users will be allowed to do 2 actions. They can add/save new users and they can filter out the disabled users. On the left side of the
section, there will be a button with "New User" button. The button will have blue background and white text color. When it is pressed, a form will be 
shown on bottom-right section (which will be explained later). Right next to the button, there will be a checkbox with the label "Hide Disabled Users". 
This checkbox can be used to filter the users table, which will be in the bottom-left section (which will be explained later). Users can use this checkbox
to change the view of the table. If it is pressed, then the users list will hide all the disabled user records. However, if it is not pressed, then the 
table will also contain the information of disabled users. Lastly for the section, there will be another button at the right side of the section. The
button will also be blue with white text color. It will have "Save User" label. After the form (which was shown after clicking Add User button) is filled,
users can press "Save User" button to save their inputs and add the user to the table. 

-- Bottom Left Section --

In this section, there will be a table that displays the information of all users. This table will have 4 columns, which are ID, User Name, Email, Enabled.
ID will store the id of users, User Name will store the names of the users, Email will store the emails of the users and Enabled will store whether that 
account is enabled or disabled. The titles of these columns will have a blue color with white text color. Also, next to these titles, there will be small
buttons which can be used by users. They will allow them to sort and filter results. Below the title, there will be all user records. This table will be
zebra striped, meaning that adjacent rows will have different colors to make reading easier. These colors will be white and light blue. All rows will have
black text color. The table will show every user's records if the checkbox on the top section is not pressed. If it is pressed, then the disabled users
will not be displayed. 

-- Bottom Right Section --

In this section, there will be a form. This form will be used to create new users and will be shown when "New User" button is pressed. On top of the section
there will be a title with black text and light grey background. The title will say "New User". Below that, there will be the form with white background. 
The first 4 parts of the form will ask users for username, display name, phone, and email in this order. The labels will be black and bold. Users will 
be able to input their answers to the text fields next to labels. Below them, there will be a label "User Roles" which will be used to set the roles of the
new users. Next to the label, there will be a drop-down list for users to select the appropriate role for the new user. This can be either admin, guest, or
super admin. Below this, there will be a label "Enabled". Next to this, there will be a checkbox. This will set the new user either enabled or disabled. This
section will not be shown to user in the beginning. It will be visible after the "New User" at the top is clicked.
