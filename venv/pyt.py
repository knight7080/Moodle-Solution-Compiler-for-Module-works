import pdfkit

# Create a Configuration object with the correct wkhtmltopdf executable path
config = pdfkit.configuration(wkhtmltopdf="C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe")

# Use the config object when calling pdfkit.from_url
pdfkit.from_url('https://google.com', 'out.pdf', configuration=config)
