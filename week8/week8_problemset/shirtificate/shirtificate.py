from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Times", "B", 50)
        self.cell(80)
        self.cell(30, 40, "CS50 Shirtificate", border=None, align="C")
        self.ln(20)

def main():
    name = input("Name: ")
    pdf = PDF(orientation="P", format="A4")
    pdf.add_page()
    pdf.image("shirtificate.png", w=190, y=60, keep_aspect_ratio=True)
    pdf.set_font("Times", size=20)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(h=180, text=f"{name} took CS50", align="C", center=True)
    #pdf.text(74, 130, text=f"{name} took CS50")



    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()


