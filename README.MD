# API Test Practice

This project contains automated API tests using `pytest` and Allure reporting. You can run the tests locally or in Docker.

---

## Project Structure

```
.
├── requirements.txt
├── Dockerfile
├── .env.local
├── tests/
│   └── test_auth.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
└── allure-results/
```

---

## Environment Variables

Tests require:
- `BASE_URL`: The API endpoint to test against (e.g., `http://localhost:8000`)
- `API_KEY`: The API key for authentication

You can set these variables either directly in your shell or by using a `.env` file.

### Sample `.env.local`
```dotenv
BASE_URL=http://host.docker.internal:8000
API_KEY=secret-demo-key
```
**Note:**  
- Use `host.docker.internal` for Docker to access services running on your host machine (Mac/Windows).
- Change the port (`8000`) if your API uses a different one.
- You can create multiple `.env` files for different environments (e.g. `.env.dev`, `.env.prod`).

---

## How to Run the Tests

### 1. **Locally in the terminal**

```sh
export BASE_URL=http://localhost:8000
export API_KEY=secret-demo-key
pytest -v --alluredir allure-results
```

### 2. **Using Docker**

#### First time (or after code changes):
```sh
docker build -t api-tests .
```

#### Run tests (always use the right `.env` file):
```sh
docker run --rm --env-file .env.local api-tests
```

#### For subsequent runs (no code changes):
```sh
docker run --rm --env-file .env.local api-tests
```

---

## Viewing Allure Report

After running the tests:
```sh
allure serve allure-results
```
This will start a local server and open the report in your browser.

---

## Troubleshooting

- **Connection Errors:**  
  If you see errors like `ConnectionRefusedError`, check that your API server is running and accessible at the address specified in `BASE_URL`.

- **Docker Networking (API on host):**  
  Use `BASE_URL=http://host.docker.internal:<port>` for Mac/Windows.  
  On Linux, you may need to expose the API differently—see Docker documentation for details.

- **Environment File:**  
  If you have multiple environments, create different `.env` files and specify which one to use with `--env-file`.

---

## Useful Commands

- **Rebuild Docker image without cache:**
  ```sh
  docker build --no-cache -t api-tests .
  ```

- **Clean up old Docker images:**
  ```sh
  docker system prune -a
  ```

---

## Contributing

Feel free to open issues or submit pull requests for improvements.

---

## License

MIT