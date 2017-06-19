# user-signup

Your assignment is simply to create a user signup form where users provide a username, password, and, optionally, an email address. You must have an additional field to verify the password (the user must retype it exactly). Then you will validate the input and either redirect them to a welcome page, or provide error information if any input is invalid.

If the user's form submission is not valid, you should reject it and re-render the form with some feedback to inform the user of what they did wrong. The following things should trigger an error:

* The user leaves any of the following fields empty: username, password, verify password.

* The user's username or password is not valid -- for example, it contains a space character or it consists of less than 3 characters or more than 20 characters (e.g., a username or password of "me" would be invalid).

* The user's password and password-confirmation do not match.

* The user provides an email, but it's not a valid email. Note: the email field may be left empty, but if there is content in it, then it must be validated. The criteria for a valid email address in this assignment are that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.
