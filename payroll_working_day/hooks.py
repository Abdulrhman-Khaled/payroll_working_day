app_name = "payroll_working_day"
app_title = "Payroll Working Day"
app_publisher = "bodykh"
app_description = "Ser days per month fixed"
app_email = "bodykh@itqan-kw.net"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/payroll_working_day/css/payroll_working_day.css"
# app_include_js = "/assets/payroll_working_day/js/payroll_working_day.js"

# include js, css files in header of web template
# web_include_css = "/assets/payroll_working_day/css/payroll_working_day.css"
# web_include_js = "/assets/payroll_working_day/js/payroll_working_day.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "payroll_working_day/public/scss/website"

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
# 	"methods": "payroll_working_day.utils.jinja_methods",
# 	"filters": "payroll_working_day.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "payroll_working_day.install.before_install"
# after_install = "payroll_working_day.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "payroll_working_day.uninstall.before_uninstall"
# after_uninstall = "payroll_working_day.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "payroll_working_day.utils.before_app_install"
# after_app_install = "payroll_working_day.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "payroll_working_day.utils.before_app_uninstall"
# after_app_uninstall = "payroll_working_day.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "payroll_working_day.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"payroll_working_day.tasks.all"
# 	],
# 	"daily": [
# 		"payroll_working_day.tasks.daily"
# 	],
# 	"hourly": [
# 		"payroll_working_day.tasks.hourly"
# 	],
# 	"weekly": [
# 		"payroll_working_day.tasks.weekly"
# 	],
# 	"monthly": [
# 		"payroll_working_day.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "payroll_working_day.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "payroll_working_day.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "payroll_working_day.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["payroll_working_day.utils.before_request"]
# after_request = ["payroll_working_day.utils.after_request"]

# Job Events
# ----------
# before_job = ["payroll_working_day.utils.before_job"]
# after_job = ["payroll_working_day.utils.after_job"]

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
# 	"payroll_working_day.auth.validate"
# ]
