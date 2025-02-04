# Markdown Viewer Application

This application allows users to convert local Markdown files into HTML format. It extracts metadata such as title, description, and author from the Markdown file and uses them in the HTML page's meta tags, displaying only the Markdown content in the visual part of the page. Additionally, a footer section is included at the bottom of the page.

## Features

- **Convert Markdown Files:** Converts Markdown files into HTML format.
- **Utilize Metadata:** Extracts metadata like `title`, `description`, and `author` from the Markdown file and uses them in the page's title and meta tags.
- **Dynamic Content:** The Markdown content is converted into HTML and displayed within the page.
- **Footer Section:** Includes a footer at the bottom of the page with copyright information.
- **Favicon Support:** Displays the application icon (favicon) in the browser tab.

## Usage

1. Drag and drop the Markdown file into the application window.
2. The application will extract the title and description from the Markdown file.
3. The converted HTML page will open in a new tab.

## Installation

This application is written in Python and can be run by following these steps:

1. Ensure you have Python installed (Python 3.7 or higher recommended).
2. Install the required libraries by running the following command in the terminal or command prompt:

    ```bash
    pip install markdown
    ```

3. Then, you can run the Python file of the application:

    ```bash
    python markdown_viewer.py
    ```

4. Drag and drop the Markdown file and press **Enter**. The application will convert the file to HTML and display it in the browser.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork this repository.
2. Make your changes and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
