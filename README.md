# conditionals-project-More and more, people are getting more aware about cybersecurity risks in their own devices. A common way I see people protecting their devices is by installing a file integrity monitor to keep sensitive files safe, but why buy one when you can easily create one in less than 10 minutes.

It is also a great project for aspiring penetration testers to learn about programming and hashes.

So how does it work?
Every file in every state has its own unique hash, when the file gets tampered with, the hash changes. So if we can take the hash of a sensitive file, we can compare it to a baseline, and if it changes, we would know that the contents in the file changed too.

Why is it important?
Tampering with files is one of the best techniques to escalate privileges(cron jobs/schedule tasks) in a system, and many more security risks. A file integrity monitor can help stop this.

Even though in most scenarios, setting proper file permissions, schedule logouts, and a good password policy, would solve this problem, a File integrity monitor cannot hurt and is a good backup/last line of defense.
