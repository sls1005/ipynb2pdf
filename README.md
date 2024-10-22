This is a tool for turning `.ipynb` files into PDF. It's a workaround, is designed to function without LaTeX, and is only intended to be used **without** any internet access.

### Warning

* Please note that this script depends on a deprecated (and possibly insecure) package. Therefore, this is possibly insecure as well. Never use it with internet access. You have been warned.

### Requirements

* Python 3.8 or later

* [__nbconvert__](https://nbconvert.readthedocs.io/en/latest/#)

    ```sh
    $ pip install nbconvert
    ```

* [__pdfkit__](https://github.com/JazzCore/python-pdfkit)

    ```sh
    $ pip install pdfkit
    ```

    Please note that this package is said to have been deprecated.
    You may also need to install `wkhtmltopdf` for using with this.

### Usage

Remember to turn off your Wi-Fi or internet access before using the following command:

```sh
$ python ipynb2pdf.py <file>
```

Where `<file>` is the name of the input file. If you have turned off the internet access as suggested, there may be error messages due to doing so. These are not considered relevant, as long as they are related with the lack of internet.

### How it works

The input is firstly turned into HTML form, and then to PDF. So this can possibly be used in systems without LaTeX support.