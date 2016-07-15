# fraud_detection
algo for bot detection at login:

	1. user at login page
	2. check grey level of ip address.
	3. if grey level greater than threshold
				present captcha
	4. user enters id, pwd.
	5. if failed attempt:
				start building pattern
				change grey level(both ip & user) according to pattern
				after grey level goes beyond threshold present with captcha	
	6. iterate 5 for each failed attempt.
	7. for blacklisted ip & users, or if grey list beyong highest threshold
				send otp or login link via email.
