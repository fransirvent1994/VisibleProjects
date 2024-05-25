from fpdf import FPDF # First we import the fpdf library

# Then we declare a class named pdf which contains the functions needed to create our pdf
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12) # Font style
        

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

# This functions will be the main (the most important) bc it will contain the texts that will be shown on the pdf.
def main():
    pdf = PDF()
    pdf.add_page()

    # Text intro
    intro_text = (
        "INTRODUCTION"
    )
    pdf.chapter_body(intro_text)

    # Text body
    background_text = (
        "BODY TEXT"
    )
    pdf.chapter_body(background_text)

    # To end
    closing_text = (
        "YOUR FINAL TEXT"
    )
    pdf.chapter_body(closing_text)

    pdf.output('your_archive_name.pdf') # Last the name of the pdf

if __name__ == '__main__':
    main()
