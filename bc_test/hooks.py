app_name = "bc_test"
app_title = "BC Test"
app_publisher = "Foss"
app_description = "Test"
app_email = "foss@erp.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bc_test/css/bc_test.css"
# app_include_js = "/assets/bc_test/js/bc_test.js"

# include js, css files in header of web template
# web_include_css = "/assets/bc_test/css/bc_test.css"
web_include_js = "bc.bundle.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "bc_test/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "bc_test.utils.jinja_methods",
# 	"filters": "bc_test.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "bc_test.install.before_install"
# after_install = "bc_test.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "bc_test.uninstall.before_uninstall"
# after_uninstall = "bc_test.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "bc_test.utils.before_app_install"
# after_app_install = "bc_test.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "bc_test.utils.before_app_uninstall"
# after_app_uninstall = "bc_test.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bc_test.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"User": {
		"after_insert": "bc_test.bc_test.user.after_insert",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"bc_test.tasks.all"
# 	],
# 	"daily": [
# 		"bc_test.tasks.daily"
# 	],
# 	"hourly": [
# 		"bc_test.tasks.hourly"
# 	],
# 	"weekly": [
# 		"bc_test.tasks.weekly"
# 	],
# 	"monthly": [
# 		"bc_test.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "bc_test.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
	"webshop.webshop.api.get_product_filter_data": "bc_test.bc_test.api.get_product_filter_data",
	"lms.lms.user.sign_up" : "bc_test.bc_test.user.sign_up"
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "bc_test.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["bc_test.utils.before_request"]
# after_request = ["bc_test.utils.after_request"]

# Job Events
# ----------
# before_job = ["bc_test.utils.before_job"]
# after_job = ["bc_test.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"bc_test.auth.validate"
# ]
