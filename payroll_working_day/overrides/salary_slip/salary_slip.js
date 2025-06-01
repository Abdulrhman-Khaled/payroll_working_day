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

    onload_post_render: function (frm) {
        if (frm.doc.status == "Submitted" || (frm.doc.status == "Draft" && frm.doc.employee)) {
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
        }
    },

    after_save: function (frm) {
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

    after_submit: function (frm) {
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

