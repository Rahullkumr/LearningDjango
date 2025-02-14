# Day 25: 14 Feb 2025

- completed all 4 apps navigation and routing 

- Observed a problem with Manual Routing
    
- `Manual Routing` The link that we manually copy paste into `<a href='here'>` from url which contains the port number 

- Eg (Manual Routing): An item from navbar
    ```
    <a href="http://127.0.0.1:8000/electronics/">Electronics</a>
    ```

## Problem with Manual routing 

- If you run the server with different port number other than 8000.

- The links in the navbar will not work because they are configured with port number 8000

## Solution

- Dynamic routing using `url dtl tag`

