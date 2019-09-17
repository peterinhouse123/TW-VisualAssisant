from pynotifier import Notification


Notification(
	title='Notification Title',
	description='Notification Description',
	icon_path='python.ico',
	duration=5,                              # Duration in seconds
	urgency=Notification.URGENCY_CRITICAL
).send()