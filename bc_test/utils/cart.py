import frappe
import frappe.defaults
from frappe import _, throw
from frappe.contacts.doctype.address.address import get_address_display
from frappe.contacts.doctype.contact.contact import get_contact_name
from frappe.utils import cint, cstr, flt, get_fullname
from frappe.utils.nestedset import get_root_of

from erpnext.accounts.utils import get_account_name
from webshop.webshop.doctype.webshop_settings.webshop_settings import (
	get_shopping_cart_settings,
)
from webshop.webshop.utils.product import get_web_item_qty_in_stock
from erpnext.selling.doctype.quotation.quotation import _make_sales_order
from webshop.webshop.shopping_cart.cart import _get_cart_quotation


@frappe.whitelist()
def place_order():
	quotation = _get_cart_quotation()
	cart_settings = frappe.get_cached_doc("Webshop Settings")
	quotation.company = cart_settings.company

	quotation.flags.ignore_permissions = True
	quotation.submit()

	if quotation.quotation_to == "Lead" and quotation.party_name:
		# company used to create customer accounts
		frappe.defaults.set_user_default("company", quotation.company)

	if not (quotation.shipping_address_name or quotation.customer_address):
		frappe.throw(_("Set Shipping Address or Billing Address"))

	sales_order = frappe.get_doc(
		_make_sales_order(
			quotation.name, ignore_permissions=True
		)
	)
	sales_order.payment_schedule = []

	if not cint(cart_settings.allow_items_not_in_stock):
		for item in sales_order.get("items"):
			item.warehouse = frappe.db.get_value(
				"Website Item", {"item_code": item.item_code}, "website_warehouse"
			)
			is_stock_item = frappe.db.get_value("Item", item.item_code, "is_stock_item")

			if is_stock_item:
				item_stock = get_web_item_qty_in_stock(
					item.item_code, "website_warehouse"
				)
				if not cint(item_stock.in_stock):
					throw(_("{0} Not in Stock").format(item.item_code))
				if item.qty > item_stock.stock_qty:
					throw(
						_("Only {0} in Stock for item {1}").format(
							item_stock.stock_qty, item.item_code
						)
					)
	coupon_code=False
	if sales_order.coupon_code and sales_order.grand_total == 0:
		coupon_code=True

	sales_order.flags.ignore_permissions = True
	sales_order.insert()
	sales_order.submit()
	if coupon_code:
		original_user = frappe.db.get_value("Sales Order", sales_order.name, "owner")
		frappe.enqueue(
				create_enrollement_for_all_cource, sales_order=sales_order, queue="short", original_user= original_user
			)

	if hasattr(frappe.local, "cookie_manager"):
		frappe.local.cookie_manager.delete_cookie("cart_count")
	if coupon_code:
		return {"sales_order":sales_order.name, "coupon_code" : True}
	else:
		return {"sales_order":sales_order.name, "coupon_code" : False}


@frappe.whitelist(allow_guest=True)
def create_enrollement_for_all_cource(sales_order, original_user):
	# Save original user
	
	try:
		# Temporarily switch to Administrator to ignore permission checks
		frappe.set_user("Administrator")
		
		# Fetch the Sales Order doc
		sales_order = frappe.get_doc("Sales Order", sales_order)

		# Get all LMS Courses
		course_list = frappe.db.get_list("LMS Course",{"published":1}, pluck="name")

		for course in course_list:
			# Check if Enrollment exists
			if not frappe.db.exists("LMS Enrollment", {"member": original_user, "course": course}):
				new_enroll = frappe.new_doc("LMS Enrollment")
				new_enroll.member = original_user
				new_enroll.course = course
				new_enroll.insert(ignore_permissions=True)
		user_doc = frappe.get_doc("User", original_user)
		user_doc.add_roles("LMS Student")
		

		# Send email
		full_name = frappe.db.get_value("User", original_user, "full_name") or "Learner"
		subject = "Your Course is Ready – Access Your Learning Now!"
		message = f"""
			<p>Hi {full_name},</p>
			<p>Thank you for your purchase!</p>
			<p>We’re excited to let you know that your courses are now available. You can start learning right away by clicking the link below:</p>
			<p>👉 <a href='https://businesscatalysts.frappe.cloud/lms/courses'>Click Here to Access Your Course</a></p>
			<p>If you have any questions or need help accessing the course, feel free to reply to this email. We're always happy to help.</p>
			<p>Happy learning!</p>
		"""
		frappe.sendmail(recipients=[original_user], content=message, subject=subject)

	finally:
		# Always reset user context back
		frappe.set_user(original_user)

		