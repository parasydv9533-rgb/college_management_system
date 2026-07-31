
import tkinter as tk
from tkinter import ttk

from controller.fee_controller import FeeController


class FeeView:

    def __init__(self):

        self.controller = FeeController()

        self.window = tk.Toplevel()

        self.window.title("Fee Management")

        self.window.geometry("900x600")

        self.create_widgets()

        self.show_fees()

    def create_widgets(self):

        tk.Label(
            self.window,
            text="Fee Management",
            font=("Arial",16,"bold")
        ).pack(pady=10)

        form = tk.Frame(self.window)
        form.pack()

        # Fee ID

        tk.Label(
            form,
            text="Fee ID"
        ).grid(row=0,column=0,padx=10,pady=5)

        self.fee_id = tk.Entry(form)

        self.fee_id.grid(row=0,column=1)

        # Student ID

        tk.Label(
            form,
            text="Student ID"
        ).grid(row=0,column=2,padx=10,pady=5)

        self.student_id = tk.Entry(form)

        self.student_id.grid(row=0,column=3)

        # Total Fee

        tk.Label(
            form,
            text="Total Fee"
        ).grid(row=1,column=0,padx=10,pady=5)

        self.total_fee = tk.Entry(form)

        self.total_fee.grid(row=1,column=1)

        # Paid Fee

        tk.Label(
            form,
            text="Paid Fee"
        ).grid(row=1,column=2,padx=10,pady=5)

        self.paid_fee = tk.Entry(form)

        self.paid_fee.grid(row=1,column=3)

        # Remaining Fee

        tk.Label(
            form,
            text="Remaining Fee"
        ).grid(row=2,column=0,padx=10,pady=5)

        self.remaining_fee = tk.Entry(form)

        self.remaining_fee.grid(row=2,column=1)

        # Payment Date

        tk.Label(
            form,
            text="Payment Date"
        ).grid(row=2,column=2,padx=10,pady=5)

        self.payment_date = tk.Entry(form)

        self.payment_date.grid(row=2,column=3)

        # Status

        tk.Label(
            form,
            text="Status"
        ).grid(row=3,column=0,padx=10,pady=5)

        self.status = ttk.Combobox(
            form,
            values=["Paid", "Pending"],
            state="readonly",
            width=18
        )

        self.status.grid(row=3,column=1)

                # ==========================
        # Buttons
        # ==========================

        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Save",
            width=12,
            command=self.save_fee
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Update",
            width=12,
            command=self.update_fee
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Delete",
            width=12,
            command=self.delete_fee
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            button_frame,
            text="Search",
            width=12,
            command=self.search_fee
        ).grid(row=0, column=3, padx=5)

        tk.Button(
            button_frame,
            text="Show All",
            width=12,
            command=self.show_fees
        ).grid(row=0, column=4, padx=5)

        tk.Button(
            button_frame,
            text="Clear",
            width=12,
            command=self.clear_fields
        ).grid(row=0, column=5, padx=5)


        

        # ==========================
        # Table
        # ==========================

        table_frame = tk.Frame(self.window)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        scroll = tk.Scrollbar(table_frame)
        scroll.pack(side="right", fill="y")

        self.tree = ttk.Treeview(

            table_frame,

            columns=(

                "Fee ID",
                "Student ID",
                "Total Fee",
                "Paid Fee",
                "Remaining Fee",
                "Payment Date",
                "Status"

            ),

            show="headings",

            yscrollcommand=scroll.set

        )

        scroll.config(command=self.tree.yview)

        self.tree.heading("Fee ID", text="Fee ID")
        self.tree.heading("Student ID", text="Student ID")
        self.tree.heading("Total Fee", text="Total Fee")
        self.tree.heading("Paid Fee", text="Paid Fee")
        self.tree.heading("Remaining Fee", text="Remaining Fee")
        self.tree.heading("Payment Date", text="Payment Date")
        self.tree.heading("Status", text="Status")

        self.tree.column("Fee ID", width=80)
        self.tree.column("Student ID", width=100)
        self.tree.column("Total Fee", width=120)
        self.tree.column("Paid Fee", width=120)
        self.tree.column("Remaining Fee", width=120)
        self.tree.column("Payment Date", width=130)
        self.tree.column("Status", width=100)

        self.tree.pack(fill="both", expand=True)

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.select_record
        )

            # ==========================
    # Save Fee
    # ==========================

    def save_fee(self):

        self.controller.save_fee(

            self.student_id.get(),
            self.total_fee.get(),
            self.paid_fee.get(),
            self.remaining_fee.get(),
            self.payment_date.get(),
            self.status.get()

        )

        self.clear_fields()

        self.show_fees()

    # ==========================
    # Update Fee
    # ==========================

    def update_fee(self):

        self.controller.update_fee(

            self.fee_id.get(),
            self.student_id.get(),
            self.total_fee.get(),
            self.paid_fee.get(),
            self.remaining_fee.get(),
            self.payment_date.get(),
            self.status.get()

        )

        self.clear_fields()

        self.show_fees()

    # ==========================
    # Delete Fee
    # ==========================

    def delete_fee(self):

        self.controller.delete_fee(
            self.fee_id.get()
        )

        self.clear_fields()

        self.show_fees()

        # ==========================
    # Search Fee
    # ==========================

    def search_fee(self):

        row = self.controller.search_fee(
            self.fee_id.get()
        )

        if row:

            self.clear_fields()

            self.fee_id.insert(0, row[0])
            self.student_id.insert(0, row[1])
            self.total_fee.insert(0, row[2])
            self.paid_fee.insert(0, row[3])
            self.remaining_fee.insert(0, row[4])
            self.payment_date.insert(0, row[5])
            self.status.set(row[6])

    # ==========================
    # Show All Fees
    # ==========================

    def show_fees(self):

        self.tree.delete(*self.tree.get_children())

        rows = self.controller.get_all_fees()

        for row in rows:

            self.tree.insert(
                "",
                tk.END,
                values=row
            )

    # ==========================
    # Select Record
    # ==========================

    def select_record(self, event):

        selected = self.tree.focus()

        values = self.tree.item(selected, "values")

        if values:

            self.clear_fields()

            self.fee_id.insert(0, values[0])
            self.student_id.insert(0, values[1])
            self.total_fee.insert(0, values[2])
            self.paid_fee.insert(0, values[3])
            self.remaining_fee.insert(0, values[4])
            self.payment_date.insert(0, values[5])
            self.status.set(values[6])

    # ==========================
    # Clear Fields
    # ==========================

    def clear_fields(self):

        self.fee_id.delete(0, tk.END)
        self.student_id.delete(0, tk.END)
        self.total_fee.delete(0, tk.END)
        self.paid_fee.delete(0, tk.END)
        self.remaining_fee.delete(0, tk.END)
        self.payment_date.delete(0, tk.END)
        self.status.set("")
