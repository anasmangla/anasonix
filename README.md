# Anasonix

Anasonix is a website project built using modern web technologies. This repository currently contains images for Anasonix, including the project logo. The goal is to develop a full website using Tailwind CSS, Font Awesome icons, and other modern tools.

## Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd anasonix
   ```
2. **Install dependencies**
   Install Node.js packages and other assets:
   ```bash
   npm install
   ```
3. **Run the development server**
   ```bash
   npm run dev
   ```

   This starts a local server with hot reloading so you can develop quickly.
You can modify the HTML files under `src/` while this server runs. Changes are compiled into `dist/` automatically.


## Building the Project

1. **Compile for production**
   ```bash
   npm run build
   ```
The optimized files will be placed in the `dist/` directory.

## Basic Landing Page

A simple `index.html` page is included. It uses Tailwind via a CDN link and
displays the Anasonix logo. Upload this file (along with `images/`) to your
web host if you want a quick placeholder page without running the build step.

## Project Structure
- `index.html` – quick landing page using Tailwind CDN.
- `src/` – place your HTML templates, CSS (`input.css`), and any client-side JavaScript while running `npm run dev` to rebuild automatically.
- `dist/` – compiled output from the dev and build scripts.
- `images/` – static assets like logos.
- `tests/` – Jest test files.


## Running Tests

The project includes a simple test suite. You can run it with npm or via the provided Makefile:

```bash
npm test       # run tests directly
make test      # equivalent wrapper defined in the Makefile
```

## Deployment

Upload the contents of `dist/` to your preferred hosting provider (e.g., Netlify, Vercel, or a traditional web server).


## Technologies Used

- **Tailwind CSS** for utility-first styling.
- **Font Awesome** for icons.
- **JavaScript** tooling via npm scripts.
- Optionally integrate additional tools like Webpack or Vite as the project grows.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or collaboration opportunities, please contact:

- **Anas Mangla** – [anas.mangla@gmail.com](mailto:anas.mangla@gmail.com)

## Troubleshooting

If `npm install` fails due to blocked domains (for example, access to
`mise.jdx.dev` is restricted), update your network settings or proxy
configuration and try again.
