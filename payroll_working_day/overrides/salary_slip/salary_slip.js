frappe.ui.form.on('Salary Slip', {
    employee: function (frm) {

        frappe.call({
            method: "payroll_working_day.overrides.salary_slip.salary_slip.fetch_custom_payroll_working_days",
            args: {
                employee: frm.doc.employee,
            },
            callback: function (response) {
                if (response.message) {
                    const customWorkingDays = response.message;
                    console.log("Custom Payroll Working Days:", customWorkingDays);
                    frm.doc.total_working_days = customWorkingDays;
                    frm.doc.absent_days = customWorkingDays - frm.doc.payment_days;
                    frm.refresh_field("total_working_days");
                    frm.refresh_field("absent_days");
                    frm.save();
                } else {
                    frappe.show_alert({
                        message: __("No working days found."),
                        indicator: "red"
                    });
                }
            },
            error: function (err) {
                console.error("Error fetching working days:", err);
            }
        });
    },
});

function fetch_last_salary_structure(employee, callback) {
    frappe.call({
        method: "salary_site_calc.overrides.salary_slip.salary_slip.get_last_salary_structure",
        args: {
            employee: employee
        },
        callback: function (response) {
            if (response.message) {
                callback(response.message.custom_site_percentage);
            } else {
                console.error("No salary structure found.");
            }
        },
        error: function (err) {
            console.error("Error fetching salary structure:", err);
        }
    });
}

