# PST2021
Fool Me Once: A Study of Password Selection Evolution over the Past Decade



**Algorithm 1**
Simplified algorithm for finding date and service related to leaked credentials using the API

**Input:** The email address to check and a list of header variables including the API key
**Output:** A list containing information about matching breaches where the provided email address was found

response <- HTTP GET(URL, email, header)
return response[name, breach_date]
