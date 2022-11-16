frappe.pages['salary-calculator'].on_page_load = function(wrapper) {
	frappe.ui.make_app_page({
		parent: wrapper,
		title: __('Salary Calculator'),
		single_column: true
	});

	let salary_calculator = new SalaryCalculator(wrapper);
	$(wrapper).bind('show', ()=> {
		salary_calculator.show();
	});
};

class SalaryCalculator {
	constructor(wrapper) {
		this.wrapper = $(wrapper);
		this.page = wrapper.page;
		this.sidebar = this.wrapper.find(".layout-side-section");
		this.main_section = this.wrapper.find(".layout-main-section");
		this.start = 0;
	}

	show() {
		let me = this;
		let field = me.page.add_field({
			label: __("gross salary"),
			fieldname: "gross_salary",
			fieldtype: "Data",
			placeholder: __("gross salary"),
			width: "800px",
			reqd: 1,
			change: () => {
				me.amount = "";
				if (me.amount != field.get_value() && field.get_value()) {
					me.start = 0;
					me.amount = field.get_value();
					me.make_display();
				}
			}
		});
		field.refresh();
		
	}

	make_display() {
		this.add_records();
		this.main_section.append(frappe.render_template("salary_calculator"));
	}

	add_records() {
		let me = this;

		if (me.amount) {
			me.show_deductions_category()

			let format_money = function(number) {
				return number.toLocaleString('en-US', {
					style: 'currency', 
					currency: 'TZS' 
				});
			  };
			
			me.page.main.find(".gross_amount").html(`<br><h4 style="backgroud-color: teal-200;"><i><em>gross amount: ${format_money(Number(me.amount))}</em></i></h4><hr>`);
			
			let nssf = 0.1 * me.amount;
			let amount_exclude_nssf = me.amount - nssf;
			let nhif = 0.03 * me.amount;
			let paye = 0.05 * amount_exclude_nssf;
			let heslb = 0.15 * me.amount;
			let wcf = 0.01 * me.amount;
			let net_salary = me.amount - nssf - paye - nhif - heslb;
			let total_employee_deductions = nssf + paye + nhif + heslb;
			let total_employer_contributions = nssf + paye + nhif + wcf;

			me.page.main.find(".salary_description").append(`
				<table class="table table-sm table-light table-hover table-striped">
					<tr><th class="text-left">Salary Component</th><th class="text-center">Employee Earnings</th>
					<th class="text-center">Employee Deductions</th><th class="text-center">Employer Contributions</th></tr>
					<tr><td>Net Salary</td><td class="text-right">${format_money(net_salary)}</td><td></td><td></td><td></td></tr>
					<tr><td>NSSF</td><td></td><td class="text-right">${format_money(nssf)}</td><td class="text-right">${format_money(nssf)}</td></tr>
					<tr><td>PAYE</td><td></td><td class="text-right">${format_money(paye)}</td><td class="text-right">${format_money(paye)}</td></tr>
					<tr><td>NHIF</td><td></td><td class="text-right">${format_money(nhif)}</td><td class="text-right">${format_money(nhif)}</td></tr>
					<tr><td>HESLB</td><td></td><td class="text-right">${format_money(heslb)}</td><td></td></tr>
					<tr><td>WCF</td><td></td><td></td><td class="text-right">${format_money(wcf)}</td></tr>
					<tr><td>Total</td><td class="text-right">${format_money(net_salary)}</td>
					<td class="text-right">${format_money(total_employee_deductions)}</td>
					<td class="text-right">${format_money(total_employer_contributions)}</td></tr>
				</table>
			`);
			
			let ctc = Number(me.amount) + Number(total_employer_contributions);
			me.page.main.find(".ctc").html(`<h4><i><em>Cost To Company: <b>${format_money(ctc)}</b></em></i></h4>`);
			
		} else {
			me.page.main.find(".salary_description").html(`
				<div align="center">
					<br><br>${__("No records..")}<br><br>
				</div>`);
		}
	};

	show_deductions_category() {
		let me = this;
		me.page.main.find(".deduction_percents").html(`
			<table class="table table-sm table-secondary table-hover" align='center'>
				<tr><td>NSSF <b>10%</td><td>PAYE <b>5%</td><td>NHIF <b>3%</b></td>
				<td>HESLB <b>15%</b></td><td>WCF <b>1%</b></td></tr>
			</table>`)
	};

	refresh() {
		let me = this;
		me.on("click", function() {
			me.amount = ""
		})
	}
};
