import os
import shutil
import flask
from flask import Flask, render_template, send_file
import pdfkit
import jdatetime

app = Flask(__name__)

customer_name = 'امین رستگاری'
economical_number = input('economical_number: ')
registration_number = input('registration_number: ')
national_code = input('national_code: ')
state = input('state: ')
city = input('city: ')
postal_code = input('postal_code: ')
address = input('address: ')
phone_number = input('phone_number: ')

context = {
    'today': jdatetime.date.today(),
    'customer_name': customer_name,
    'economical_number': economical_number,
    'registration_number': registration_number,
    'national_code': national_code,
    'state': state,
    'city': city,
    'postal_code': postal_code,
    'address': address,
    'phone_number': phone_number
    }


def find_wkhtmltopdf():
    """Locate the wkhtmltopdf binary without hardcoding a Windows-only path.

    Resolution order:
      1. WKHTMLTOPDF_PATH environment variable, if set.
      2. Whatever `wkhtmltopdf` resolves to on PATH (works out of the box on
         Linux/macOS after `apt install wkhtmltopdf` / `brew install
         wkhtmltopdf`, and on Windows too once its install dir is on PATH).
      3. The default Windows install location, as a last-resort fallback.
    """
    env_path = os.environ.get('WKHTMLTOPDF_PATH')
    if env_path and os.path.exists(env_path):
        return env_path

    which_path = shutil.which('wkhtmltopdf')
    if which_path:
        return which_path

    windows_default = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    if os.path.exists(windows_default):
        return windows_default

    raise FileNotFoundError(
        "Could not find wkhtmltopdf. Install it "
        "(https://wkhtmltopdf.org/downloads.html) and either add it to your "
        "PATH or set the WKHTMLTOPDF_PATH environment variable to its full "
        "path."
    )


@app.route('/', methods=['GET', 'POST'])
def getvalue():
    today = jdatetime.date.today()
    return render_template('pass_data.html', **context, charset='UTF-8')


@app.route('/download', methods=['GET', 'POST'])
def download_file():
    # Render your template and save it as a file
    rendered_template = render_template('pass_data.html', **context, charset='UTF-8')

    # Configure pdfkit to use the path to the wkhtmltopdf executable
    config = pdfkit.configuration(wkhtmltopdf=find_wkhtmltopdf())

    # Convert the rendered template to PDF
    pdf_file = 'templates/output.pdf'
    pdfkit.from_string(rendered_template, pdf_file, configuration=config)

    # Send the file to the client for download
    return send_file(pdf_file, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
