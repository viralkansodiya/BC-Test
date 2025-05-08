# Copyright (c) 2025, Viral Patel and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class SignupForm(Document):
	def validate(self):
		if frappe.db.exists("User", self.email):
			frappe.throw("Email already exists")
		if self.is_new():
			doc_user = frappe.new_doc("User")
			doc_user.email = self.email
			doc_user.first_name = self.first_name
			doc_user.last_name = self.last_name
			doc_user.send_welcome_email = 1
			doc_user.flags.ignore_permissions = True
			doc_user.append("roles",{
				"role" : "Webuser",
			})
			doc_user.insert()