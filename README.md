# django-crm

Data Hub Task

Hi,
This is a rough idea about how I created a simple CRM application requested by your company. While it does not have the templates to display the website, I do however implemented a functional REST API within a Django Framework. Hence, with the URLs implemented we could access CRUD operations for both Employee and User.

P.S. I had some difficulty in auto-generating emp-no initially as I've tried UUID but it had certain issues with the database so I had to remove it as a whole.

URLS (if using localhost):
"/users" -> User create
"/users/<id no>" -> User Update/Delete/Read
"/employees" -> Employee create
"/employees/<id no>" -> employees Update/Delete/Read
